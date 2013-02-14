# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agenda.ui'
#
# Created: Mon Feb  4 13:43:33 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
# pyside-uic -o agenda_src.py agenda.ui
# WARNING! All changes made in this file will be lost!

import sys
from PySide import QtCore, QtGui
from rutinas.varias import *

ruta_arch_conf = os.path.dirname(sys.argv[0])
archivo_configuracion = os.path.join(ruta_arch_conf, 'agenda.conf')
fc = FileConfig(archivo_configuracion)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(602, 491)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/agenda.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 611, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 178, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 213, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 89, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 119, 146))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 178, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 216, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 178, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 213, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 89, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 119, 146))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 178, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 216, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 89, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 178, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 248, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 213, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 89, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 119, 146))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 89, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 89, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 178, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 178, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 178, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.widget.setPalette(palette)
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.btnNuevo = QtGui.QPushButton(self.widget)
        self.btnNuevo.setGeometry(QtCore.QRect(10, 10, 91, 41))
        self.btnNuevo.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/30px-Crystal_Clear_app_List_manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon1)
        self.btnNuevo.setObjectName("btnNuevo")
        self.btnModificar = QtGui.QPushButton(self.widget)
        self.btnModificar.setEnabled(False)
        self.btnModificar.setGeometry(QtCore.QRect(110, 10, 91, 41))
        self.btnModificar.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/40px-Crystal_Clear_app_kedit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon2)
        self.btnModificar.setObjectName("btnModificar")
        self.btnEliminar = QtGui.QPushButton(self.widget)
        self.btnEliminar.setGeometry(QtCore.QRect(210, 10, 91, 41))
        self.btnEliminar.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/30px_1 (514).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon3)
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnDeshacer = QtGui.QPushButton(self.widget)
        self.btnDeshacer.setGeometry(QtCore.QRect(310, 10, 91, 41))
        self.btnDeshacer.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/40px_reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDeshacer.setIcon(icon4)
        self.btnDeshacer.setObjectName("btnDeshacer")
        self.btnSalir = QtGui.QPushButton(self.widget)
        self.btnSalir.setGeometry(QtCore.QRect(510, 10, 91, 41))
        self.btnSalir.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/25px_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon5)
        self.btnSalir.setObjectName("btnSalir")
        self.btnLimpiar = QtGui.QPushButton(self.widget)
        self.btnLimpiar.setGeometry(QtCore.QRect(410, 10, 91, 41))
        self.btnLimpiar.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/erase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar.setIcon(icon6)
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 80, 601, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 222, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 238, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 111, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 148, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 222, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 238, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 222, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 238, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 111, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 148, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 222, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 238, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 111, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 222, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(237, 238, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 111, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 148, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 111, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 111, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 222, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 222, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 222, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lblId = QtGui.QLabel(self.frame)
        self.lblId.setGeometry(QtCore.QRect(10, 20, 62, 15))
        self.lblId.setObjectName("lblId")
        self.txtId = QtGui.QLineEdit(self.frame)
        self.txtId.setGeometry(QtCore.QRect(10, 40, 51, 23))
        self.txtId.setObjectName("txtId")
        self.txtNombre = QtGui.QLineEdit(self.frame)
        self.txtNombre.setGeometry(QtCore.QRect(70, 40, 181, 23))
        self.txtNombre.setObjectName("txtNombre")
        self.lblNombre = QtGui.QLabel(self.frame)
        self.lblNombre.setGeometry(QtCore.QRect(70, 20, 62, 15))
        self.lblNombre.setObjectName("lblNombre")
        self.txtDepartamento = QtGui.QLineEdit(self.frame)
        self.txtDepartamento.setGeometry(QtCore.QRect(260, 40, 161, 23))
        self.txtDepartamento.setObjectName("txtDepartamento")
        self.lblDepartamento = QtGui.QLabel(self.frame)
        self.lblDepartamento.setGeometry(QtCore.QRect(260, 20, 121, 16))
        self.lblDepartamento.setObjectName("lblDepartamento")
        self.lblTelefono = QtGui.QLabel(self.frame)
        self.lblTelefono.setGeometry(QtCore.QRect(430, 20, 62, 15))
        self.lblTelefono.setObjectName("lblTelefono")
        self.txtTelefono = QtGui.QLineEdit(self.frame)
        self.txtTelefono.setGeometry(QtCore.QRect(430, 40, 161, 23))
        self.txtTelefono.setObjectName("txtTelefono")
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 170, 581, 291))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 222, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 206, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 222, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 206, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)

        #hasta aqui
        QtCore.QObject.connect(self.btnNuevo, QtCore.SIGNAL("clicked()"), self.nuevoGuardar)
        QtCore.QObject.connect(self.btnModificar, QtCore.SIGNAL("clicked()"), self.modificarGuardar)
        QtCore.QObject.connect(self.btnEliminar, QtCore.SIGNAL("clicked()"), self.preguntarEliminar)
        QtCore.QObject.connect(self.btnDeshacer, QtCore.SIGNAL("clicked()"), self.iniciarForm)
        QtCore.QObject.connect(self.btnLimpiar, QtCore.SIGNAL("clicked()"), self.limpiar_text)
        QtCore.QObject.connect(self.btnSalir, QtCore.SIGNAL("clicked()"), Form.close)
        QtCore.QObject.connect(self.txtNombre, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        QtCore.QObject.connect(self.txtDepartamento, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        QtCore.QObject.connect(self.txtTelefono, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("itemClicked(QTableWidgetItem*)"), self.clickEnTabla)
        

        Form.setTabOrder(self.btnNuevo, self.btnModificar)
        Form.setTabOrder(self.btnModificar, self.btnEliminar)
        Form.setTabOrder(self.btnEliminar, self.btnDeshacer)
        Form.setTabOrder(self.btnDeshacer, self.btnLimpiar)
        Form.setTabOrder(self.btnLimpiar, self.btnSalir)
        Form.setTabOrder(self.btnSalir, self.txtId)
        Form.setTabOrder(self.txtId, self.txtNombre)
        Form.setTabOrder(self.txtNombre, self.txtDepartamento)
        Form.setTabOrder(self.txtDepartamento, self.txtTelefono)
        Form.setTabOrder(self.txtTelefono, self.tableWidget)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Agenda Telefonica Hospital Coromoto", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNuevo.setText(QtGui.QApplication.translate("Form", "&Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.btnModificar.setText(QtGui.QApplication.translate("Form", "&Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEliminar.setText(QtGui.QApplication.translate("Form", "&Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDeshacer.setText(QtGui.QApplication.translate("Form", "&Deshacer", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSalir.setText(QtGui.QApplication.translate("Form", "&Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLimpiar.setText(QtGui.QApplication.translate("Form", "&Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.lblId.setText(QtGui.QApplication.translate("Form", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.lblNombre.setText(QtGui.QApplication.translate("Form", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDepartamento.setText(QtGui.QApplication.translate("Form", "Departamento", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTelefono.setText(QtGui.QApplication.translate("Form", "Telefono", None, QtGui.QApplication.UnicodeUTF8))

        self.main()


    def main(self):
        host,  db, user, clave = fc.opcion_consultar('POSTGRESQL')
        self.cadconex = "host='%s' dbname='%s' user='%s' password='%s'" % (host[1], db[1], user[1], clave[1])

        self.iniciarForm()
        self.Buscar()

    def iniciarForm(self):
        '''
        '''

        #Activar la Busqueda al escribir el los textbox
        self.activarBuscar = True

        #Activar Bandera para saber cuando el boton Nuevo funciona como Boton Nuevo
        self.banderaNuevo = True
        self.banderaModificar = True

        #Deshabilitar y Habilitar botones
        self.btnNuevo.setEnabled(True)
        self.btnModificar.setEnabled(False)
        self.btnEliminar.setEnabled(False)
        self.btnLimpiar.setEnabled(True)
        self.btnDeshacer.setEnabled(False)
        self.btnSalir.setEnabled(True)

        #Cambiar el Caption o Text del Boton
        self.btnNuevo.setText("&Nuevo")
        self.btnModificar.setText('&Modificar')

        #Cambiar icono del Boton Nuevo por Nuevo
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/30px-Crystal_Clear_app_List_manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon1)
        
        #Cambiar icono del Boton Modificar por Modificar
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/40px-Crystal_Clear_app_kedit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon2)

    def Buscar(self):
        '''
        Metodo que se utiliza para realizar la busqueda segun lo que
        ingresa el usuario en las cajas de texto.
        '''
        
        if self.activarBuscar:
            cadsq = self.armar_select()
            lista = self.obtener_datos(cadsq)
            self.PrepararTableWidget(len(lista))  # Configurar el tableWidget
            self.InsertarRegistros(lista)  # Insertar los Registros en el TableWidget

    def armar_select(self):
        '''
        Metodo que permite armar la consulta select a medica que el usuario
        va tecleando en los textbox
        Parametro devuelto(1) String con la cadena sql de busqueda    
        '''

        lcNombre = self.txtNombre.text()
        lcDepartamento = self.txtDepartamento.text()
        lcTelefono = self.txtTelefono.text()

        valorNombre =  "upper(nombre) like '%%%s%%' AND " % (lcNombre.upper()) if lcNombre else ''
        valorDepartamento =  " upper(departamento) like '%%%s%%' AND " % (lcDepartamento.upper()) if lcDepartamento else ''
        valorTelefono = " telefono like '%%%s%%' AND " % (lcTelefono) if lcTelefono else ''

        campos = valorNombre + valorDepartamento + valorTelefono
        cadenaSql = 'select id,nombre,departamento,telefono from agenda where ' + campos + 'del = 0 order by nombre'
        return cadenaSql

    def PrepararTableWidget(self, CantidadReg=0):
        '''
        Meotod que permite asignar y ajustar  las columnas que tendra el tablewidget
        basados en la cantidad de conlumnas y la cantidad de registros que le son
        pasados como parametro
        #Ej: lista = ((0, 'Carlos Garcia', 'Sistemas', '41075'), (1, 'Nairesther Gomez', 'Docencia', '41075')) 
        '''

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(245, 244, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)

        brush = QtGui.QBrush(QtGui.QColor(254, 206, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)

        lista = CantidadReg
        
        #Indicar los nombres que tendran las cabeceras de los campos o columnas
        cabecera = ["ID", "Nombre", "Departamento", "Telefono"]
        
        self.tableWidget.setColumnCount(len(cabecera))
        self.tableWidget.setRowCount(lista)

        self.tableWidget.setHorizontalHeaderLabels(cabecera)
        self.tableWidget.setPalette(palette)

        #Ajustar el ancho de las columnas
        self.tableWidget.horizontalHeader().resizeSection(0, 40)
        self.tableWidget.horizontalHeader().resizeSection(1, 206)
        self.tableWidget.horizontalHeader().resizeSection(2, 216)
        self.tableWidget.horizontalHeader().resizeSection(3, 90)

        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setAlternatingRowColors(True)

        self.tableWidget.setSelectionMode(QtGui.QTableWidget.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QTableView.SelectRows)

        #ciudades = ["Valencia","Maracay","Barquisimeto","Merida","Caracas"]
        #self.combo.addItems(ciudades)
        #deshabilitar() 

    def InsertarRegistros(self, cursor):
        '''
        Metodo que permite asignarle registros al tablewidget
        parametros recibitos (1) Tipo (Lista)
        Ej:RowSource(['0', 'Carlos', 'Garcia'], ['1', 'Nairesther', 'Gomez'])
        '''

        ListaCursor = cursor
        for pos, fila in enumerate(ListaCursor):
            for posc, columna in enumerate(fila):
                self.tableWidget.setItem(pos, posc, QtGui.QTableWidgetItem(str(columna)))

    def obtener_datos(self, cadena_pasada):
        '''
        Ejecuta la Consulta SQl a el servidor PostGreSQL segun la cadena SQL
        pasada como parametro
        parametros recibidos: (1) String
        parametros devueltos: (1) Lista

        Ej: obtener_datos('select *from tabla where condicion')
        '''

        try:
            pg = ConectarPG(self.cadconex)
            self.registros = pg.ejecutar(cadena_pasada)
            pg.cur.close()
            pg.conn.close()
        except:
            self.registros = []
        return self.registros

    def limpiar_text(self):
        '''
        Limpia los QlineEdit o Textbox
        '''
        self.txtId.clear()
        self.txtNombre.clear()
        self.txtDepartamento.clear()
        self.txtTelefono.clear()
        self.iniciarForm()

    def clickEnTabla(self):
        '''
        Este metodo se activa al momento de hace click en el tableWidget y permite
        mostrar el contenido de los campos de la fila seleccionada en el tableWidget
        en los textbox bien sea para Verlos, modificarlos o Eliminarlos
        '''

        self.activarBuscar = False
         
        fila = self.tableWidget.currentRow()
        #total_columnas = self.tableWidget.columnCount()
        
        id = self.tableWidget.item(fila, 0).text()
        nombre = self.tableWidget.item(fila, 1).text()
        dpto = self.tableWidget.item(fila, 2).text()
        tlf = self.tableWidget.item(fila, 3).text()

        self.txtId.setText(id)
        self.txtNombre.setText(nombre)
        self.txtDepartamento.setText(dpto)
        self.txtTelefono.setText(tlf) 

        self.btnModificar.setEnabled(True)
        self.btnEliminar.setEnabled(True)

    def nuevoGuardar(self):
        '''
        El metodo nuevo cumple dos funciones, una es de boton nuevo y otra es de boton guardar,
        la Variables self.banderaNuevo es el swith que me permite saber cuando el 
        boton nuevo hace la funcion de nuevo o de guardar, cuando la variable
        banderaNuevo es True entonces el boton debe actuar como Boton Nuevo de
        lo contrario cuando banderaNuevo es false entonces el boton nuevo debe 
        actuar como boton Guardar
        
        lcMensaje = 'Hola'  # self.combo.currentText()
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, 'Titulo',lcMensaje)
        msgBox.exec_()
        '''

        if self.banderaNuevo:
            #Prepara los Botones
            self.habilitarNuevo()
        else:
            #Ejecurar sentencia SQL para guardar en PostGreSQL
            nombre = self.txtNombre.text()
            dpto = self.txtDepartamento.text()
            telf = self.txtTelefono.text()

            sqlInsert = " insert into agenda (nombre, departamento, telefono) values ('%s', '%s', '%s') " % (nombre, dpto, telf)
            
            try:
                pg = ConectarPG(self.cadconex)
                pg.ejecutar(sqlInsert)
                pg.conn.commit()

                lcMensaje = 'Registro Guardaro Satisfactoriamente'  # self.combo.currentText()
                msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, 'Felicidades',lcMensaje)
                msgBox.exec_()
            except:
                print exceptionValue
            
            #Restaurar todos los Iconos y Botones
            self.iniciarForm()
            self.limpiar_text()


    def habilitarNuevo(self):
        ''' 
         Este metodo permite preparar los botones, los text y los iconos.
         Cuando se presiona el boton nuevo por primera vez este cambia para Boton Guardar asi como  
         tanmbien el icono y el texto del boton y desabilita el resto de los botonos, dejando solo 
         el boton Guardar,deshacer y salir
        '''

        #Limpar los TextBox
        self.limpiar_text()

        #Desactivar la Busqueda al escribir el los textbox
        self.activarBuscar = False

        #Activar Bandera para saber cuando el boton Nuevo funciona como Boton Nuevo o Como Boton Guardar
        self.banderaNuevo = False

        #Deshabilitar y Habilitar botonoes
        self.btnModificar.setEnabled(False)
        self.btnEliminar.setEnabled(False)
        self.btnLimpiar.setEnabled(False)
        self.btnDeshacer.setEnabled(True)
            
        #Cambiar el Caption o Text del Boton
        self.btnNuevo.setText("&Guardar")
            
        #Cambiar icono del Boton Nuevo  de Nuevo por Guardar
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/40px_3floppy_unmount.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNuevo.setIcon(icon1)
        self.txtNombre.setFocus()

    def modificarGuardar(self):
        '''
        El metodo modificarGuardar cumple dos funciones, una es de boton Modificar y otra es de boton guardar,
        la Variables self.banderaModificar es el swith que me permite saber cuando el 
        boton Modificar hace la funcion de Modificar o de guardar, cuando la variable
        banderaModificar es True entonces el boton debe actuar como Boton Guardar de
        lo contrario cuando banderaModificar es false entonces el boton nuevo debe 
        actuar como boton Guardar
        '''

        if self.banderaModificar:
            #Prepara los Botones
            self.habilitarModificar()
        else:            
            #Ejecurar sentencia SQL para guardar en PostGreSQL
            id = self.txtId.text()
            nombre = self.txtNombre.text()
            dpto = self.txtDepartamento.text()
            telf = self.txtTelefono.text()

            sqlUpdate = " update agenda set nombre = '%s', departamento = '%s', telefono = '%s' where id = %s " % (nombre, dpto, telf, id)
            print sqlUpdate

            try:
                pg = ConectarPG(self.cadconex)
                pg.ejecutar(sqlUpdate)
                pg.conn.commit()

                lcMensaje = 'Registro Guardaro Satisfactoriamente'  # self.combo.currentText()
                msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, 'Felicidades',lcMensaje)
                msgBox.exec_()
            except:
                print exceptionValue
            
            #Restaurar los Botones a su normalidad
            self.iniciarForm()
            self.limpiar_text()


    def habilitarModificar(self):
        ''' 
         Este metodo permite habilitar el Boton Modificar.
         Cuando se presiona el boton Modificar por primera vez este cambia para Boton Guardar asi como  
         tanmbien el icono y el texto del boton y desabilita el resto de los botonos, dejando solo el 
         boton Guardar,deshacer y salir
        '''

        #Desactivar la Busqueda al escribir el los QlineEdit o TextBox
        self.activarBuscar = False

        #Activar Bandera para saber cuando el boton Nuevo funciona como Boton Nuevo o Como Boton Guardar
        self.banderaModificar = False
            
        #Deshabilitar y Habilitar botonoes y TextBox
        self.txtId.setEnabled(False)

        self.btnNuevo.setEnabled(False)
        self.btnEliminar.setEnabled(False)
        self.btnLimpiar.setEnabled(False)
        self.btnDeshacer.setEnabled(True)
            
        #Cambiar el Caption o Text del Boton
        self.btnModificar.setText("&Guardar")
            
        #Cambiar icono del Boton Nuevo  de Nuevo por Guardar
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/40px_3floppy_unmount.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon1)
        self.txtNombre.setFocus()

    def preguntarEliminar(self):
        '''
        Metodo que permite Consultar si se desea eliminar un registro de la Agenda
        '''
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, 'Informacion', 'Este Registro sera Eliminado')
        msgBox.setInformativeText(u"¿Esta Seguro que desea eliminar este registro?")
        
        GuardarButton = msgBox.addButton("&Aceptar", QtGui.QMessageBox.ActionRole)
        CancelarButton = msgBox.addButton("&Cancelar", QtGui.QMessageBox.ActionRole)
        msgBox.exec_()
        
        if msgBox.clickedButton() == GuardarButton:
            print 'Aceptar'
            self.eliminar()
        
        elif msgBox.clickedButton() == CancelarButton:
            #print 'Cancelar'
            pass

    def eliminar(self):
        '''
        Metodo que permite eliminar de la base de datos un registro de la agenda
        '''
        
        id = self.txtId.text()
        sqlDelete = " update agenda set del = 1 where id = %s " % (id)
        print sqlDelete

        try:
            pg = ConectarPG(self.cadconex)
            pg.ejecutar(sqlDelete)
            pg.conn.commit()

            lcMensaje = 'Registro Eliminado Satisfactoriamente'
            msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, 'Felicidades',lcMensaje)
            msgBox.exec_()
        except:
            print exceptionValue
        
        #Restaurar los Botones a su normalidad
        self.iniciarForm()
        self.limpiar_text()

    def salir(self):
        pass

    def borrar(self):
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, 'Titulo', 'Prueba')
        #msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
        GuardarButton = msgBox.addButton("Guardar", QtGui.QMessageBox.ActionRole)
        AbortarButton = msgBox.addButton("Cancelar", QtGui.QMessageBox.ActionRole)
        msgBox.exec_()
        print GuardarButton
        print AbortarButton

    def GoFocus(self):
        lcMensaje = 'Hola'  # self.combo.currentText()
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, 'Titulo',lcMensaje)
        msgBox.exec_()


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui =  Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
