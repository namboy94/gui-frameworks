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

import tkinter

from gfworks.interfaces.GenericWindow import GenericWindow
from gfworks.implementations.valuegetters.tk.TkValueGetter import TkValueGetter
from gfworks.implementations.widgetgenerators.tk.TkWidgetGenerator import TkWidgetGenerator
from gfworks.implementations.dialogshowers.tk.TkDialogShower import TkDialogShower
from gfworks.implementations.positioners.tk.TkGridPositioner import TkGridPositioner


class TkGridTemplate(tkinter.Tk,
                     GenericWindow,
                     TkWidgetGenerator,
                     TkValueGetter,
                     TkDialogShower,
                     TkGridPositioner):
    """
    Interface that defines how a window is initialized, run and closed
    """

    def __init__(self, title: str = "Window", parent=None, hide_parent: bool = True):
        """
        Constructor of the Window
        Should call lay_out at the end
        :param title: The window title
        :param parent: The parent window
        :param hide_parent: Flag that defines if the parent should be hidden
        :return: void
        """
        super().__init__()
        self.title(title)
        self.parent = parent
        self.hide_parent = hide_parent
        self.lay_out()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def lay_out(self):
        """
        Initializes widgets and positions them in the Window
        :return: void
        """
        raise NotImplementedError("lay_out not implemented")

    def start(self):
        """
        Starts the Window main loop
        :return:void
        """
        if self.parent is not None and self.hide_parent:
            self.parent.withdraw()
        self.mainloop()
        if self.parent is not None and self.hide_parent:
            self.parent.deiconify()

    def stop(self):
        """
        Forcibly stops the Window
        :return: void
        """
        if self.parent is not None and self.hide_parent:
            self.parent.deiconify()
        self.destroy()
