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

import sys

if sys.argv[1] == "gtk":

    from gfworks.templates.gtk3.Gtk3GridTemplate import Gtk3GridTemplate as Template

else:
    from gfworks.templates.tk.TkGridTemplate import TkGridTemplate as Template


class TestGui(Template):

    def __init__(self):
        super().__init__()

    def lay_out(self):
        self.panel = self.generate_image_label("/home/hermann/Desktop/sun.png", False, 1, 20)
        self.position_absolute(self.panel, 1, 2, 1, 1)

if __name__ == '__main__':

    TestGui().start()
