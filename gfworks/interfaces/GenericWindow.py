"""
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
"""


class GenericWindow(object):
    """
    Interface that defines how a window is initialized, run and closed
    """

    def __init__(self, title: str = "Window", parent: object = None, hide_parent: bool = True) -> None:
        """
        Constructor of the Window
        Should call lay_out at the end
        :param title: The window title
        :param parent: The parent window
        :param hide_parent: Flag that defines if the parent should be hidden
        :return: void
        """
        str(title)
        str(parent)
        str(hide_parent)
        raise NotImplementedError("Constructor not implemented")

    def lay_out(self) -> None:
        """
        Initializes widgets and positions them in the Window
        :return: void
        """
        raise NotImplementedError("lay_out not implemented")

    def start(self) -> None:
        """
        Starts the Window main loop
        :return:void
        """
        raise NotImplementedError("start not implemented")

    def stop(self) -> None:
        """
        Forcibly stops the Window
        :return: void
        """
        raise NotImplementedError("stop not implemented")
