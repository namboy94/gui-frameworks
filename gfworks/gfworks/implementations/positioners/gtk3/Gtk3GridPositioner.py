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

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gfworks.interfaces.positioners.GenericGridPositioner import GenericGridPositioner


class Gtk3GridPositioner(GenericGridPositioner):
    """
    Implements the grid positioner interface in GTK 3/GObject
    """

    def __init__(self):
        """
        Dummy Constructor to avoid segfaults when no Window can be created
        """
        self.grid = Gtk.Grid()
        raise NotImplementedError("This is a dummy Constructor")

    def position_absolute(self, widget: Gtk.Widget, x_position: int, y_position: int, x_size: int, y_size: int) -> None:
        """
        Position a widget absolutely in a grid layout
        :param widget: the widget to be positioned
        :param x_position: the horizontal position of the widget in the grid
        :param y_position: the vertical position of the widget in the grid
        :param x_size: the width of the widget in the grid layout
        :param y_size: the width of the widget in the grid layout
        :return: void
        """
        widget.set_vexpand(True)
        widget.set_hexpand(True)
        widget.set_size_request(0, 0)
        self.grid.attach(widget, x_position, y_position, x_size, y_size)

    def position_relative(self, widget: Gtk.Widget, neighbour: Gtk.Widget, orientation: str, x_size: int, y_size: int,
                          spacing: int = 0) -> None:
        """
        Position a widget relatively to another widget in a grid layout
        :param widget: the widget to be positioned
        :param neighbour: the neighbour widget to be used as a reference point
        :param orientation: the orientation of the widget relative to the neighbour
                should be able to accept:
                    NORTH/EAST/SOUTH/WEST
                    N/E/S/W
                    TOP/BOTTOM/RIGHT/LEFT
                For Future: Maybe consider using a python enum equivalent
        :param x_size: the width of the widget in the grid layout
        :param y_size: the height of the widget in the grid layout
        :param spacing: space between the widgets
        :return: void
        """
        x_spacing = 1 if orientation.upper() in ["NORTH", "N", "TOP", "SOUTH", "S", "BOTTOM"] else spacing
        y_spacing = 1 if orientation.upper() in ["EAST", "E", "RIGHT", "WEST", "W", "LEFT"] else spacing
        root_widget = neighbour if spacing == 0 else \
            self.add_spacing_next_to(neighbour, orientation, x_spacing, y_spacing)

        widget.set_vexpand(True)
        widget.set_hexpand(True)
        widget.set_size_request(0, 0)

        if orientation.upper() in ["NORTH", "N", "TOP"]:
            self.grid.attach_next_to(widget, root_widget, Gtk.PositionType.TOP, x_size, y_size)
        elif orientation.upper() in ["EAST", "E", "RIGHT"]:
            self.grid.attach_next_to(widget, root_widget, Gtk.PositionType.RIGHT, x_size, y_size)
        elif orientation.upper() in ["SOUTH", "S", "BOTTOM"]:
            self.grid.attach_next_to(widget, root_widget, Gtk.PositionType.BOTTOM, x_size, y_size)
        elif orientation.upper() in ["WEST", "W", "LEFT"]:
            self.grid.attach_next_to(widget, root_widget, Gtk.PositionType.LEFT, x_size, y_size)
        else:
            raise ValueError("Incorrect orientation type " + orientation)

    def add_spacing_next_to(self, widget: Gtk.Widget, orientation: str, x_size: int, y_size: int) -> Gtk.Widget:
        """
        Adds an empty label next to a widget to add spacing between widgets
        :param widget: the widget to which the spacing will be added next to
        :param orientation: the direction from which the spacing will be added
                                should be able to accept:
                                    NORTH/EAST/SOUTH/WEST
                                    N/E/S/W
                                    TOP/BOTTOM/RIGHT/LEFT
                                For Future: Maybe consider using a python enum equivalent
        :param x_size: the width of the spacing
        :param y_size: the height of the spacing
        :return: the spacing label
        """
        spacer_label = Gtk.Label()
        spacer_text = " " * x_size
        spacer_label.set_text(spacer_text)
        self.position_relative(spacer_label, widget, orientation, x_size, y_size)
        return spacer_label
