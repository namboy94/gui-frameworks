"""
LICENSE:
Copyright 2016 Hermann Krumrey

This file is part of gfworks.

    gfworks is a collection of classes and methods that are designed to make
    cross-framework GUI design easier by standardizing a lot of framework-specific
    functionality with a unified interface.

    gfworks is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    gfworks is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with gfworks. If not, see <http://www.gnu.org/licenses/>.
LICENSE
"""


class GenericGridPositioner(object):
    """
    Interface that defines the requirements for a grid layout based GUI to position widgets.
    """

    def position_absolute(self, widget: object, x_position: int, y_position: int, x_size: int, y_size: int) -> None:
        """
        Position a widget absolutely in a grid layout
        :param widget: the widget to be positioned
        :param x_position: the horizontal position of the widget in the grid
        :param y_position: the vertical position of the widget in the grid
        :param x_size: the width of the widget in the grid layout
        :param y_size: the width of the widget in the grid layout
        :return: void
        """
        raise NotImplementedError("position_absolute not implemented")

    def position_relative(self, widget: object, neighbour: object, orientation: str, x_size: int, y_size: int) -> None:
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
        :return: void
        """
        raise NotImplementedError("position_relative not implemented")

    def add_spacing_next_to(self, widget: object, orientation: str, x_size: int, y_size: int) -> None:
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
        :return: None
        """
        raise NotImplementedError("add_spacing_next_to not implemented")
