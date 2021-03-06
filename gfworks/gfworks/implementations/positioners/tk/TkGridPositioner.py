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
import tkinter
from tkinter import N, E, S, W
from gfworks.interfaces.positioners.GenericGridPositioner import GenericGridPositioner


class TkGridPositioner(GenericGridPositioner):
    """
    Implements the grid positioner interface in Tk/Tkinter
    """

    rowcounter = 0
    columncounter = 0

    def position_absolute(self, widget: tkinter.Widget, x_position: int, y_position: int, x_size: int, y_size: int) \
            -> None:
        """
        Position a widget absolutely in a grid layout
        :param widget: the widget to be positioned
        :param x_position: the horizontal position of the widget in the grid
        :param y_position: the vertical position of the widget in the grid
        :param x_size: the width of the widget in the grid layout
        :param y_size: the width of the widget in the grid layout
        :return: void
        """
        widget.grid(column=x_position, row=y_position, columnspan=x_size, rowspan=y_size, sticky=W + E + N + S)
        if self.rowcounter < y_position + y_size:
            self.rowcounter = y_position + y_size
        if self.columncounter < x_position + x_size:
            self.columncounter = x_position + x_size

    def position_relative(self, widget: tkinter.Widget, neighbour: tkinter.Widget, orientation: str, x_size: int,
                          y_size: int, spacing: int = 0) -> None:
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
        neighbour = neighbour if spacing == 0 \
            else self.add_spacing_next_to(neighbour, orientation, x_spacing, y_spacing)

        neighbour_row = neighbour.grid_info()["row"]
        neighbour_column = neighbour.grid_info()["column"]
        neighbour_row_end = neighbour_row + neighbour.grid_info()["rowspan"]
        neighbour_column_end = neighbour_column + neighbour.grid_info()["columnspan"]

        if orientation.upper() in ["NORTH", "N", "TOP"]:
            row = neighbour_row - 1
            column = neighbour_column
        elif orientation.upper() in ["EAST", "E", "RIGHT"]:
            row = neighbour_row
            column = neighbour_column_end
        elif orientation.upper() in ["SOUTH", "S", "BOTTOM"]:
            row = neighbour_row_end
            column = neighbour_column
        elif orientation.upper() in ["WEST", "W", "LEFT"]:
            row = neighbour_row
            column = neighbour_column - 1
        else:
            raise ValueError("Incorrect orientation type " + orientation)

        widget.grid(row=row, column=column, rowspan=y_size, columnspan=x_size, sticky=W + E + N + S)

        self.columncounter = column + x_size if self.columncounter < column + x_size else self.columncounter
        self.rowcounter = row + y_size if self.rowcounter < row + y_size else self.rowcounter

    def add_spacing_next_to(self, widget: tkinter.Widget, orientation: str, x_size: int, y_size: int) -> tkinter.Widget:
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
        :return: the spacer label
        """
        spacer_label = tkinter.Label(self, text="")
        self.position_relative(spacer_label, widget, orientation, x_size, y_size)
        return spacer_label
