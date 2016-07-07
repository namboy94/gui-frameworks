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

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gfworks.templates.generic.GenericGridTemplate import GenericGridTemplate
from gfworks.implementations.positioners.gtk3.Gtk3GridPositioner import Gtk3GridPositioner
from gfworks.implementations.generators.widgetgenerators.gtk3.Gtk3WidgetGenerator import Gtk3WidgetGenerator
from gfworks.implementations.generators.dialogshowers.gtk3.Gtk3DialogShower import Gtk3DialogShower
from gfworks.implementations.threading.gtk3.Gtk3Threading import Gtk3Threading
from gfworks.implementations.widgetdatamanipulators.valuegetters.gtk3.Gtk3ValueGetter import Gtk3ValueGetter
from gfworks.implementations.widgetdatamanipulators.valuesetters.gtk3.Gtk3ValueSetter import Gtk3ValueSetter
from gfworks.implementations.widgetdatamanipulators.widgetclearers.gtk3.Gtk3WidgetClearer import Gtk3WidgetClearer


class Gtk3GridTemplate(Gtk3WidgetGenerator,
                       Gtk3ValueGetter,
                       Gtk3ValueSetter,
                       Gtk3WidgetClearer,
                       Gtk3DialogShower,
                       Gtk3Threading,
                       Gtk3GridPositioner,
                       GenericGridTemplate):
    """
    Grid GUI base written in Gtk 3
    """

    identifier = "gtk3-grid"
    """
    An identifier to implement framework-specific code
    """

    def __init__(self, title: str = "Window", parent: Gtk.Window = None, hide_parent: bool = True) -> None:
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

        # noinspection PyCallByClass
        Gtk.Window.__init__(self, title=title)
        self.grid = Gtk.Grid()
        self.add(self.grid)
        self.lay_out()

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
        if self.parent and self.hide_parent:
            self.parent.hide()
        self.window = self
        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()
        Gtk.main()
        self.stop()
        if self.parent and self.hide_parent:
            self.parent.show_all()

    def stop(self) -> None:
        """
        Forcibly stops the Window
        :return: void
        """
        self.window.destroy()
        if self.parent and self.hide_parent:
            self.parent.show_all()
