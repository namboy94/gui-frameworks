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

from gfworks.interfaces.generators.GenericDialogShower import GenericDialogShower


class Gtk3DialogShower(Gtk.Window, GenericDialogShower):
    """
    Implements the Dialog showing commands for GTK 3 (GObject)
    """

    def show_message_dialog(self, title: str, body: str) -> None:
        """
        Shows a message dialog which contains a message for the user and a button
        for the user to press to confirm
        :param title: the window title of the message dialog
        :param body: the body text of the dialog
        :return: void
        """
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, title)
        dialog.format_secondary_text(body)
        dialog.run()
        dialog.destroy()

    def show_yes_no_dialog(self, title: str, body: str) -> bool:
        """
        Shows a yes/no dialog which shows some text and two buttons for the user to press.
        'Yes' will return True if pressed, 'No' returns False
        :param title: the window title of the yes/no dialog
        :param body: the body text of the dialog
        :return: True if 'Yes' was selected, False if 'No' was selected
        """
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, title)
        dialog.format_secondary_text(body)
        response = dialog.run()
        dialog.destroy()
        if response == Gtk.ResponseType.YES:
            return True
        else:
            return False

    def show_file_chooser_dialog(self) -> str:
        """
        Shows a file chooser dialog that allows the user to select a file
        :return: the path to the selected file
        """
        dialog = Gtk.FileChooserDialog("Please choose a file", self, Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = dialog.run()
        selected_file = ""
        if response == Gtk.ResponseType.OK:
            selected_file = dialog.get_filename()
        dialog.destroy()
        return selected_file

    def show_directory_chooser_dialog(self) -> str:
        """
        Shows a directory chooser dialog that allows the user to select a directory
        :return: the path to the selected directory
        """
        dialog = Gtk.FileChooserDialog("Please choose a file", self, Gtk.FileChooserAction.SELECT_FOLDER,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = dialog.run()
        directory = ""
        if response == Gtk.ResponseType.OK:
            directory = dialog.get_filename()
        dialog.destroy()
        return directory

    def show_text_input_box(self, title: str, body: str) -> str:
        """
        Shows a text input dialog, enabling the user to enter some text and afterwards
        confirming it via a button
        :param title: the window title of the dialog
        :param body: the body text of the dialog
        :return: the entered text, or an empty string if the operation was cancelled
        """
        # TODO make window title
        str(title)
        dialog = Gtk.MessageDialog(self, Gtk.DialogFlags.MODAL | Gtk.DialogFlags.DESTROY_WITH_PARENT,
                                   Gtk.MessageType.QUESTION, Gtk.ButtonsType.OK_CANCEL, body)

        dialog_box = dialog.get_content_area()
        user_entry = Gtk.Entry()
        user_entry.set_size_request(250, 0)
        dialog_box.pack_end(user_entry, False, False, 0)

        dialog.show_all()

        response = dialog.run()
        response_text = user_entry.get_text()
        dialog.destroy()
        if (response == Gtk.ResponseType.OK) and (response_text != ''):
            return response_text
        else:
            return ""
