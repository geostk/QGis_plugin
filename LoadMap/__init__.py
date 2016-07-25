# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LoadMap
                                 A QGIS plugin
 loads map from database
                             -------------------
        begin                : 2015-02-26
        copyright            : (C) 2015 by Mael
        email                : mael.taye@insa.gov.et
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LoadMap class from file LoadMap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .map_loader import LoadMap
    return LoadMap(iface)
