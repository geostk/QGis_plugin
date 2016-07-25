# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ParcelSearch
                                 A QGIS plugin
 Search by UniqueParcelID
                             -------------------
        begin                : 2016-04-13
        copyright            : (C) 2016 by INSA
        email                : robel.g@insa.gov.et
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
    """Load ParcelSearch class from file ParcelSearch.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .parcel_search import ParcelSearch
    return ParcelSearch(iface)
