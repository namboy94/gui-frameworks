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

from gi.repository import Gtk

from gfworks.interfaces.GenericWindow import GenericWindow
from gfworks.implementations.widgetgenerators.gtk3.Gtk3WidgetGenerator import Gtk3WidgetGenerator
from gfworks.implementations.positioners.gtk3.Gtk3GridPositioner import Gtk3GridPositioner
from gfworks.implementations.dialogshowers.gtk3.Gtk3DialogShower import Gtk3DialogShower
from gfworks.implementations.valuegetters.gtk3.Gtk3ValueGetter import Gtk3ValueGetter


class Gtk3GridTemplate(Gtk.Window,
                       GenericWindow,
                       Gtk3GridPositioner,
                       Gtk3WidgetGenerator,
                       Gtk3ValueGetter,
                       Gtk3DialogShower):
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
        self.window = None

        self.parent = parent
        self.hide_parent = hide_parent

        super().__init__(self, title=title)
        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.lay_out()

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
        if self.parent and self.hide_parent:
            self.parent.window.hide()
        self.window = self
        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()
        Gtk.main()
        if self.parent and self.hide_parent:
            self.parent.window.show_all()

    def stop(self):
        """
        Forcibly stops the Window
        :return: void
        """
        self.window.destroy()
        if self.parent and self.hide_parent:
            self.parent.window.show_all()
