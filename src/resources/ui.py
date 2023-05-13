# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui-app.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(510, 434)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_lab = QtWidgets.QLabel(self.centralwidget)
        self.background_lab.setGeometry(QtCore.QRect(0, 0, 600, 401))
        self.background_lab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.background_lab.setAutoFillBackground(False)
        self.background_lab.setStyleSheet("background-image: url(:/back_newton/nyuton.jpg)")
        self.background_lab.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_lab.setFrameShadow(QtWidgets.QFrame.Plain)
        self.background_lab.setLineWidth(0)
        self.background_lab.setText("")
        self.background_lab.setTextFormat(QtCore.Qt.AutoText)
        self.background_lab.setPixmap(QtGui.QPixmap(":/back_newton/nyuton.jpg"))
        self.background_lab.setScaledContents(True)
        self.background_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.background_lab.setIndent(0)
        self.background_lab.setObjectName("background_lab")
        self.caption_lab = QtWidgets.QLabel(self.centralwidget)
        self.caption_lab.setGeometry(QtCore.QRect(10, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.caption_lab.setFont(font)
        self.caption_lab.setStyleSheet("color: rgb(255, 255, 255)")
        self.caption_lab.setScaledContents(False)
        self.caption_lab.setObjectName("caption_lab")
        self.variant_lab = QtWidgets.QLabel(self.centralwidget)
        self.variant_lab.setGeometry(QtCore.QRect(10, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.variant_lab.setFont(font)
        self.variant_lab.setStyleSheet("color: rgb(255, 255, 255)")
        self.variant_lab.setScaledContents(False)
        self.variant_lab.setObjectName("variant_lab")
        self.completed_lab = QtWidgets.QLabel(self.centralwidget)
        self.completed_lab.setGeometry(QtCore.QRect(10, 70, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.completed_lab.setFont(font)
        self.completed_lab.setStyleSheet("color: rgb(255, 255, 255)")
        self.completed_lab.setScaledContents(False)
        self.completed_lab.setObjectName("completed_lab")
        self.group_lab = QtWidgets.QLabel(self.centralwidget)
        self.group_lab.setGeometry(QtCore.QRect(10, 100, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.group_lab.setFont(font)
        self.group_lab.setStyleSheet("color: rgb(255, 255, 255)")
        self.group_lab.setScaledContents(False)
        self.group_lab.setObjectName("group_lab")
        self.fio_lab = QtWidgets.QLabel(self.centralwidget)
        self.fio_lab.setGeometry(QtCore.QRect(10, 130, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fio_lab.setFont(font)
        self.fio_lab.setStyleSheet("color: rgb(255, 255, 255)")
        self.fio_lab.setScaledContents(False)
        self.fio_lab.setObjectName("fio_lab")
        self.enter_lab = QtWidgets.QLabel(self.centralwidget)
        self.enter_lab.setGeometry(QtCore.QRect(340, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.enter_lab.setFont(font)
        self.enter_lab.setStyleSheet("color: rgb(255, 255, 255)")
        self.enter_lab.setScaledContents(False)
        self.enter_lab.setObjectName("enter_lab")
        self.c_lab = QtWidgets.QLabel(self.centralwidget)
        self.c_lab.setGeometry(QtCore.QRect(370, 60, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.c_lab.setFont(font)
        self.c_lab.setStyleSheet("color: rgb(255, 255, 255)")
        self.c_lab.setScaledContents(False)
        self.c_lab.setObjectName("c_lab")
        self.plus_lab = QtWidgets.QLabel(self.centralwidget)
        self.plus_lab.setGeometry(QtCore.QRect(435, 60, 15, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plus_lab.setFont(font)
        self.plus_lab.setStyleSheet("color: rgb(255, 255, 255)")
        self.plus_lab.setScaledContents(False)
        self.plus_lab.setObjectName("plus_lab")
        self.real_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.real_edit.setGeometry(QtCore.QRect(410, 60, 20, 20))
        self.real_edit.setObjectName("real_edit")
        self.image_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.image_edit.setGeometry(QtCore.QRect(450, 60, 21, 20))
        self.image_edit.setObjectName("image_edit")
        self.i_lab = QtWidgets.QLabel(self.centralwidget)
        self.i_lab.setGeometry(QtCore.QRect(468, 60, 16, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.i_lab.setFont(font)
        self.i_lab.setStyleSheet("color: rgb(255, 255, 255)")
        self.i_lab.setScaledContents(False)
        self.i_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.i_lab.setObjectName("i_lab")
        self.r_lab = QtWidgets.QLabel(self.centralwidget)
        self.r_lab.setGeometry(QtCore.QRect(370, 110, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.r_lab.setFont(font)
        self.r_lab.setStyleSheet("color: rgb(255, 255, 255)")
        self.r_lab.setScaledContents(False)
        self.r_lab.setObjectName("r_lab")
        self.r_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.r_edit.setGeometry(QtCore.QRect(400, 110, 91, 20))
        self.r_edit.setObjectName("r_edit")
        self.buld_fractal_btn = QtWidgets.QPushButton(self.centralwidget)
        self.buld_fractal_btn.setGeometry(QtCore.QRect(-10, 270, 521, 141))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.buld_fractal_btn.setFont(font)
        self.buld_fractal_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-image: url(:/button/space.jpg)")
        self.buld_fractal_btn.setAutoDefault(True)
        self.buld_fractal_btn.setDefault(False)
        self.buld_fractal_btn.setFlat(True)
        self.buld_fractal_btn.setObjectName("buld_fractal_btn")
        self.r_lab_2 = QtWidgets.QLabel(self.centralwidget)
        self.r_lab_2.setGeometry(QtCore.QRect(363, 140, 140, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.r_lab_2.setFont(font)
        self.r_lab_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.r_lab_2.setScaledContents(False)
        self.r_lab_2.setObjectName("r_lab_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(380, 170, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setSingleStep(0.2)
        self.doubleSpinBox.setProperty("value", 1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Бассейны Ньютона"))
        self.caption_lab.setText(_translate("MainWindow", "Бассейны Ньютона - 3"))
        self.variant_lab.setText(_translate("MainWindow", "Вариант №16."))
        self.completed_lab.setText(_translate("MainWindow", "Выполнил: студент"))
        self.group_lab.setText(_translate("MainWindow", "группы ПМИ-22 БО"))
        self.fio_lab.setText(_translate("MainWindow", "Шубин В.С"))
        self.enter_lab.setText(_translate("MainWindow", "Введите параметры:"))
        self.c_lab.setText(_translate("MainWindow", "C = "))
        self.plus_lab.setText(_translate("MainWindow", "+"))
        self.i_lab.setText(_translate("MainWindow", "i"))
        self.r_lab.setText(_translate("MainWindow", "R = "))
        self.buld_fractal_btn.setText(_translate("MainWindow", "Построить фрактал!"))
        self.r_lab_2.setText(_translate("MainWindow", "Масштабирование:"))
import background_rc
