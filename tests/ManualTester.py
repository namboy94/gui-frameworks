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
from gfworks.templates.tk.TkGridTemplate import TkGridTemplate
from tkinter import *
from PIL import ImageTk, Image
import os

class TestGui(TkGridTemplate):

    def __init__(self):
        super().__init__("Test")

    def lay_out(self):
        imagelabel = self.generate_image_label("/home/hermann/Desktop/sun.png")
        print(imagelabel)
        imagelabel.pack()

if __name__ == '__main__':
    x = TestGui()
    x.start()