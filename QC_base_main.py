import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtCore import QTimer
import home_icons_rc
from QC_base_UI import Ui_MainWindow

import cv2
from pyzbar import pyzbar

from configparser import ConfigParser

from stl import mesh
import numpy as np
from stl_height_finder import find_stl_height
from sole_size import find_sides

from API_Library import retrieve_insole_data, retrieve_insole_stl
from validator import validate_arch_height, validate_compressions, \
                      validate_length, validate_weight

from baseconv import base36

from internet_test import isConnected

import logging


logging.basicConfig(
    level = logging.DEBUG,
    format = '{asctime} {levelname:<8} {message}',
    style = '{',
    filename = 'QCrig.log',
    filemode = 'a'
)

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        logging.debug('Init UI success')

        # Read configs 
        parser = ConfigParser()
        parser.read('config.ini')
        logging.debug('Config file read success')

        self.sole_data = {}      # sole data including target and measured QC values
        self.qc_thresholds = parser._sections['qc_thresholds']  # threshold config for qc pass or fail
        self.stl_height_params = parser._sections['stl_height_params']
        self.sole_size_params = parser._sections['sole_size_params']
        self.size_conversions = parser._sections['length_conversions']

        # RUN MODE FLAGS
        self.QRdebug = True  # if True, use dummy production id instead of QR code
        self.process_arch = True  # if True, include arch in QC process
        self.uart = False   # Can set to False for testing UI on PC (dummy values used for arch, compression, weight QC)

        if not self.uart:
            logging.warning('flag self.uart is False, running in PC test mode')
        if self.QRdebug:
            logging.warning('flag self.QRdebug is True, using dummy production_id (2469) for sole data')
        if not self.process_arch:
            logging.warning('flag self.process_arch is False, arch params excluded from QC process')

        # Init uart to use with Arduino
        if self.uart:
            try:
                import serial
                self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
                self.ser.flush()   
                logging.info('Init UART success')
            except Exception as e:
                logging.critical('Init UART error', exc_info=True)


        # Declare button click connections for all pages of UI
        self.ui.startQC_button.clicked.connect(self.start_page2)
        self.ui.startQCprocess_button.clicked.connect(self.start_page4)
        self.ui.test_another_button.clicked.connect(self.start_page1)
        self.ui.more_details_button.clicked.connect(self.start_page6)
        self.ui.test_another_button_2.clicked.connect(self.start_page1)
        self.ui.page6_back_button.clicked.connect(self.start_page5)
        self.ui.back_to_main_button.clicked.connect(self.start_page1)
        
        self.ui.log_button.clicked.connect(self.toggle_log)
        logging.debug('Init buttons success')

        self.log_on = True

        self.check_internet()

        self.cap = None  # Will be later used for camera capture
        self.timer = None  # Will be used for live camera feed callback timer

        # Starting point is page 1
        self.start_page1()
        logging.debug('MainWindow init finish')


    def show(self):
        self.main_win.show()


    def start_page1(self):
        if isinstance(self.cap, cv2.VideoCapture):
            self.cap.release()
        if isinstance(self.timer, QTimer):
            self.timer.stop()
    
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/dev_green.png"), QIcon.Normal, QIcon.Off)
        self.ui.log_button.setIcon(icon)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        logging.debug('start_page1 finish')


    def start_page2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        try:
            self.cap = cv2.VideoCapture(0)
            logging.debug('QR scan open camera success')
        except Exception as e:
            logging.critical('QR scan open camera error', exc_info=True)

        self.timer = QTimer()
        self.QR_count = 0
        self.timer.start(20)
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        logging.debug('start_page2 finish')


    # Get frame from camera and scan for QR code
    def viewCam(self):
        # read image in BGR format
        ret, img = self.cap.read()
        # detect QR code
        detections = pyzbar.decode(img, symbols=[pyzbar.ZBarSymbol.QRCODE])
        # convert image to RGB format
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # qr code found
        if len(detections) > 0:
            data = detections[0].data.decode("utf-8") 
            # display success text
            cv2.putText(img, "PROCESSING QR CODE", (int(img.shape[1] / 8), int(img.shape[0] - (img.shape[0] * 0.2))), cv2.FONT_HERSHEY_SIMPLEX,
                        1.5, (0, 255, 0), 4)
            height, width, channel = img.shape
            step = channel * width
            qImg = QImage(img.data, width, height, step, QImage.Format_RGB888)
            self.ui.QC_scan_label.setPixmap(QPixmap.fromImage(qImg))  # display img in label
            self.QR_count += 1

            # Need 2 consecutive successful scans for robustness
            if self.QR_count > 1:
                logging.debug('QR code scan success')
                logging.debug('QR code: {}'.format(data))  # TODO: wasnt printing properly??
                self.timer.timeout.disconnect(self.viewCam)
                self.timer.stop()
                # process the QR code and start next page   
                self.cap.release()              
                logging.debug('QR code found')     
                self.process_QR(data)
                self.start_page3()

        # no qr found, just display image and reset timer
        else:
            self.QR_count = 0
            cv2.putText(img, "SCAN QR CODE", (int(img.shape[1] / 5), int(img.shape[0] - (img.shape[0] * 0.2))), cv2.FONT_HERSHEY_SIMPLEX,
                        1.5, (255, 0, 0), 4)
            # get image infos
            height, width, channel = img.shape
            step = channel * width
            # create QImage from image
            qImg = QImage(img.data, width, height, step, QImage.Format_RGB888)
            # show image in a label
            self.ui.QC_scan_label.setPixmap(QPixmap.fromImage(qImg))
            # start timer again
            self.timer.start(20)


    def process_QR(self, qr_data):
        # Tare the scale before sole is placed on bed
        if self.uart:
            logging.debug('Send TARE command to Arduino')
            self.ser.write(b"TARE;")

        # get sole data and save to member dict
        if not self.QRdebug:
            decoded_qr = self.decode_qr(qr_data)
        else:
            logging.warning('Using dummy prod id 2469')
            decoded_qr = '2469'

        # test if internet working and change wifi icon accordingly
        self.check_internet()

        # Retrieve sole data from db and log if expected keys not present
        try:
            sole_data = retrieve_insole_data(decoded_qr).json()
            logging.debug('Retrieve sole data success')
            logging.debug('Sole data: \n{}'.format(sole_data))
        except Exception as e:
            logging.critical('Retrieve sole data error', exc_info=True)

        try:
            self.sole_data['ID'] = decoded_qr
            self.sole_data['volume'] = sole_data['FilamentConsumption_mm3']
            self.sole_data['printer'] = sole_data['printer']
            self.sole_data['shoe_size'] = str(sole_data['streetSize']) 
            self.sole_data['side'] = sole_data['foot_chirality']
            self.sole_data['target_side'] = sole_data['foot_chirality']
        except Exception as e:
            logging.critical('Key error for retrieved sole data. Maybe a bug for this prod id: {}'.format(decoded_qr), exc_info=True)

        # get sole stl and save to file
        try:
            sole_stl = retrieve_insole_stl(decoded_qr).content
            logging.debug('Retrieve sole stl success')
        except Exception as e:
            logging.critical('Retrieve sole stl error', exc_info=True)

        with open('current_sole_stl.stl', 'wb+') as file:
            file.write(sole_stl)
        logging.debug('Sole data saved locally as current_sole_stl.stl')
        
        # get size of sole stl to use as targt size
        sole_stl_mesh = mesh.Mesh.from_file('current_sole_stl.stl').vectors
        self.sole_data['size']=str(round(sole_stl_mesh[:,:,0,].max()))
        logging.debug('Sole size calculated from stl file: {} mm'.format(self.sole_data['size']))
    

    def decode_qr(self, data):
        # Example: Decode the following to 3455
        # https://ca.casca.com/002NZ-001YP-VA-IN-a0-01
        try: 
            serial_code = data[len('https://ca.casca.com/'):]
            production_id_base36 = serial_code.split('-', 1)[0]
            production_id_decimal = base36.decode(production_id_base36.lower())
            logging.debug('Decode QR code success')
            logging.debug('Decoded QR code: {}'.format(production_id_decimal))
        except Exception as e:
            logging.critical('Decode QR code error', exc_info=True)
        return production_id_decimal


    def process_stl_height(self):
        sole_stl_mesh = mesh.Mesh.from_file('current_sole_stl.stl')

        self.sole_data['target_arch'] = round(find_stl_height(
            int(self.stl_height_params['x_distance']),
            int(self.stl_height_params['y_distance']),
            float(self.stl_height_params['range']),
            sole_stl_mesh.vectors
        ))


    def start_page3(self):
        self.ui.page3_ID_label.setText(self.sole_data['ID'])
        self.ui.page3_printer_label.setText(self.sole_data['printer'])
        self.ui.page3_size_label.setText(self.sole_data['shoe_size'])
        self.ui.page3_side_label.setText(self.sole_data['side'])
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        logging.debug('start_page3 finish')


    def start_page4(self):
        self.ui.progressBar.setValue(0)
        self.ui.part_ID_label.setText(self.sole_data['ID'])
        self.ui.printer_label.setText(self.sole_data['printer'])
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)
        self.qc_process()
        logging.debug('start_page4 finish')


    def qc_process(self):
        self.ui.QC_status_label.setText("Processing size and side")
        # target size, weight, compression, arch
        self.sole_data['target_size'] = self.sole_data['size']
        self.sole_data['target_weight'] = str(round(float(self.sole_data['volume']) * 0.00112))
        self.sole_data['target_compression'] = '55 - 75'
        if self.process_arch:
            self.process_stl_height()   # sets self.sole_data['target_arch'] implicitly
        else:
            self.sole_data['target_arch'] = '22'

        # measured size, weight, compression, arch
        self.process_sole_size_side()    # sets self.sole_data['measured_size'] implicitly
        self.ui.progressBar.setValue(25)

        if self.uart:
            self.ui.QC_status_label.setText("Processing weight")
            logging.debug('Send WEIGHT command to Arduino')
            self.ser.write(b"WEIGHT;")
            while True:
                if self.ser.in_waiting > 0:
                    uart_data = self.ser.readline().decode('utf-8').rstrip()
                    self.check_if_number(uart_data)
                    self.sole_data['measured_weight'] = uart_data
                    logging.debug('Received data from Arduino: {}'.format(self.sole_data['measured_weight']))
                    break
            self.ui.progressBar.setValue(50)

            self.ui.QC_status_label.setText("Processing compression")
            logging.debug('Send COMPRESSION command to Arduino')
            self.ser.write(b"COMPRESSION;")
            while True:
                if self.ser.in_waiting > 0:
                    uart_data = self.ser.readline().decode('utf-8').rstrip()
                    self.check_if_number(uart_data)
                    self.sole_data['measured_compression'] = uart_data
                    logging.debug('Received data from Arduino: {}'.format(self.sole_data['measured_compression']))
                    break
            self.ui.progressBar.setValue(75)

            if self.process_arch:
                self.ui.QC_status_label.setText("Processing arch")
                logging.debug('Send ARCH command to Arduino')
                self.ser.write(b"ARCH;50;1")
                while True:
                    if self.ser.in_waiting > 0:
                        uart_data = self.ser.readline().decode('utf-8').rstrip()
                        self.check_if_number(uart_data)
                        self.sole_data['measured_arch'] = uart_data
                        logging.debug('Received data from Arduino: {}'.format(self.sole_data['measured_arch']))
                        break
                self.ui.progressBar.setValue(100)
                
        # For testing on PC
        else:
            self.sole_data['measured_weight'] = '50'
            self.sole_data['measured_compression'] = '20'
            self.sole_data['measured_arch'] = '30'

        self.check_internet()
        self.validate_results()
        self.start_page5()


    # Check if string is a number (float or int)
    def check_if_number(self, a):
        if a.isdigit():
            return
        elif a.replace('.','',1).isdigit() and a.count('.') < 2:
            return
        else:
            logging.critical('Command error received from Arduino')
            return


    def validate_results(self):
        logging.debug('Start vaidate QC results')

        # Validate functions, thresholds and logging done implicitly
        size_result = validate_length(float(self.sole_data['size']), float(self.sole_data['measured_size']))
        weight_result = validate_weight(float(self.sole_data['target_weight']), float(self.sole_data['measured_weight']))
        compression_result = validate_compressions(float(self.sole_data['measured_compression']))

        # Explicit side validation
        side_result = True if(self.sole_data['target_side'] == self.sole_data['measured_side']) else False
        if side_result:
            logging.info('validate_side PASS')
        else:
            logging.info('validate_side FAIL')

        if self.process_arch:
            arch_result = validate_arch_height(float(self.sole_data['target_arch']), float(self.sole_data['measured_arch']))
        else:
            arch_result = True

        self.ui.page5_size_label.setText('Pass' if size_result else 'Fail')
        self.ui.page5_weight_label.setText('Pass' if weight_result else 'Fail')
        self.ui.page5_comp_label.setText('Pass' if compression_result else 'Fail')
        self.ui.page5_side_label.setText('Pass' if side_result else 'Fail')

        if self.process_arch:
            self.ui.page5_arch_label.setText('Pass' if arch_result else 'Fail')
        else:
            self.ui.page5_arch_label.setText('N/A')

        # Set result icon 
        if False in [size_result, weight_result, compression_result, arch_result]:
            self.ui.QC_result_label.setPixmap(QPixmap(":/newPrefix/fail_result.png"))
        else:
            self.ui.QC_result_label.setPixmap(QPixmap(":/newPrefix/done_tick.svg"))


    def process_sole_size_side(self):
        try:
            self.cap = cv2.VideoCapture(0)
            logging.debug('sole size open camera success')
        except Exception as e:
            logging.critical('sole size open camera error', exc_info=True)

        # read image in BGR format
        ret, img = self.cap.read()
        self.cap.release()

        # Rotate img
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        
        logging.debug('Run find_sides')
        #  Get index of tip pixel (toe) of the insole (top is y cord, side is x cord)
        top, side = find_sides(
                img, 
                float(self.sole_size_params['color_thresh']), 
                int(self.sole_size_params['calib_slice_range']), 
                float(self.sole_size_params['calib_x']), 
                float(self.sole_size_params['calib_y']),
                float(self.sole_size_params['crop_y_top']), 
                float(self.sole_size_params['crop_y_bottom']), 
                float(self.sole_size_params['crop_center']),
                return_cropped=False,
                save_result=True)   # Saves debug images to size_result folder

        logging.debug('Calculate sole size')
        #   Calculate sole size in mm
        offset = float(self.sole_size_params['offset'])
        size = float(self.sole_size_params['size_conv_factor']) * (img.shape[0] - top)
        real_size = size + offset
        self.sole_data['measured_size'] = round(real_size)

        logging.debug('Calculate sole side')
        #   Calculate side
        calib_line = round(float(self.sole_size_params['side_test_line']) * img.shape[1])
        s1 = calib_line - side
        if(s1 > 0):
            self.sole_data['measured_side'] = 'right'
        elif(s1 < 0):
            self.sole_data['measured_side'] = 'left'
        else:
            logging.critical('Sole side measurement error (calib_line - side == 0). Sole tip is at center line of sole')
            

    def start_page5(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
        logging.debug('start_page5 finish')


    def start_page6(self):
        self.ui.page6_ID_label_2.setText(self.sole_data['ID'])
        self.ui.page6_printer_label_2.setText(self.sole_data['printer'])

        if self.process_arch:
            self.ui.page6_t_arch_label.setText(str(self.sole_data['target_arch']))
        else:
             self.ui.page6_t_arch_label.setText('N/A')

        self.ui.page6_t_size_label.setText(self.sole_data['size'])
        self.ui.page6_t_weight_label.setText(str(self.sole_data['target_weight']))
        self.ui.page6_t_comp_label.setText(str(self.sole_data['target_compression']))
        self.ui.page6_t_side_label.setText(self.sole_data['target_side'])

        if self.process_arch:
            self.ui.page6_m_arch_label.setText(str(self.sole_data['measured_arch']))
        else:
            self.ui.page6_m_arch_label.setText('N/A')

        self.ui.page6_m_size_label.setText(str(self.sole_data['measured_size']))
        self.ui.page6_m_weight_label.setText(str(self.sole_data['measured_weight']))
        self.ui.page6_m_comp_label.setText(str(self.sole_data['measured_compression']))
        self.ui.page6_m_side_label.setText(self.sole_data['measured_side'])

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_6)
        logging.debug('start_page6 finish')


    def toggle_log(self):
        if self.log_on:
            icon = QIcon()
            icon.addPixmap(QPixmap(":/newPrefix/home_dev.png"), QIcon.Normal, QIcon.Off)
            self.ui.log_button.setIcon(icon)
            logging.getLogger().setLevel(logging.WARNING)
            self.log_on = False
        else:
            icon = QIcon()
            icon.addPixmap(QPixmap(":/newPrefix/dev_green.png"), QIcon.Normal, QIcon.Off)
            self.ui.log_button.setIcon(icon)
            logging.getLogger().setLevel(logging.DEBUG)
            self.log_on = True


    def check_internet(self):
        if not isConnected():
            logging.critical('Internet connection error')
            icon = QIcon()
            icon.addPixmap(QPixmap(":/newPrefix/wifi_red.png"), QIcon.Normal, QIcon.Off)
            self.ui.wifi_button.setIcon(icon)
        else:
            logging.debug('Internet connection working')
            icon = QIcon()
            icon.addPixmap(QPixmap(":/newPrefix/wifi_green.png"), QIcon.Normal, QIcon.Off)
            self.ui.wifi_button.setIcon(icon)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())