# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SENSUM_Plugin
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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "SENSUM_Plugin"


def description():
    return "First SENSUM plugin"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "SENSUM Consortium"

def email():
    return "giannicristian.iannelli@unipv.it"

def classFactory(iface):
    # load SENSUM_Plugin class from file SENSUM_Plugin
    from sensum_plugin import SENSUM_Plugin
    return SENSUM_Plugin(iface)
