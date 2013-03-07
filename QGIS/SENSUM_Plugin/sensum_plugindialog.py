# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SENSUM_PluginDialog
                                 A QGIS plugin
 First SENSUM plugin
                             -------------------
        begin                : 2013-03-06
        copyright            : (C) 2013 by SENSUM Consortium
        email                : giannicristian.iannelli@unipv.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_sensum_plugin import Ui_SENSUM_Plugin
# create the dialog for zoom to point


class SENSUM_PluginDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_SENSUM_Plugin()
        self.ui.setupUi(self)
