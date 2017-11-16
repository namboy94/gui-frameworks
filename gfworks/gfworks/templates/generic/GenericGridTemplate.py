"""
Copyright 2016-2017 Hermann Krumrey <hermann@krumreyh.com>

This file is part of gfworks.

gfworks is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

gfworks is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with gfworks.  If not, see <http://www.gnu.org/licenses/>.
"""

from gfworks.interfaces.GenericWindow import GenericWindow
from gfworks.interfaces.positioners.GenericGridPositioner import GenericGridPositioner
from gfworks.interfaces.generators.GenericWidgetGenerator import GenericWidgetGenerator
from gfworks.interfaces.generators.GenericDialogShower import GenericDialogShower
from gfworks.interfaces.threading.Threading import Threading
from gfworks.interfaces.widgetdatamanipulators.GenericValueGetter import GenericValueGetter
from gfworks.interfaces.widgetdatamanipulators.GenericValueSetter import GenericValueSetter
from gfworks.interfaces.widgetdatamanipulators.GenericWidgetClearer import GenericWidgetClearer


# noinspection PyAbstractClass
class GenericGridTemplate(GenericWidgetGenerator,
                          GenericValueGetter,
                          GenericValueSetter,
                          GenericWidgetClearer,
                          GenericDialogShower,
                          Threading,
                          GenericGridPositioner,
                          GenericWindow):
    """
    The buildup of a Generic Grid Template
    """

    identifier = "generic-grid"
    """
    An identifier to implement framework-specific code
    """
