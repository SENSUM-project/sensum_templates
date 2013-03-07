# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sensum_plugin.ui'
#
# Created: Wed Mar 06 16:07:37 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SENSUM_Plugin(object):
    def setupUi(self, SENSUM_Plugin):
        SENSUM_Plugin.setObjectName(_fromUtf8("SENSUM_Plugin"))
        SENSUM_Plugin.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(SENSUM_Plugin)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(SENSUM_Plugin)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SENSUM_Plugin.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SENSUM_Plugin.reject)
        QtCore.QMetaObject.connectSlotsByName(SENSUM_Plugin)

    def retranslateUi(self, SENSUM_Plugin):
        SENSUM_Plugin.setWindowTitle(QtGui.QApplication.translate("SENSUM_Plugin", "SENSUM_Plugin", None, QtGui.QApplication.UnicodeUTF8))

