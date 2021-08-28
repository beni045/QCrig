import numpy as np

import logging
logger = logging.getLogger(__name__)

def find_stl_height(x_distance, y_distance, range, stl_mesh_vectors):
    """
    Brief: Find closest point to given x and y with maximum height z
    :param x_distance: x distance in mm
    :param p2: y distance in mm
    :param p3: range to look for points around given x,y distances
    :param stl_mesh_vectors: np array of stl mesh
    :returns: None if no points found in given range
              Maximum z distance of points found in range
    """ 

    logging.info('Find stl height params -  x_distance: {}mm, y_distance: {}mm, range: {}mm'.format(x_distance,y_distance,range))

    x = stl_mesh_vectors[:,:,0].flatten()
    y = stl_mesh_vectors[:,:,1].flatten()

    x_lower = x > (x_distance - (range / 2))
    x_upper = x < (x_distance + (range / 2))
    y_lower = y > (y_distance - (range / 2))
    y_upper = y < (y_distance + (range / 2))

    overlap = x_lower * x_upper * y_lower * y_upper
    if not True in overlap:
        logger.cirtical('Find stl height no points within range found')
        return None
    
    indices = np.where(overlap)

    logging.info('Find stl height number of points in range found: {}'.format(len(indices)))
    z_max = stl_mesh_vectors[:,:,2].flatten()[indices].max()

    return z_max



if __name__ == "__main__":
    from stl import mesh

    sole_stl_mesh = mesh.Mesh.from_file('HighArch_L_Insole.stl').vectors

    y_max = find_stl_height(140, -20, 3, sole_stl_mesh)

    print("y_max", y_max)

    print(sole_stl_mesh.shape)
    print(sole_stl_mesh[:,:,0,].max())
    print(sole_stl_mesh[:,:,1,].max())
    print(sole_stl_mesh[:,:,2,].max())

