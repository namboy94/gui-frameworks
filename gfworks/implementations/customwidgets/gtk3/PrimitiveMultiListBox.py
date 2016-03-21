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


class PrimitiveMultiListBox(object):
    """
    A multi list box object that stores primitive values like str and int
    """

    def __init__(self,
                 scrollable_tree_list: Gtk.ScrolledWindow,
                 tree_selection: Gtk.TreeSelection,
                 list_store: Gtk.ListStore):
        self.scrollable_tree_list = scrollable_tree_list
        self.tree_selection = tree_selection
        self.list_store = list_store
