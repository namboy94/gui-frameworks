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

from gfworks.templates.gtk3.Gtk3GridTemplate import Gtk3GridTemplate


class Gtk3BasicGui(Gtk3GridTemplate):
    """
    Class that models the Welcome Screen GUI. It offers the choice of either
    using one of the already existing accounts in the file system, import an
    external file or creating a new account.
    """

    def __init__(self, title="Basic Gtk GUI"):
        """
        Extends the functionality of GenericGtkGui's constructor if needed
        :param title: the title of the GUI. Defaults to "Finance Manager"
        :return: void
        """
        self.label = None
        self.button = None
        self.text_entry = None
        self.combo_box = None
        super().__init__(title)

    def lay_out(self):
        """
        Lays out all needed objects of the GUI
        :return: void
        """
        self.label = self.generate_label("Label")
        self.position_absolute(self.label, 0, 0, 2, 1)
        self.button = self.generate_button("Button")
        self.position_absolute(self.button, 2, 0, 2, 1)
        self.text_entry = self.generate_text_entry("Entry")
        self.position_absolute(self.text_entry, 2, 2, 2, 1)
        self.combo_box = self.generate_string_combo_box(["Combo", "Box"])
        self.position_relative(self.combo_box, self.text_entry, "right", 3, 3)

    # noinspection PyMethodMayBeStatic
    def start(self):
        """
        Extends the functionality of GenericGtkGui's start method if needed
        :return: void
        """
        super().start()


if __name__ == '__main__':
    Gtk3BasicGui().start()