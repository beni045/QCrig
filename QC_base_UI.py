# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QC_base_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 60, 800, 421))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.startQC_button = QtWidgets.QPushButton(self.page_1)
        self.startQC_button.setGeometry(QtCore.QRect(100, 240, 600, 110))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startQC_button.setFont(font)
        self.startQC_button.setAutoFillBackground(False)
        self.startQC_button.setStyleSheet("background-color:rgb(255, 192, 9)")
        self.startQC_button.setAutoDefault(False)
        self.startQC_button.setFlat(False)
        self.startQC_button.setObjectName("startQC_button")
        self.label = QtWidgets.QLabel(self.page_1)
        self.label.setGeometry(QtCore.QRect(110, 60, 161, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/home_casca.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_1)
        self.label_2.setGeometry(QtCore.QRect(320, 100, 51, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/home_X.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_1)
        self.label_3.setGeometry(QtCore.QRect(390, 80, 321, 111))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/home_footb3d.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(270, 280, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(255, 192, 9)")
        self.label_6.setObjectName("label_6")
        self.QC_scan_label = QtWidgets.QLabel(self.page_2)
        self.QC_scan_label.setGeometry(QtCore.QRect(-10, -10, 791, 401))
        self.QC_scan_label.setText("")
        self.QC_scan_label.setAlignment(QtCore.Qt.AlignCenter)
        self.QC_scan_label.setObjectName("QC_scan_label")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.startQCprocess_button = QtWidgets.QPushButton(self.page_3)
        self.startQCprocess_button.setGeometry(QtCore.QRect(580, 230, 181, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startQCprocess_button.setFont(font)
        self.startQCprocess_button.setStyleSheet("background-color:rgb(255, 192, 9)\n"
"")
        self.startQCprocess_button.setObjectName("startQCprocess_button")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(30, 30, 521, 311))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/newPrefix/start_info.PNG"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(self.page_3)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 110, 341, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.page3_ID_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.page3_ID_label.setFont(font)
        self.page3_ID_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.page3_ID_label.setObjectName("page3_ID_label")
        self.verticalLayout_2.addWidget(self.page3_ID_label)
        self.page3_printer_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.page3_printer_label.setFont(font)
        self.page3_printer_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.page3_printer_label.setObjectName("page3_printer_label")
        self.verticalLayout_2.addWidget(self.page3_printer_label)
        self.page3_size_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.page3_size_label.setFont(font)
        self.page3_size_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.page3_size_label.setObjectName("page3_size_label")
        self.verticalLayout_2.addWidget(self.page3_size_label)
        self.page3_side_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.page3_side_label.setFont(font)
        self.page3_side_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.page3_side_label.setObjectName("page3_side_label")
        self.verticalLayout_2.addWidget(self.page3_side_label)
        self.layoutWidget1 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 110, 131, 201))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_19 = QtWidgets.QLabel(self.page_4)
        self.label_19.setGeometry(QtCore.QRect(270, -10, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color:rgb(255, 192, 9)")
        self.label_19.setObjectName("label_19")
        self.progressBar = QtWidgets.QProgressBar(self.page_4)
        self.progressBar.setGeometry(QtCore.QRect(100, 210, 600, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_20 = QtWidgets.QLabel(self.page_4)
        self.label_20.setGeometry(QtCore.QRect(30, 110, 92, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.part_ID_label = QtWidgets.QLabel(self.page_4)
        self.part_ID_label.setGeometry(QtCore.QRect(135, 110, 371, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.part_ID_label.setFont(font)
        self.part_ID_label.setObjectName("part_ID_label")
        self.label_22 = QtWidgets.QLabel(self.page_4)
        self.label_22.setGeometry(QtCore.QRect(31, 145, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.printer_label = QtWidgets.QLabel(self.page_4)
        self.printer_label.setGeometry(QtCore.QRect(135, 145, 421, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.printer_label.setFont(font)
        self.printer_label.setObjectName("printer_label")
        self.QC_status_label = QtWidgets.QLabel(self.page_4)
        self.QC_status_label.setGeometry(QtCore.QRect(140, 300, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.QC_status_label.setFont(font)
        self.QC_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.QC_status_label.setObjectName("QC_status_label")
        self.stackedWidget.addWidget(self.page_4)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_48 = QtWidgets.QLabel(self.page_6)
        self.label_48.setGeometry(QtCore.QRect(40, 315, 92, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.page6_ID_label_2 = QtWidgets.QLabel(self.page_6)
        self.page6_ID_label_2.setGeometry(QtCore.QRect(150, 315, 221, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.page6_ID_label_2.setFont(font)
        self.page6_ID_label_2.setObjectName("page6_ID_label_2")
        self.page6_printer_label_2 = QtWidgets.QLabel(self.page_6)
        self.page6_printer_label_2.setGeometry(QtCore.QRect(150, 350, 221, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.page6_printer_label_2.setFont(font)
        self.page6_printer_label_2.setObjectName("page6_printer_label_2")
        self.label_51 = QtWidgets.QLabel(self.page_6)
        self.label_51.setGeometry(QtCore.QRect(40, 350, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.layoutWidget_2 = QtWidgets.QWidget(self.page_6)
        self.layoutWidget_2.setGeometry(QtCore.QRect(550, 0, 151, 231))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_4.addWidget(self.label_31)
        self.page6_m_size_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page6_m_size_label.setFont(font)
        self.page6_m_size_label.setObjectName("page6_m_size_label")
        self.verticalLayout_4.addWidget(self.page6_m_size_label)
        self.page6_m_comp_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page6_m_comp_label.setFont(font)
        self.page6_m_comp_label.setObjectName("page6_m_comp_label")
        self.verticalLayout_4.addWidget(self.page6_m_comp_label)
        self.page6_m_weight_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page6_m_weight_label.setFont(font)
        self.page6_m_weight_label.setObjectName("page6_m_weight_label")
        self.verticalLayout_4.addWidget(self.page6_m_weight_label)
        self.page6_m_arch_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page6_m_arch_label.setFont(font)
        self.page6_m_arch_label.setObjectName("page6_m_arch_label")
        self.verticalLayout_4.addWidget(self.page6_m_arch_label)
        self.test_another_button_2 = QtWidgets.QPushButton(self.page_6)
        self.test_another_button_2.setGeometry(QtCore.QRect(560, 310, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.test_another_button_2.setFont(font)
        self.test_another_button_2.setStyleSheet("background-color:rgb(255, 192, 9)\n"
"")
        self.test_another_button_2.setObjectName("test_another_button_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.page_6)
        self.layoutWidget2.setGeometry(QtCore.QRect(360, 0, 151, 231))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_30 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_3.addWidget(self.label_30)
        self.page6_t_size_label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page6_t_size_label.setFont(font)
        self.page6_t_size_label.setObjectName("page6_t_size_label")
        self.verticalLayout_3.addWidget(self.page6_t_size_label)
        self.page6_t_comp_label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page6_t_comp_label.setFont(font)
        self.page6_t_comp_label.setObjectName("page6_t_comp_label")
        self.verticalLayout_3.addWidget(self.page6_t_comp_label)
        self.page6_t_weight_label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page6_t_weight_label.setFont(font)
        self.page6_t_weight_label.setObjectName("page6_t_weight_label")
        self.verticalLayout_3.addWidget(self.page6_t_weight_label)
        self.page6_t_arch_label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page6_t_arch_label.setFont(font)
        self.page6_t_arch_label.setObjectName("page6_t_arch_label")
        self.verticalLayout_3.addWidget(self.page6_t_arch_label)
        self.layoutWidget3 = QtWidgets.QWidget(self.page_6)
        self.layoutWidget3.setGeometry(QtCore.QRect(70, 50, 249, 181))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_5.addWidget(self.label_17)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.label_21 = QtWidgets.QLabel(self.page_6)
        self.label_21.setGeometry(QtCore.QRect(70, 240, 247, 39))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.page6_t_side_label = QtWidgets.QLabel(self.page_6)
        self.page6_t_side_label.setGeometry(QtCore.QRect(360, 237, 149, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page6_t_side_label.setFont(font)
        self.page6_t_side_label.setObjectName("page6_t_side_label")
        self.page6_m_side_label = QtWidgets.QLabel(self.page_6)
        self.page6_m_side_label.setGeometry(QtCore.QRect(550, 237, 149, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page6_m_side_label.setFont(font)
        self.page6_m_side_label.setObjectName("page6_m_side_label")
        self.page6_back_button = QtWidgets.QPushButton(self.page_6)
        self.page6_back_button.setGeometry(QtCore.QRect(380, 310, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.page6_back_button.setFont(font)
        self.page6_back_button.setStyleSheet("background-color:rgb(255, 192, 9)\n"
"")
        self.page6_back_button.setObjectName("page6_back_button")
        self.stackedWidget.addWidget(self.page_6)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_53 = QtWidgets.QLabel(self.page_5)
        self.label_53.setGeometry(QtCore.QRect(30, 10, 350, 320))
        self.label_53.setText("")
        self.label_53.setPixmap(QtGui.QPixmap(":/newPrefix/start_info.PNG"))
        self.label_53.setScaledContents(True)
        self.label_53.setObjectName("label_53")
        self.label_58 = QtWidgets.QLabel(self.page_5)
        self.label_58.setGeometry(QtCore.QRect(50, 260, 129, 44))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.page_5)
        self.label_59.setGeometry(QtCore.QRect(50, 208, 129, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.page_5)
        self.label_60.setGeometry(QtCore.QRect(50, 105, 129, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.page_5)
        self.label_61.setGeometry(QtCore.QRect(50, 157, 129, 44))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.page5_weight_label = QtWidgets.QLabel(self.page_5)
        self.page5_weight_label.setGeometry(QtCore.QRect(148, 159, 171, 44))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.page5_weight_label.setFont(font)
        self.page5_weight_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.page5_weight_label.setObjectName("page5_weight_label")
        self.page5_arch_label = QtWidgets.QLabel(self.page_5)
        self.page5_arch_label.setGeometry(QtCore.QRect(190, 262, 129, 44))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.page5_arch_label.setFont(font)
        self.page5_arch_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.page5_arch_label.setObjectName("page5_arch_label")
        self.page5_size_label = QtWidgets.QLabel(self.page_5)
        self.page5_size_label.setGeometry(QtCore.QRect(190, 107, 129, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.page5_size_label.setFont(font)
        self.page5_size_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.page5_size_label.setObjectName("page5_size_label")
        self.page5_comp_label = QtWidgets.QLabel(self.page_5)
        self.page5_comp_label.setGeometry(QtCore.QRect(190, 210, 129, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.page5_comp_label.setFont(font)
        self.page5_comp_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.page5_comp_label.setObjectName("page5_comp_label")
        self.QC_result_label = QtWidgets.QLabel(self.page_5)
        self.QC_result_label.setGeometry(QtCore.QRect(450, 20, 300, 300))
        self.QC_result_label.setText("")
        self.QC_result_label.setPixmap(QtGui.QPixmap(":/newPrefix/done_tick.svg"))
        self.QC_result_label.setScaledContents(True)
        self.QC_result_label.setObjectName("QC_result_label")
        self.test_another_button = QtWidgets.QPushButton(self.page_5)
        self.test_another_button.setGeometry(QtCore.QRect(450, 340, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.test_another_button.setFont(font)
        self.test_another_button.setStyleSheet("background-color:rgb(255, 192, 9)\n"
"")
        self.test_another_button.setObjectName("test_another_button")
        self.more_details_button = QtWidgets.QPushButton(self.page_5)
        self.more_details_button.setGeometry(QtCore.QRect(60, 340, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.more_details_button.setFont(font)
        self.more_details_button.setStyleSheet("background-color:rgb(255, 192, 9)\n"
"")
        self.more_details_button.setObjectName("more_details_button")
        self.label_62 = QtWidgets.QLabel(self.page_5)
        self.label_62.setGeometry(QtCore.QRect(50, 52, 129, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.page5_side_label = QtWidgets.QLabel(self.page_5)
        self.page5_side_label.setGeometry(QtCore.QRect(190, 52, 129, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.page5_side_label.setFont(font)
        self.page5_side_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.page5_side_label.setObjectName("page5_side_label")
        self.stackedWidget.addWidget(self.page_5)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 471, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/home_bar1.svg"))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 0, 351, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/home_bar2.svg"))
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.wifi_button = QtWidgets.QPushButton(self.centralwidget)
        self.wifi_button.setGeometry(QtCore.QRect(40, 10, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wifi_button.setFont(font)
        self.wifi_button.setAutoFillBackground(False)
        self.wifi_button.setStyleSheet("color: rgb(176, 176, 176);\n"
"background-color:rgb(51, 51, 51);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/home_wifi.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wifi_button.setIcon(icon)
        self.wifi_button.setIconSize(QtCore.QSize(25, 25))
        self.wifi_button.setFlat(True)
        self.wifi_button.setObjectName("wifi_button")
        self.log_button = QtWidgets.QPushButton(self.centralwidget)
        self.log_button.setGeometry(QtCore.QRect(680, 10, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.log_button.setFont(font)
        self.log_button.setAutoFillBackground(False)
        self.log_button.setStyleSheet("color: rgb(176, 176, 176);\n"
"background-color:rgb(51, 51, 51);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/home_dev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.log_button.setIcon(icon1)
        self.log_button.setIconSize(QtCore.QSize(30, 30))
        self.log_button.setFlat(True)
        self.log_button.setObjectName("log_button")
        self.back_to_main_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_to_main_button.setGeometry(QtCore.QRect(140, 10, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.back_to_main_button.setFont(font)
        self.back_to_main_button.setAutoFillBackground(False)
        self.back_to_main_button.setStyleSheet("color: rgb(176, 176, 176);\n"
"background-color:rgb(51, 51, 51);")
        self.back_to_main_button.setIconSize(QtCore.QSize(30, 30))
        self.back_to_main_button.setDefault(True)
        self.back_to_main_button.setFlat(False)
        self.back_to_main_button.setObjectName("back_to_main_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quality Control"))
        self.startQC_button.setText(_translate("MainWindow", "Start Quality Control"))
        self.label_6.setText(_translate("MainWindow", "Scan QR Code"))
        self.startQCprocess_button.setText(_translate("MainWindow", "Start Tests"))
        self.page3_ID_label.setText(_translate("MainWindow", "TextLabel"))
        self.page3_printer_label.setText(_translate("MainWindow", "TextLabel"))
        self.page3_size_label.setText(_translate("MainWindow", "TextLabel"))
        self.page3_side_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "ID"))
        self.label_11.setText(_translate("MainWindow", "Printer"))
        self.label_12.setText(_translate("MainWindow", "Size"))
        self.label_13.setText(_translate("MainWindow", "Sole side"))
        self.label_19.setText(_translate("MainWindow", "QC in Progress"))
        self.label_20.setText(_translate("MainWindow", "Part ID:"))
        self.part_ID_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_22.setText(_translate("MainWindow", "Printer:"))
        self.printer_label.setText(_translate("MainWindow", "TextLabel"))
        self.QC_status_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_48.setText(_translate("MainWindow", "Part ID:"))
        self.page6_ID_label_2.setText(_translate("MainWindow", "TextLabel"))
        self.page6_printer_label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_51.setText(_translate("MainWindow", "Printer:"))
        self.label_31.setText(_translate("MainWindow", "Measured"))
        self.page6_m_size_label.setText(_translate("MainWindow", "TextLabel"))
        self.page6_m_comp_label.setText(_translate("MainWindow", "TextLabel"))
        self.page6_m_weight_label.setText(_translate("MainWindow", "TextLabel"))
        self.page6_m_arch_label.setText(_translate("MainWindow", "TextLabel"))
        self.test_another_button_2.setText(_translate("MainWindow", "Test another sole"))
        self.label_30.setText(_translate("MainWindow", "Target"))
        self.page6_t_size_label.setText(_translate("MainWindow", "TextLabel"))
        self.page6_t_comp_label.setText(_translate("MainWindow", "TextLabel"))
        self.page6_t_weight_label.setText(_translate("MainWindow", "TextLabel"))
        self.page6_t_arch_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "Size (mm)"))
        self.label_17.setText(_translate("MainWindow", "Compression (N/mm^2)"))
        self.label_16.setText(_translate("MainWindow", "Weight (g)"))
        self.label_18.setText(_translate("MainWindow", "Arch (mm)"))
        self.label_21.setText(_translate("MainWindow", "Side"))
        self.page6_t_side_label.setText(_translate("MainWindow", "TextLabel"))
        self.page6_m_side_label.setText(_translate("MainWindow", "TextLabel"))
        self.page6_back_button.setText(_translate("MainWindow", "Back"))
        self.label_58.setText(_translate("MainWindow", "Arch"))
        self.label_59.setText(_translate("MainWindow", "Compression"))
        self.label_60.setText(_translate("MainWindow", "Size"))
        self.label_61.setText(_translate("MainWindow", "Weight"))
        self.page5_weight_label.setText(_translate("MainWindow", "TextLabel"))
        self.page5_arch_label.setText(_translate("MainWindow", "TextLabel"))
        self.page5_size_label.setText(_translate("MainWindow", "TextLabel"))
        self.page5_comp_label.setText(_translate("MainWindow", "TextLabel"))
        self.test_another_button.setText(_translate("MainWindow", "Test another sole"))
        self.more_details_button.setText(_translate("MainWindow", "More details"))
        self.label_62.setText(_translate("MainWindow", "Side"))
        self.page5_side_label.setText(_translate("MainWindow", "TextLabel"))
        self.wifi_button.setText(_translate("MainWindow", "Wifi "))
        self.log_button.setText(_translate("MainWindow", "Log"))
        self.back_to_main_button.setText(_translate("MainWindow", "Back to main"))

import home_icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

