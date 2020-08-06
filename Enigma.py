# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Enigma")
        MainWindow.resize(600, 926)
        font = QtGui.QFont()
        font.setPointSize(7)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_In_Text = ""
        self.Label_Out_Text = ""

        self.Tag3 = QtWidgets.QLabel(self.centralwidget)
        self.Tag3.setGeometry(QtCore.QRect(45, 10, 110, 30))
        self.Tag3.setFont(QtGui.QFont("Arial",16))
        self.Tag3.setAlignment(QtCore.Qt.AlignCenter)
        self.Tag3.setObjectName("Tag3")

        self.Tag2 = QtWidgets.QLabel(self.centralwidget)
        self.Tag2.setGeometry(QtCore.QRect(245, 10, 110, 30))
        self.Tag2.setFont(QtGui.QFont("Arial",16))
        self.Tag2.setAlignment(QtCore.Qt.AlignCenter)
        self.Tag2.setObjectName("Tag2")

        self.Tag1 = QtWidgets.QLabel(self.centralwidget)
        self.Tag1.setGeometry(QtCore.QRect(445, 10, 110, 30))
        self.Tag1.setFont(QtGui.QFont("Arial",16))
        self.Tag1.setAlignment(QtCore.Qt.AlignCenter)
        self.Tag1.setObjectName("Tag1")

        self.TagIn = QtWidgets.QLabel(self.centralwidget)
        self.TagIn.setGeometry(QtCore.QRect(30,490,90,25))
        self.TagIn.setFont(QtGui.QFont("Arial",14))
        self.TagIn.setAlignment(QtCore.Qt.AlignLeft)
        self.TagIn.setObjectName("TagIn")

        self.TagOut = QtWidgets.QLabel(self.centralwidget)
        self.TagOut.setGeometry(QtCore.QRect(30,610,90,25))
        self.TagOut.setFont(QtGui.QFont("Arial", 14))
        self.TagOut.setAlignment(QtCore.Qt.AlignLeft)
        self.TagOut.setObjectName("TagOut")

        self.dial_3 = QtWidgets.QDial(self.centralwidget)
        self.dial_3.setGeometry(QtCore.QRect(45, 40, 110, 110))
        self.dial_3.setMinimum(1)
        self.dial_3.setMaximum(26)
        self.dial_3.setInvertedControls(False)
        self.dial_3.setObjectName("dial_3")
        self.dial_3.valueChanged.connect(self.gear3update)
        self.previous_gear3_value = 0

        self.dial_2 = QtWidgets.QDial(self.centralwidget)
        self.dial_2.setGeometry(QtCore.QRect(245, 40, 110, 110))
        self.dial_2.setMinimum(1)
        self.dial_2.setMaximum(26)
        self.dial_2.setObjectName("dial_2")
        self.dial_2.valueChanged.connect(self.gear2update)
        self.previous_gear2_value = 0

        self.dial_1 = QtWidgets.QDial(self.centralwidget)
        self.dial_1.setGeometry(QtCore.QRect(445, 40, 110, 110))
        self.dial_1.setMinimum(1)
        self.dial_1.setMaximum(26)
        self.dial_1.setObjectName("dial_1")
        self.dial_1.valueChanged.connect(self.gear1update)
        self.previous_gear1_value = 0

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(75, 150, 50, 31))
        self.label_3.setFont(QtGui.QFont("Arial", 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(275, 150, 50, 31))
        self.label_2.setFont(QtGui.QFont("Arial", 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(475, 150, 50, 31))
        self.label_1.setFont(QtGui.QFont("Times", 16))
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")

        self.pushButtonQ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonQ.setGeometry(QtCore.QRect(70, 200, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonQ.setFont(font)
        self.pushButtonQ.setObjectName("pushButtonQ")
        self.pushButtonQ.clicked.connect(self.pressed_Q)

        self.pushButtonW = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonW.setGeometry(QtCore.QRect(120, 200, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonW.setFont(font)
        self.pushButtonW.setObjectName("pushButtonW")
        self.pushButtonW.clicked.connect(self.pressed_W)

        self.pushButtonE = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonE.setGeometry(QtCore.QRect(170, 200, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonE.setFont(font)
        self.pushButtonE.setObjectName("pushButtonE")
        self.pushButtonE.clicked.connect(self.pressed_E)

        self.pushButtonR = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonR.setGeometry(QtCore.QRect(220, 200, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonR.setFont(font)
        self.pushButtonR.setObjectName("pushButtonR")
        self.pushButtonR.clicked.connect(self.pressed_R)

        self.pushButtonT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonT.setGeometry(QtCore.QRect(270, 200, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonT.setFont(font)
        self.pushButtonT.setObjectName("pushButtonT")
        self.pushButtonT.clicked.connect(self.pressed_T)

        self.pushButtonZ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonZ.setGeometry(QtCore.QRect(320, 200, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonZ.setFont(font)
        self.pushButtonZ.setObjectName("pushButtonZ")
        self.pushButtonZ.clicked.connect(self.pressed_Z)

        self.pushButtonU = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonU.setGeometry(QtCore.QRect(370, 200, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonU.setFont(font)
        self.pushButtonU.setObjectName("pushButtonU")
        self.pushButtonU.clicked.connect(self.pressed_U)

        self.pushButtonI = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonI.setGeometry(QtCore.QRect(420, 200, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonI.setFont(font)
        self.pushButtonI.setObjectName("pushButtonI")
        self.pushButtonI.clicked.connect(self.pressed_I)

        self.pushButtonO = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonO.setGeometry(QtCore.QRect(470, 200, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonO.setFont(font)
        self.pushButtonO.setObjectName("pushButtonO")
        self.pushButtonO.clicked.connect(self.pressed_O)

        self.pushButtonK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonK.setGeometry(QtCore.QRect(440, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonK.setFont(font)
        self.pushButtonK.setObjectName("pushButtonK")
        self.pushButtonK.clicked.connect(self.pressed_K)

        self.pushButtonH = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonH.setGeometry(QtCore.QRect(340, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonH.setFont(font)
        self.pushButtonH.setObjectName("pushButtonH")
        self.pushButtonH.clicked.connect(self.pressed_H)

        self.pushButtonA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonA.setGeometry(QtCore.QRect(90, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonA.setFont(font)
        self.pushButtonA.setObjectName("pushButtonA")
        self.pushButtonA.clicked.connect(self.pressed_A)

        self.pushButtonF = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonF.setGeometry(QtCore.QRect(240, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonF.setFont(font)
        self.pushButtonF.setObjectName("pushButtonF")
        self.pushButtonF.clicked.connect(self.pressed_F)

        self.pushButtonJ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonJ.setGeometry(QtCore.QRect(390, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonJ.setFont(font)
        self.pushButtonJ.setObjectName("pushButtonJ")
        self.pushButtonJ.clicked.connect(self.pressed_J)

        self.pushButtonG = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonG.setGeometry(QtCore.QRect(290, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonG.setFont(font)
        self.pushButtonG.setObjectName("pushButtonG")
        self.pushButtonG.clicked.connect(self.pressed_G)

        self.pushButtonD = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonD.setGeometry(QtCore.QRect(190, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonD.setFont(font)
        self.pushButtonD.setObjectName("pushButtonD")
        self.pushButtonD.clicked.connect(self.pressed_D)

        self.pushButtonS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonS.setGeometry(QtCore.QRect(140, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonS.setFont(font)
        self.pushButtonS.setObjectName("pushButtonS")
        self.pushButtonS.clicked.connect(self.pressed_S)

        self.pushButtonL = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonL.setGeometry(QtCore.QRect(470, 300, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonL.setFont(font)
        self.pushButtonL.setObjectName("pushButtonL")
        self.pushButtonL.clicked.connect(self.pressed_L)

        self.pushButtonM = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonM.setGeometry(QtCore.QRect(420, 300, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonM.setFont(font)
        self.pushButtonM.setObjectName("pushButtonM")
        self.pushButtonM.clicked.connect(self.pressed_M)

        self.pushButtonB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonB.setGeometry(QtCore.QRect(320, 300, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonB.setFont(font)
        self.pushButtonB.setObjectName("pushButtonB")
        self.pushButtonB.clicked.connect(self.pressed_B)

        self.pushButtonP = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonP.setGeometry(QtCore.QRect(70, 300, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonP.setFont(font)
        self.pushButtonP.setObjectName("pushButtonP")
        self.pushButtonP.clicked.connect(self.pressed_P)

        self.pushButtonC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonC.setGeometry(QtCore.QRect(220, 300, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonC.setFont(font)
        self.pushButtonC.setObjectName("pushButtonC")
        self.pushButtonC.clicked.connect(self.pressed_C)

        self.pushButtonN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonN.setGeometry(QtCore.QRect(370, 300, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonN.setFont(font)
        self.pushButtonN.setObjectName("pushButtonN")
        self.pushButtonN.clicked.connect(self.pressed_N)

        self.pushButtonV = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonV.setGeometry(QtCore.QRect(270, 300, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonV.setFont(font)
        self.pushButtonV.setObjectName("pushButtonV")
        self.pushButtonV.clicked.connect(self.pressed_V)

        self.pushButtonX = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonX.setGeometry(QtCore.QRect(170, 300, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonX.setFont(font)
        self.pushButtonX.setObjectName("pushButtonX")
        self.pushButtonX.clicked.connect(self.pressed_X)

        self.pushButtonY = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonY.setGeometry(QtCore.QRect(120, 300, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonY.setFont(font)
        self.pushButtonY.setObjectName("pushButtonY")
        self.pushButtonY.clicked.connect(self.pressed_Y)

        self.Combo_1_1 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_1_1.setGeometry(QtCore.QRect(70, 410, 41, 22))
        self.Combo_1_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_1_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_1_2.setGeometry(QtCore.QRect(110, 410, 41, 22))
        self.Combo_1_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_2_1 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_2_1.setGeometry(QtCore.QRect(160, 410, 41, 22))
        self.Combo_2_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_2_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_2_2.setGeometry(QtCore.QRect(200, 410, 41, 22))
        self.Combo_2_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_3_1 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_3_1.setGeometry(QtCore.QRect(250, 410, 41, 22))
        self.Combo_3_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_3_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_3_2.setGeometry(QtCore.QRect(290, 410, 41, 22))
        self.Combo_3_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_4_1 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_4_1.setGeometry(QtCore.QRect(340, 410, 41, 22))
        self.Combo_4_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_4_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_4_2.setGeometry(QtCore.QRect(380, 410, 41, 22))
        self.Combo_4_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_5_1 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_5_1.setGeometry(QtCore.QRect(430, 410, 41, 22))
        self.Combo_5_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_5_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_5_2.setGeometry(QtCore.QRect(470, 410, 41, 22))
        self.Combo_5_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_6_1 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_6_1.setGeometry(QtCore.QRect(70, 460, 41, 22))
        self.Combo_6_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_6_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_6_2.setGeometry(QtCore.QRect(110, 460, 41, 22))
        self.Combo_6_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_7_1 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_7_1.setGeometry(QtCore.QRect(160, 460, 41, 22))
        self.Combo_7_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_7_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_7_2.setGeometry(QtCore.QRect(200, 460, 41, 22))
        self.Combo_7_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_8_1 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_8_1.setGeometry(QtCore.QRect(250, 460, 41, 22))
        self.Combo_8_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_8_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_8_2.setGeometry(QtCore.QRect(290, 460, 41, 22))
        self.Combo_8_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_9_1 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_9_1.setGeometry(QtCore.QRect(340, 460, 41, 22))
        self.Combo_9_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_9_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_9_2.setGeometry(QtCore.QRect(380, 460, 41, 22))
        self.Combo_9_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_10_1 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_10_1.setGeometry(QtCore.QRect(430, 460, 41, 22))
        self.Combo_10_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.Combo_10_2 = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_10_2.setGeometry(QtCore.QRect(470, 460, 41, 22))
        self.Combo_10_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])

        self.PanelTag = QtWidgets.QLabel(self.centralwidget)
        self.PanelTag.setGeometry(QtCore.QRect(70,360,121,31))
        self.PanelTag.setFont(QtGui.QFont("Arial", 16))
        self.PanelTag.setAlignment(QtCore.Qt.AlignTop)
        self.PanelTag.setObjectName("PatchPanel")

        self.Connection1 = QtWidgets.QLabel(self.centralwidget)
        self.Connection1.setGeometry(QtCore.QRect(70,390,81,16))
        self.Connection1.setFont(QtGui.QFont("Arial", 9))
        self.Connection1.setAlignment(QtCore.Qt.AlignTop)
        self.Connection1.setObjectName("Connection1")

        self.Connection2 = QtWidgets.QLabel(self.centralwidget)
        self.Connection2.setGeometry(QtCore.QRect(160,390,81,16))
        self.Connection2.setFont(QtGui.QFont("Arial", 9))
        self.Connection2.setAlignment(QtCore.Qt.AlignTop)
        self.Connection2.setObjectName("Connection2")

        self.Connection3 = QtWidgets.QLabel(self.centralwidget)
        self.Connection3.setGeometry(QtCore.QRect(250,390,81,16))
        self.Connection3.setFont(QtGui.QFont("Arial", 9))
        self.Connection3.setAlignment(QtCore.Qt.AlignTop)
        self.Connection3.setObjectName("Connection3")

        self.Connection4 = QtWidgets.QLabel(self.centralwidget)
        self.Connection4.setGeometry(QtCore.QRect(340,390,81,16))
        self.Connection4.setFont(QtGui.QFont("Arial", 9))
        self.Connection4.setAlignment(QtCore.Qt.AlignTop)
        self.Connection4.setObjectName("Connection4")

        self.Connection5 = QtWidgets.QLabel(self.centralwidget)
        self.Connection5.setGeometry(QtCore.QRect(430,390,81,16))
        self.Connection5.setFont(QtGui.QFont("Arial", 9))
        self.Connection5.setAlignment(QtCore.Qt.AlignTop)
        self.Connection5.setObjectName("Connection5")

        self.Connection6 = QtWidgets.QLabel(self.centralwidget)
        self.Connection6.setGeometry(QtCore.QRect(70,440,81,16))
        self.Connection6.setFont(QtGui.QFont("Arial", 9))
        self.Connection6.setAlignment(QtCore.Qt.AlignTop)
        self.Connection6.setObjectName("Connection6")

        self.Connection7 = QtWidgets.QLabel(self.centralwidget)
        self.Connection7.setGeometry(QtCore.QRect(160,440,81,16))
        self.Connection7.setFont(QtGui.QFont("Arial", 9))
        self.Connection7.setAlignment(QtCore.Qt.AlignTop)
        self.Connection7.setObjectName("Connection7")

        self.Connection8 = QtWidgets.QLabel(self.centralwidget)
        self.Connection8.setGeometry(QtCore.QRect(250,440,81,16))
        self.Connection8.setFont(QtGui.QFont("Arial", 9))
        self.Connection8.setAlignment(QtCore.Qt.AlignTop)
        self.Connection8.setObjectName("Connection8")

        self.Connection9 = QtWidgets.QLabel(self.centralwidget)
        self.Connection9.setGeometry(QtCore.QRect(340,440,81,16))
        self.Connection9.setFont(QtGui.QFont("Arial", 9))
        self.Connection9.setAlignment(QtCore.Qt.AlignTop)
        self.Connection9.setObjectName("Connection9")

        self.Connection10 = QtWidgets.QLabel(self.centralwidget)
        self.Connection10.setGeometry(QtCore.QRect(430,440,81,16))
        self.Connection10.setFont(QtGui.QFont("Arial", 9))
        self.Connection10.setAlignment(QtCore.Qt.AlignTop)
        self.Connection10.setObjectName("Connection10")


        self.TextIn = QtWidgets.QLabel(self.centralwidget)
        self.TextIn.setGeometry(QtCore.QRect(30,520, 561, 81))
        self.TextIn.setFont(QtGui.QFont("Arial", 20))
        self.TextIn.setAlignment(QtCore.Qt.AlignTop)
        self.TextIn.setObjectName("TextIn")

        self.TextOut = QtWidgets.QLabel(self.centralwidget)
        self.TextOut.setGeometry(QtCore.QRect(30,640, 561, 81))
        self.TextOut.setFont(QtGui.QFont("Arial", 20))
        self.TextOut.setAlignment(QtCore.Qt.AlignTop)
        self.TextOut.setObjectName("TextOut")

        self.AutomaticTag = QtWidgets.QLabel(self.centralwidget)
        self.AutomaticTag.setGeometry(QtCore.QRect(30, 730,90,25))
        self.AutomaticTag.setFont(QtGui.QFont("Arial", 14))
        self.AutomaticTag.setAlignment(QtCore.Qt.AlignTop)
        self.AutomaticTag.setObjectName("AutoTag")

        self.Auto_In = QtWidgets.QTextEdit(self.centralwidget)
        self.Auto_In.setGeometry(QtCore.QRect(30,760,261,41))
        self.Auto_In.setFont(QtGui.QFont("Arial", 16))
        self.Auto_In.setAlignment(QtCore.Qt.AlignTop)
        self.Auto_In.setObjectName("AutoIn")

        self.Auto_Out = QtWidgets.QLabel(self.centralwidget)
        self.Auto_Out.setGeometry(QtCore.QRect(300,760,261,41))
        self.Auto_Out.setFont(QtGui.QFont("Arial", 16))
        self.Auto_Out.setAlignment(QtCore.Qt.AlignTop)
        self.Auto_Out.setStyleSheet("border: 1px solid gray;")
        self.Auto_Out.setObjectName("AutoOut")

        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(451,850,111,31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reset_button.setFont(font)
        self.reset_button.setObjectName("resetButton")
        self.reset_button.clicked.connect(self.reset)

        self.auto_button = QtWidgets.QPushButton(self.centralwidget)
        self.auto_button.setGeometry(QtCore.QRect(451,803,111,31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.auto_button.setFont(font)
        self.auto_button.setObjectName("autoButton")
        self.auto_button.clicked.connect(self.automatic)

        self.gear1 = [["A", "W"], ["B", "D"], ["C", "I"], ["D", "T"], ["E", "M"], ["F", "S"],
                      ["G", "H"], ["H", "A"], ["I", "G"], ["J", "Y"], ["K", "N"], ["L", "Q"],
                      ["M", "C"], ["N", "U"], ["O", "X"], ["P", "F"], ["Q", "J"], ["R", "L"],
                      ["S", "O"], ["T", "R"], ["U", "B"], ["V", "Z"], ["W", "V"], ["X", "P"],
                      ["Y", "E"], ["Z", "K"]]
        self.gear1_original = [["A", "W"], ["B", "D"], ["C", "I"], ["D", "T"], ["E", "M"], ["F", "S"],
                      ["G", "H"], ["H", "A"], ["I", "G"], ["J", "Y"], ["K", "N"], ["L", "Q"],
                      ["M", "C"], ["N", "U"], ["O", "X"], ["P", "F"], ["Q", "J"], ["R", "L"],
                      ["S", "O"], ["T", "R"], ["U", "B"], ["V", "Z"], ["W", "V"], ["X", "P"],
                      ["Y", "E"], ["Z", "K"]]
        self.gear2 = [["A", "F"], ["B", "L"], ["C", "Q"], ["D", "G"], ["E", "T"], ["F", "K"],
                      ["G", "Y"], ["H", "P"], ["I", "E"], ["J", "D"], ["K", "X"], ["L", "S"],
                      ["M", "C"], ["N", "O"], ["O", "W"], ["P", "J"], ["R", "V"], ["Q", "R"],
                      ["S", "B"], ["T", "N"], ["U", "H"], ["V", "Z"], ["W", "A"], ["X", "M"],
                      ["Y", "U"], ["Z", "I"]]
        self.gear2_original = [["A", "F"], ["B", "L"], ["C", "Q"], ["D", "G"], ["E", "T"], ["F", "K"],
                      ["G", "Y"], ["H", "P"], ["I", "E"], ["J", "D"], ["K", "X"], ["L", "S"],
                      ["M", "C"], ["N", "O"], ["O", "W"], ["P", "J"], ["R", "V"], ["Q", "R"],
                      ["S", "B"], ["T", "N"], ["U", "H"], ["V", "Z"], ["W", "A"], ["X", "M"],
                      ["Y", "U"], ["Z", "I"]]
        self.gear3 = [["A", "T"], ["B", "L"], ["C", "H"], ["D", "Z"], ["E", "A"], ["F", "M"],
                      ["G", "S"], ["H", "K"], ["I", "X"], ["J", "D"], ["K", "W"], ["L", "G"],
                      ["M", "P"], ["N", "R"], ["O", "C"], ["P", "N"], ["Q", "V"], ["R", "B"],
                      ["S", "Q"], ["T", "U"], ["U", "I"], ["V", "O"], ["W", "F"], ["X", "E"],
                      ["Y", "J"], ["Z", "Y"]]
        self.gear3_original = [["A", "T"], ["B", "L"], ["C", "H"], ["D", "Z"], ["E", "A"], ["F", "M"],
                      ["G", "S"], ["H", "K"], ["I", "X"], ["J", "D"], ["K", "W"], ["L", "G"],
                      ["M", "P"], ["N", "R"], ["O", "C"], ["P", "N"], ["Q", "V"], ["R", "B"],
                      ["S", "Q"], ["T", "U"], ["U", "I"], ["V", "O"], ["W", "F"], ["X", "E"],
                      ["Y", "J"], ["Z", "Y"]]
        self.reflection_panel = [["A", "S"], ["B", "N"], ["C", "V"], ["D", "X"], ["E", "T"],
                                 ["F", "R"], ["G", "O"], ["H", "W"], ["I", "P"], ["J", "Z"],
                                 ["K", "Y"], ["L", "U"], ["M", "Q"], ["S", "A"], ["N", "B"],
                                 ["V", "C"], ["X", "D"], ["T", "E"], ["R", "F"], ["O", "G"],
                                 ["W", "H"], ["P", "I"], ["Z", "J"], ["Y", "K"], ["U", "L"],
                                 ["Q", "M"]]
        self.patch_panel = [[" "," "]]

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enigma"))
        self.label_3.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "1"))
        self.label_1.setText(_translate("MainWindow", "1"))
        self.Tag3.setText(_translate("MainWindow", "Gear 3"))
        self.Tag2.setText(_translate("MainWindow", "Gear 2"))
        self.Tag1.setText(_translate("MainWindow", "Gear 1"))
        self.TagIn.setText(_translate("MainWindow", "Text In"))
        self.TagOut.setText(_translate("MainWindow", "Text Out"))
        self.pushButtonQ.setText(_translate("MainWindow", "Q"))
        self.pushButtonW.setText(_translate("MainWindow", "W"))
        self.pushButtonE.setText(_translate("MainWindow", "E"))
        self.pushButtonR.setText(_translate("MainWindow", "R"))
        self.pushButtonT.setText(_translate("MainWindow", "T"))
        self.pushButtonZ.setText(_translate("MainWindow", "Z"))
        self.pushButtonU.setText(_translate("MainWindow", "U"))
        self.pushButtonI.setText(_translate("MainWindow", "I"))
        self.pushButtonO.setText(_translate("MainWindow", "O"))
        self.pushButtonK.setText(_translate("MainWindow", "K"))
        self.pushButtonH.setText(_translate("MainWindow", "H"))
        self.pushButtonA.setText(_translate("MainWindow", "A"))
        self.pushButtonF.setText(_translate("MainWindow", "F"))
        self.pushButtonJ.setText(_translate("MainWindow", "J"))
        self.pushButtonG.setText(_translate("MainWindow", "G"))
        self.pushButtonD.setText(_translate("MainWindow", "D"))
        self.pushButtonS.setText(_translate("MainWindow", "S"))
        self.pushButtonL.setText(_translate("MainWindow", "L"))
        self.pushButtonM.setText(_translate("MainWindow", "M"))
        self.pushButtonB.setText(_translate("MainWindow", "B"))
        self.pushButtonP.setText(_translate("MainWindow", "P"))
        self.pushButtonC.setText(_translate("MainWindow", "C"))
        self.pushButtonN.setText(_translate("MainWindow", "N"))
        self.pushButtonV.setText(_translate("MainWindow", "V"))
        self.pushButtonX.setText(_translate("MainWindow", "X"))
        self.pushButtonY.setText(_translate("MainWindow", "Y"))
        self.PanelTag.setText(_translate("MainWindow", "Patch Panel"))
        self.Connection1.setText(_translate("MainWindow", "Connection 1"))
        self.Connection2.setText(_translate("MainWindow", "Connection 2"))
        self.Connection3.setText(_translate("MainWindow", "Connection 3"))
        self.Connection4.setText(_translate("MainWindow", "Connection 4"))
        self.Connection5.setText(_translate("MainWindow", "Connection 5"))
        self.Connection6.setText(_translate("MainWindow", "Connection 6"))
        self.Connection7.setText(_translate("MainWindow", "Connection 7"))
        self.Connection8.setText(_translate("MainWindow", "Connection 8"))
        self.Connection9.setText(_translate("MainWindow", "Connection 9"))
        self.Connection10.setText(_translate("MainWindow", "Connection 10"))
        self.reset_button.setText(_translate("MainWindow", "Reset Program"))
        self.auto_button.setText(_translate("MainWindow", "Run"))
        self.AutomaticTag.setText(_translate("MainWindow","Automatic"))

    def gear3update(self):
        if self.previous_gear3_value == 26 and self.dial_3.value() == 1:
            self.rotate_gear3_forward()
        elif (self.previous_gear3_value == 1 or self.previous_gear3_value == 0) and self.dial_3.value() == 26:
            self.gear3 = self.rotate_gear3_backward(self.gear3)
        elif self.previous_gear3_value < self.dial_3.value():
            self.rotate_gear3_forward()
        else:
            self.gear3 = self.rotate_gear3_backward(self.gear3)

        self.gear3setting = str(self.dial_3.value())
        temp = self.dial_3.value()
        self.label_3.setText(self.gear3setting)

        self.previous_gear3_value = temp


    def gear2update(self):
        if self.previous_gear2_value == 26 and self.dial_2.value() == 1:
            self.rotate_gear2_forward()
        elif (self.previous_gear2_value == 1 or self.previous_gear2_value == 0) and self.dial_2.value() == 26:
            self.gear2 = self.rotate_gear2_backward(self.gear2)
        elif self.previous_gear2_value < self.dial_2.value():
            self.rotate_gear2_forward()
        else:
            self.gear2 = self.rotate_gear2_backward(self.gear2)

        self.gear2setting = str(self.dial_2.value())
        temp = self.dial_2.value()
        self.label_2.setText(self.gear2setting)

        self.previous_gear2_value = temp


    def gear1update(self):
        if self.previous_gear1_value == 26 and self.dial_1.value() == 1:
            self.rotate_gear1_forward()
        elif (self.previous_gear1_value == 1 or self.previous_gear1_value == 0) and self.dial_1.value() == 26:
            self.gear1 = self.rotate_gear1_backward(self.gear1)
        elif self.previous_gear1_value < self.dial_1.value():
            self.rotate_gear1_forward()
        else:
            self.gear1 = self.rotate_gear1_backward(self.gear1)

        self.gear1setting = str(self.dial_1.value())
        temp = self.dial_1.value()
        self.label_1.setText(self.gear1setting)

        self.previous_gear1_value = temp




    def pressed_A(self):
        self.insert_Letter("A")
    def pressed_B(self):
        self.insert_Letter("B")
    def pressed_C(self):
        self.insert_Letter("C")
    def pressed_D(self):
        self.insert_Letter("D")
    def pressed_E(self):
        self.insert_Letter("E")
    def pressed_F(self):
        self.insert_Letter("F")
    def pressed_G(self):
        self.insert_Letter("G")
    def pressed_H(self):
        self.insert_Letter("H")
    def pressed_I(self):
        self.insert_Letter("I")
    def pressed_J(self):
        self.insert_Letter("J")
    def pressed_K(self):
        self.insert_Letter("K")
    def pressed_L(self):
        self.insert_Letter("L")
    def pressed_M(self):
        self.insert_Letter("M")
    def pressed_N(self):
        self.insert_Letter("N")
    def pressed_O(self):
        self.insert_Letter("O")
    def pressed_P(self):
        self.insert_Letter("P")
    def pressed_Q(self):
        self.insert_Letter("Q")
    def pressed_R(self):
        self.insert_Letter("R")
    def pressed_S(self):
        self.insert_Letter("S")
    def pressed_T(self):
        self.insert_Letter("T")
    def pressed_U(self):
        self.insert_Letter("U")
    def pressed_V(self):
        self.insert_Letter("V")
    def pressed_W(self):
        self.insert_Letter("W")
    def pressed_X(self):
        self.insert_Letter("X")
    def pressed_Y(self):
        self.insert_Letter("Y")
    def pressed_Z(self):
        self.insert_Letter("Z")

    def insert_Letter(self,letter_in):
        self.patch_panel_setup()

        temp = letter_in
        self.Label_In_Text = self.Label_In_Text + temp
        self.TextIn.setText(self.Label_In_Text)

        num1 = self.letter_to_num(temp)
        num2 = self.insert_patch_panel_to(num1)
        num3 = self.insert_gear_to(num2,self.gear1)
        num4 = self.insert_gear_to(num3, self.gear2)
        num5 = self.insert_gear_to(num4, self.gear3)
        num6 = self.insert_reflection(num5,self.reflection_panel)
        num7 = self.insert_gear_from(num6,self.gear3)
        num8 = self.insert_gear_from(num7, self.gear2)
        num9 = self.insert_gear_from(num8, self.gear1)
        num10 = self.insert_patch_panel_from(num9)
        let1 = self.num_to_letter(num10)



        self.Label_Out_Text = self.Label_Out_Text + let1
        self.TextOut.setText(self.Label_Out_Text)
        self.rotate_gears()

        self.patch_panel = [[" "," "]]

    def insert_patch_panel_to(self,num):
        let1 = self.num_to_letter(num)
        pos = 0
        for x in range(0,len(self.patch_panel)):
            if self.patch_panel[x][0] == let1:
                temp = self.patch_panel[x][1]
                pos = self.letter_to_num(temp)
        if pos == 0:
            return num
        return pos

    def insert_patch_panel_from(self,num):
        let1 = self.num_to_letter(num)
        pos = -1
        for x in range(0, len(self.patch_panel)):
            if self.patch_panel[x][1] == let1:
                temp = self.patch_panel[x][0 ]
                pos = self.letter_to_num(temp)
        if pos == -1:
            return num
        return pos

    def insert_gear_to(self,num,gear):
        let1 = gear[num][0]
        pos = -1
        for x in range(0,len(gear)):
            if gear[x][1] == let1:
                pos = x
        return pos

    def insert_gear_from(self,num,gear):
        let1 = gear[num][1]
        pos = -1
        for x in range(0, len(gear)):
            if gear[x][0] == let1:
                pos = x

        return pos

    def insert_reflection(self,num,panel):
        let1 = panel[num][0]
        pos = -1
        for x in range(0,len(panel)):
            if panel[x][1] == let1:
                pos = x
        return pos

    def rotate_gears(self):
        num1 = self.dial_1.value()
        num2 = self.dial_2.value()
        num3 = self.dial_3.value()
        if num1 != 26:
            num1+=1
        elif num1==26 and num2!=26 and num3!=26:
            num1=1
            num2+=1
        elif num1 == 26 and num2 == 26 and num3 != 26:
            num1=1
            num2=1
            num3+=1
        elif num1 == 26 and num2 == 26 and num3 == 26:
            num1=1
            num2=1
            num3=1

        self.dial_1.setValue(num1)
        self.dial_2.setValue(num2)
        self.dial_3.setValue(num3)

    def rotate_gear1_forward(self):
        temp = self.gear1[0]
        for x in range(0,25):
            self.gear1[x] = self.gear1[x+1]
        self.gear1[25] = temp

    def rotate_gear2_forward(self):
        temp = self.gear2[0]
        for x in range(0,25):
            self.gear2[x] = self.gear2[x+1]
        self.gear2[25] = temp

    def rotate_gear3_forward(self):
        temp = self.gear3[0]
        for x in range(0,25):
            self.gear3[x] = self.gear3[x+1]
        self.gear3[25] = temp

    def rotate_gear1_backward(self,temp_arr):
        temp = temp_arr.copy()

        for x in range(len(temp)):
            temp[x] = ""
        temp2 = temp_arr[len(temp_arr) - 1]

        for x in range(1, len(temp)):
            temp[x] = temp_arr[x - 1]

        temp[0] = temp2
        temp_arr = temp
        return temp_arr

    def rotate_gear2_backward(self,temp_arr):
        temp = temp_arr.copy()

        for x in range(len(temp)):
            temp[x] = ""
        temp2 = temp_arr[len(temp_arr) - 1]

        for x in range(1, len(temp)):
            temp[x] = temp_arr[x - 1]

        temp[0] = temp2
        temp_arr = temp
        return temp_arr

    def rotate_gear3_backward(self,temp_arr):
        temp = temp_arr.copy()

        for x in range(len(temp)):
            temp[x] = ""
        temp2 = temp_arr[len(temp_arr) - 1]

        for x in range(1, len(temp)):
            temp[x] = temp_arr[x - 1]

        temp[0] = temp2
        temp_arr = temp
        return temp_arr



    def patch_panel_setup(self):
        if self.Combo_1_1.currentText() != " " and self.Combo_1_2.currentText() != " ":
            self.patch_panel.append([self.Combo_1_1.currentText(),self.Combo_1_2.currentText()])
        if self.Combo_2_1.currentText() != " " and self.Combo_2_2.currentText() != " ":
            self.patch_panel.append([self.Combo_2_1.currentText(),self.Combo_2_2.currentText()])
        if self.Combo_3_1.currentText() != " " and self.Combo_3_2.currentText() != " ":
            self.patch_panel.append([self.Combo_3_1.currentText(),self.Combo_3_2.currentText()])
        if self.Combo_4_1.currentText() != " " and self.Combo_4_2.currentText() != " ":
            self.patch_panel.append([self.Combo_4_1.currentText(),self.Combo_4_2.currentText()])
        if self.Combo_5_1.currentText() != " " and self.Combo_5_2.currentText() != " ":
            self.patch_panel.append([self.Combo_5_1.currentText(),self.Combo_5_2.currentText()])
        if self.Combo_6_1.currentText() != " " and self.Combo_6_2.currentText() != " ":
            self.patch_panel.append([self.Combo_6_1.currentText(),self.Combo_6_2.currentText()])
        if self.Combo_7_1.currentText() != " " and self.Combo_7_2.currentText() != " ":
            self.patch_panel.append([self.Combo_7_1.currentText(),self.Combo_7_2.currentText()])
        if self.Combo_8_1.currentText() != " " and self.Combo_8_2.currentText() != " ":
            self.patch_panel.append([self.Combo_8_1.currentText(), self.Combo_8_2.currentText()])
        if self.Combo_9_1.currentText() != " " and self.Combo_9_2.currentText() != " ":
            self.patch_panel.append([self.Combo_9_1.currentText(), self.Combo_9_2.currentText()])
        if self.Combo_10_1.currentText() != " " and self.Combo_10_2.currentText() != " ":
            self.patch_panel.append([self.Combo_10_1.currentText(), self.Combo_10_2.currentText()])

    def reset(self):
        self.dial_3.setValue(1)
        self.dial_2.setValue(1)
        self.dial_1.setValue(1)
        self.gear3 = self.gear3_original
        self.gear2 = self.gear2_original
        self.gear1 = self.gear1_original
        self.Combo_1_1.clear()
        self.Combo_1_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_1_2.clear()
        self.Combo_1_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_2_1.clear()
        self.Combo_2_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_2_2.clear()
        self.Combo_2_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_3_1.clear()
        self.Combo_3_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_3_2.clear()
        self.Combo_3_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_4_1.clear()
        self.Combo_4_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_4_2.clear()
        self.Combo_4_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_5_1.clear()
        self.Combo_5_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_5_2.clear()
        self.Combo_5_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_6_1.clear()
        self.Combo_6_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_6_2.clear()
        self.Combo_6_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_7_1.clear()
        self.Combo_7_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_7_2.clear()
        self.Combo_7_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_8_1.clear()
        self.Combo_8_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_8_2.clear()
        self.Combo_8_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_9_1.clear()
        self.Combo_9_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_9_2.clear()
        self.Combo_9_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_10_1.clear()
        self.Combo_10_1.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Combo_10_2.clear()
        self.Combo_10_2.addItems(
            [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"])
        self.Label_Out_Text = ""
        self.Label_In_Text = ""
        self.TextIn.setText(self.Label_In_Text)
        self.TextOut.setText(self.Label_Out_Text)
        self.Auto_Out.clear()
        self.Auto_In.clear()


    def automatic(self):
        self.Auto_Out.clear()
        temp = self.Auto_In.toPlainText().upper()
        out_text = ""
        for x in temp:
            self.patch_panel_setup()
            num1 = self.letter_to_num(x)
            num2 = self.insert_patch_panel_to(num1)
            num3 = self.insert_gear_to(num2, self.gear1)
            num4 = self.insert_gear_to(num3, self.gear2)
            num5 = self.insert_gear_to(num4, self.gear3)
            num6 = self.insert_reflection(num5, self.reflection_panel)
            num7 = self.insert_gear_from(num6, self.gear3)
            num8 = self.insert_gear_from(num7, self.gear2)
            num9 = self.insert_gear_from(num8, self.gear1)
            num10 = self.insert_patch_panel_from(num9)
            let1 = self.num_to_letter(num10)
            out_text = out_text + let1
            self.rotate_gears()
            self.patch_panel = [[" ", " "]]

        self.Auto_Out.setText(str(out_text))

        out_text = ""

    def letter_to_num(self, letter):
        if letter=="A":
            return 0
        elif letter=="B":
            return 1
        elif letter=="C":
            return 2
        elif letter=="D":
            return 3
        elif letter=="E":
            return 4
        elif letter=="F":
            return 5
        elif letter=="G":
            return 6
        elif letter=="H":
            return 7
        elif letter=="I":
            return 8
        elif letter=="J":
            return 9
        elif letter=="K":
            return 10
        elif letter=="L":
            return 11
        elif letter=="M":
            return 12
        elif letter=="N":
            return 13
        elif letter=="O":
            return 14
        elif letter=="P":
            return 15
        elif letter=="Q":
            return 16
        elif letter=="R":
            return 17
        elif letter=="S":
            return 18
        elif letter=="T":
            return 19
        elif letter=="U":
            return 20
        elif letter=="V":
            return 21
        elif letter=="W":
            return 22
        elif letter=="X":
            return 23
        elif letter=="Y":
            return 24
        elif letter=="Z":
            return 25

    def num_to_letter(self, num):
        if num==0:
            return "A"
        elif num == 1:
            return "B"
        elif num == 2:
            return "C"
        elif num == 3:
            return "D"
        elif num == 4:
            return "E"
        elif num == 5:
            return "F"
        elif num == 6:
            return "G"
        elif num == 7:
            return "H"
        elif num == 8:
            return "I"
        elif num == 9:
            return "J"
        elif num == 10:
            return "K"
        elif num == 11:
            return "L"
        elif num == 12:
            return "M"
        elif num == 13:
            return "N"
        elif num == 14:
            return "O"
        elif num == 15:
            return "P"
        elif num == 16:
            return "Q"
        elif num == 17:
            return "R"
        elif num == 18:
            return "S"
        elif num == 19:
            return "T"
        elif num == 20:
            return "U"
        elif num == 21:
            return "V"
        elif num == 22:
            return "W"
        elif num == 23:
            return "X"
        elif num == 24:
            return "Y"
        elif num == 25:
            return "Z"


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
