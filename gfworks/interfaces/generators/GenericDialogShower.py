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
    Interface that defines the requirements for a GUI framework to show dialogs.
    """

    def show_message_dialog(self, title: str, body: str) -> None:
        """
        Shows a message dialog which contains a message for the user and a button
        for the user to press to confirm
        :param title: the window title of the message dialog
        :param body: the body text of the dialog
        :return: void
        """
        raise NotImplementedError("show_message_dialog not implemented")

    def show_yes_no_dialog(self, title: str, body: str) -> bool:
        """
        Shows a yes/no dialog which shows some text and two buttons for the user to press.
        'Yes' will return True if pressed, 'No' returns False
        :param title: the window title of the yes/no dialog
        :param body: the body text of the dialog
        :return: True if 'Yes' was selected, False if 'No' was selected
        """
        raise NotImplementedError("show_yes_no_dialog not implemented")

    def show_file_chooser_dialog(self) -> str:
        """
        Shows a file chooser dialog that allows the user to select a file
        :return: the path to the selected file
        """
        raise NotImplementedError("show_file_chooser_dialog not implemented")

    def show_directory_chooser_dialog(self) -> str:
        """
        Shows a directory chooser dialog that allows the user to select a directory
        :return: the path to the selected directory
        """
        raise NotImplementedError("show_directory_chooser_dialog not implemented")

    def show_text_input_box(self, title: str, body: str) -> str:
        """
        Shows a text input dialog, enabling the user to enter some text and afterwards
        confirming it via a button
        :param title: the window title of the dialog
        :param body: the body text of the dialog
        :return: the entered text
        """
        raise NotImplementedError("show_text_input_box not implemented")
