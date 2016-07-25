# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TaskManager
                                 A QGIS plugin
 Mange and Load Tasks
                             -------------------
        begin                : 2015-09-03
        copyright            : (C) 2015 by INSA
        email                : robgirmay@yahoo.com
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
    """Load TaskManager class from file TaskManager.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .task_manager import TaskManager
    return TaskManager(iface)
