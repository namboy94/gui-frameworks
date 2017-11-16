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

from gfworks.templates.generic.GenericGridTemplate import GenericGridTemplate
from gfworks.implementations.positioners.tk.TkGridPositioner import TkGridPositioner
from gfworks.implementations.generators.dialogshowers.tk.TkDialogShower import TkDialogShower
from gfworks.implementations.generators.widgetgenerators.tk.TkWidgetGenerator import TkWidgetGenerator
from gfworks.implementations.widgetdatamanipulators.widgetclearers.tk.TkWidgetClearer import TkWidgetClearer
from gfworks.implementations.widgetdatamanipulators.valuegetters.tk.TkValueGetter import TkValueGetter
from gfworks.implementations.widgetdatamanipulators.valuesetters.tk.TkValueSetter import TkValueSetter
from gfworks.implementations.threading.tk.TkThreading import TkThreading


class TkGridTemplate(TkWidgetGenerator,
                     TkValueGetter,
                     TkValueSetter,
                     TkWidgetClearer,
                     TkDialogShower,
                     TkGridPositioner,
                     TkThreading,
                     GenericGridTemplate):
    """
    Grid Gui Base written in Tk
    """

    identifier = "tk-grid"
    """
    An identifier to implement framework-specific code
    """

    def __init__(self, title: str = "Window", parent: tkinter.Tk = None, hide_parent: bool = True) -> None:
        """
        Constructor of the Window
        Should call lay_out at the end
        :param title: The window title
        :param parent: The parent window
        :param hide_parent: Flag that defines if the parent should be hidden
        :return: void
        """
        self.is_root_window = False
        if parent is None:
            self.tkinter_root = tkinter.Tk()
            self.tkinter_root.withdraw()
            self.is_root_window = True

        tkinter.Toplevel.__init__(self)
        self.title(title)
        self.parent = parent
        self.hide_parent = hide_parent
        self.lay_out()
        self.protocol("WM_DELETE_WINDOW", self.stop)

        i = 0
        while i < self.columncounter:
            tkinter.Grid.columnconfigure(self, i, weight=2)
            i += 1
        i = 0
        while i < self.rowcounter:
            tkinter.Grid.rowconfigure(self, i, weight=2)
            i += 1

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
        if self.parent is not None and self.hide_parent:
            self.parent.withdraw()
        self.mainloop()
        if self.parent is not None and self.hide_parent:
            # noinspection PyProtectedMember
            try:
                self.parent.deiconify()
            except tkinter._tkinter.TclError:
                pass

    def stop(self) -> None:
        """
        Forcibly stops the Window
        :return: void
        """
        if self.parent is not None and self.hide_parent:
            self.parent.deiconify()
        self.destroy()
        if self.is_root_window:
            self.tkinter_root.destroy()
