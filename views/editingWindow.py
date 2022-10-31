# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(250, 252)
        Dialog.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./imgs/Logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("* {\n"
"    font-family: Roboto, Arial;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"    border-bottom: 1px solid #000;\n"
"    font-size: 16px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-size: 17px;\n"
"    background: #127FFF;\n"
"    color: #fff;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #2288FF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"        background: #0276FE;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(25, -1, 25, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setStyleSheet("Font-size: 20px;\n"
"font-weight: bold;\n"
"color: #FF5C00;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ledName = QtWidgets.QLineEdit(Dialog)
        self.ledName.setMinimumSize(QtCore.QSize(180, 0))
        self.ledName.setAlignment(QtCore.Qt.AlignCenter)
        self.ledName.setObjectName("ledName")
        self.verticalLayout.addWidget(self.ledName)
        self.ledAge = QtWidgets.QLineEdit(Dialog)
        self.ledAge.setMinimumSize(QtCore.QSize(180, 0))
        self.ledAge.setAlignment(QtCore.Qt.AlignCenter)
        self.ledAge.setObjectName("ledAge")
        self.verticalLayout.addWidget(self.ledAge)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnSave = QtWidgets.QPushButton(Dialog)
        self.btnSave.setMinimumSize(QtCore.QSize(120, 40))
        self.btnSave.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSave.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./imgs/disco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon1)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Editando..."))
        self.label_3.setText(_translate("Dialog", "EDITAR"))
        self.ledName.setPlaceholderText(_translate("Dialog", "Nombre"))
        self.ledAge.setPlaceholderText(_translate("Dialog", "Edad"))
        self.btnSave.setToolTip(_translate("Dialog", "(Enter)"))
        self.btnSave.setText(_translate("Dialog", " Guardar"))
        self.btnSave.setShortcut(_translate("Dialog", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())