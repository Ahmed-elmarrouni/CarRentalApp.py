# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'location.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LOCATION_DE_VOITURE(object):
    def setupUi(self, LOCATION_DE_VOITURE):
        LOCATION_DE_VOITURE.setObjectName("LOCATION_DE_VOITURE")
        LOCATION_DE_VOITURE.resize(918, 799)
        LOCATION_DE_VOITURE.setStyleSheet("background-color: rgb(242, 244, 255);")
        self.centralwidget = QtWidgets.QWidget(LOCATION_DE_VOITURE)
        self.centralwidget.setObjectName("centralwidget")
        self.VOITURE_MODEL_input = QtWidgets.QLineEdit(self.centralwidget)
        self.VOITURE_MODEL_input.setGeometry(QtCore.QRect(640, 190, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VOITURE_MODEL_input.setFont(font)
        self.VOITURE_MODEL_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.VOITURE_MODEL_input.setObjectName("VOITURE_MODEL_input")
        self.VOITURE_MAT_input = QtWidgets.QLineEdit(self.centralwidget)
        self.VOITURE_MAT_input.setGeometry(QtCore.QRect(30, 190, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VOITURE_MAT_input.setFont(font)
        self.VOITURE_MAT_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.VOITURE_MAT_input.setText("")
        self.VOITURE_MAT_input.setObjectName("VOITURE_MAT_input")
        self.VOITURE_COLOR_input = QtWidgets.QLineEdit(self.centralwidget)
        self.VOITURE_COLOR_input.setGeometry(QtCore.QRect(340, 190, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VOITURE_COLOR_input.setFont(font)
        self.VOITURE_COLOR_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.VOITURE_COLOR_input.setObjectName("VOITURE_COLOR_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(9, 28, 149);")
        self.label.setObjectName("label")
        self.Add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Add_btn.setGeometry(QtCore.QRect(650, 300, 241, 71))
        self.Add_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Add_btn.setFont(font)
        self.Add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Add_btn.setStyleSheet("#Add_btn{\n"
"background-color: rgb(112, 162, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"border: 3px Solid rgb(17, 21, 255);\n"
"}\n"
"#Add_btn:hover:pressed{\n"
"background-color: rgb(190, 164, 255);\n"
"}")
        self.Add_btn.setObjectName("Add_btn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(46, 199, 12);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 140, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(46, 199, 12);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(640, 140, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(46, 199, 12);")
        self.label_7.setObjectName("label_7")
        self.VOITURE_YEAR_input = QtWidgets.QLineEdit(self.centralwidget)
        self.VOITURE_YEAR_input.setGeometry(QtCore.QRect(20, 350, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VOITURE_YEAR_input.setFont(font)
        self.VOITURE_YEAR_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.VOITURE_YEAR_input.setText("")
        self.VOITURE_YEAR_input.setObjectName("VOITURE_YEAR_input")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 300, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(46, 199, 12);")
        self.label_8.setObjectName("label_8")
        self.VOITURE_MARQUE_input = QtWidgets.QLineEdit(self.centralwidget)
        self.VOITURE_MARQUE_input.setGeometry(QtCore.QRect(330, 350, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VOITURE_MARQUE_input.setFont(font)
        self.VOITURE_MARQUE_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.VOITURE_MARQUE_input.setText("")
        self.VOITURE_MARQUE_input.setObjectName("VOITURE_MARQUE_input")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 300, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(46, 199, 12);")
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 460, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(9, 28, 149);")
        self.label_4.setObjectName("label_4")
        self.VOITURE_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.VOITURE_listWidget.setGeometry(QtCore.QRect(20, 510, 871, 231))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VOITURE_listWidget.setFont(font)
        self.VOITURE_listWidget.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.VOITURE_listWidget.setObjectName("VOITURE_listWidget")
        self.Delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_btn.setGeometry(QtCore.QRect(650, 400, 241, 71))
        self.Delete_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Delete_btn.setFont(font)
        self.Delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Delete_btn.setStyleSheet("#Delete_btn{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"background-color: rgb(255, 2, 14);\n"
"border: 3px Solid rgb(175, 34, 15);\n"
"}\n"
"#Delete_btn:hover:pressed{\n"
"background-color: rgb(255, 167, 43);\n"
"}\n"
"")
        self.Delete_btn.setObjectName("Delete_btn")
        LOCATION_DE_VOITURE.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LOCATION_DE_VOITURE)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 918, 29))
        self.menubar.setObjectName("menubar")
        LOCATION_DE_VOITURE.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LOCATION_DE_VOITURE)
        self.statusbar.setObjectName("statusbar")
        LOCATION_DE_VOITURE.setStatusBar(self.statusbar)

        self.retranslateUi(LOCATION_DE_VOITURE)
        QtCore.QMetaObject.connectSlotsByName(LOCATION_DE_VOITURE)

    def retranslateUi(self, LOCATION_DE_VOITURE):
        _translate = QtCore.QCoreApplication.translate
        LOCATION_DE_VOITURE.setWindowTitle(_translate("LOCATION_DE_VOITURE", "MainWindow"))
        self.VOITURE_MODEL_input.setPlaceholderText(_translate("LOCATION_DE_VOITURE", " model"))
        self.VOITURE_MAT_input.setPlaceholderText(_translate("LOCATION_DE_VOITURE", "50-A-1111"))
        self.VOITURE_COLOR_input.setPlaceholderText(_translate("LOCATION_DE_VOITURE", "color     "))
        self.label.setText(_translate("LOCATION_DE_VOITURE", "LOCATION VOITURE"))
        self.Add_btn.setText(_translate("LOCATION_DE_VOITURE", "Add "))
        self.label_5.setText(_translate("LOCATION_DE_VOITURE", "Voiture Matricule :"))
        self.label_6.setText(_translate("LOCATION_DE_VOITURE", "Voiture Color :"))
        self.label_7.setText(_translate("LOCATION_DE_VOITURE", "Voiture Model :"))
        self.VOITURE_YEAR_input.setPlaceholderText(_translate("LOCATION_DE_VOITURE", "2000"))
        self.label_8.setText(_translate("LOCATION_DE_VOITURE", "Voiture Year :"))
        self.VOITURE_MARQUE_input.setPlaceholderText(_translate("LOCATION_DE_VOITURE", "marque"))
        self.label_9.setText(_translate("LOCATION_DE_VOITURE", "Voiture Marque :"))
        self.label_4.setText(_translate("LOCATION_DE_VOITURE", "Voiture list  :"))
        self.Delete_btn.setText(_translate("LOCATION_DE_VOITURE", "Delete "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LOCATION_DE_VOITURE = QtWidgets.QMainWindow()
    ui = Ui_LOCATION_DE_VOITURE()
    ui.setupUi(LOCATION_DE_VOITURE)
    LOCATION_DE_VOITURE.show()
    sys.exit(app.exec_())