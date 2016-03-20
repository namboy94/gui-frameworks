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


class GenericDialogShower(object):
    """
    Interface that defines the requirements for a GUI framework to show specific dialogs.
    """

    def show_message_dialog(self, title, body):
        raise NotImplementedError()

    def show_yes_no_dialog(self, title, body):
        raise NotImplementedError()

    def show_file_chooser_dialog(self):
        raise NotImplementedError()

    def show_directory_chooser_dialog(self):
        raise NotImplementedError()

    def show_text_input_box(self, title, body):
        raise NotImplementedError()