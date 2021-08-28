import cv2
import numpy as np

import logging
logger = logging.getLogger(__name__)

def find_sides(img, color_thresh, calib_slice_range, calib_x, calib_y, crop_y_top, crop_y_bottom, crop_center, return_cropped = False, save_result = False):
    """
    Brief: Find the top, left, right indices of edges of a sole
    :param img: np array image in BGR format
    :param color_thresh: +- this value to the calibration pixels to create masks
    :param calib_slice_range: how much to slice for calibration crop (both x and y)
    :param calib_x: cropping start value x for calibration pixels (decimal %)
    :param calib_y: cropping start value y for calibration pixels (decimal %)
    :param crop_y_top: percent of image to remove from top before searching for top y index
    :param crop_y_bottom: percent of image to remove from bottom before searching for top y index
    :param crop_center: percent of image to keep (crop left and right sides)
    :param return_cropped: return cropped image bool
    :param save_result: save debug images for calibrating color_thresh
    :returns: y index of top point on the sole 
    :returns: x index of top point on the sole
    """ 
    # Crop a small area of pixels to calibrate target color (use background, NOT the sole)
    x_calib_start = round(img.shape[1] * calib_x)
    y_calib_start = round(img.shape[0] * calib_y)

    # Use HSV color space (more robust with lighting)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    sample = img[y_calib_start : y_calib_start+calib_slice_range, 
                x_calib_start : x_calib_start+calib_slice_range].reshape(-1, 3)

    # Create boundaries based on a small cropped area and color threshold
    boundaries = []
    for pixel in sample:
      # Thresholding based on first index (Hue) which represents the color
      boundaries.append(([pixel[0] - color_thresh,0,0], [pixel[0] + color_thresh, 255, 255]))

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
        # find the colors within the specified boundaries and apply the mask
        mask = cv2.inRange(img, lower, upper)
        output = cv2.bitwise_and(img_gray, img_gray, mask = mask)

    # Crop some of the mask and find indices of top y, x
    y_cut_top = round(output.shape[0] * crop_y_top)
    y_cut_bottom = output.shape[0] - round(output.shape[0] * crop_y_bottom)
    x_cut = round(output.shape[1] * crop_center)
    x_center = output.shape[1] // 2
    idx = np.argwhere(output[y_cut_top: y_cut_bottom, x_center - x_cut : x_center + x_cut] == 0)

    # Find y index
    top_y = idx[:,0].min() + y_cut_top

    # Find x index
    top_idx = idx[:,0].argmin()
    top_x = idx[top_idx, 1] + (img.shape[1] // 2 - x_cut)
    
    # # Also find left and right sides (this is not used)
    # left_pix = idx[:,1].min() + x_center - x_cut
    # right_pix = idx[:,1].max() + x_center - x_cut
    
    # Save debug imgs
    if save_result:
        img_bgr = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        cv2.line(img_bgr, (top_x, 0), (top_x, img.shape[0]), (255,0,0), 2)
        cv2.line(img_bgr, (0, top_y), (img.shape[1], top_y), (255,0,0), 2)
        # cv2.line(img_bgr, (left_pix, 0), (left_pix, img.shape[0]), (255,0,0), 2)
        # cv2.line(img_bgr, (right_pix, 0), (right_pix, img.shape[0]), (255,0,0), 2)
        img_bgr = cv2.resize(img_bgr, (round(img_bgr.shape[1] * 0.75), round(round(img_bgr.shape[0]) * 0.75)))
        cv2.imwrite('size_result/sides.jpg', img_bgr) 
        cv2.imwrite('size_result/mask.jpg', output[y_cut_top: y_cut_bottom, x_center - x_cut : x_center + x_cut])

    # Return cropped image (for calibrating crop)
    if return_cropped:
      cropped = output[y_cut_top: y_cut_bottom, x_center - x_cut : x_center + x_cut]
      return cropped, top_y, top_x
    else:
      return top_y, top_x
    


if __name__ == '__main__':
  pass
