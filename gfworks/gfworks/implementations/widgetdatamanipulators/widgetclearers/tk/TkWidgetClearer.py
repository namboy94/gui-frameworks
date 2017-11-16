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
from tkinter import ttk

from gfworks.interfaces.widgetdatamanipulators.GenericWidgetClearer import GenericWidgetClearer


class TkWidgetClearer(GenericWidgetClearer):
    """
    Implements methods to clear widget data in Tk/Tkinter.
    """

    def clear_text_entry(self, text_entry: tkinter.Entry) -> None:
        """
        Clears a text entry widget and fills it with an empty string
        :param text_entry: The text entry to be cleared
        :return: void
        """
        text_entry.delete(0, tkinter.END)

    def clear_label_text(self, label: tkinter.Label) -> None:
        """
        Clears a label widget's text and fills it with an empty string
        :param label: The label to be cleared
        :return: void
        """
        label['text'] = ""

    # TODO Figure out progress bars in Tk
    def reset_percentage_progress_bar(self, percentage_progress_bar: tkinter.Label) -> None:
        """
        Resets a percentage-based progress bar to 0%
        :param percentage_progress_bar: the progress bar to be reset
        :return: void
        """
        percentage_progress_bar["value"] = 0.0

    def clear_primitive_combo_box(self, primitive_combo_box: ttk.Combobox) -> None:
        """
        Clears all entries of a primitive-type (str, int, etc.) storing combo box.
        :param primitive_combo_box: the combo box to be cleared
        :return: void
        """
        raise NotImplementedError("clear_primitive_combo_box not implemented")

    def clear_primitive_multi_list_box(self, primitive_multi_list_box: ttk.Treeview) -> None:
        """
        Clears all entries of a primitive-type (str, int, etc.) storing multi list box.
        :param primitive_multi_list_box: the multi list box to be cleared
        :return: void
        """
        primitive_multi_list_box.delete(*primitive_multi_list_box.get_children())

    def reset_check_box(self, check_box: tkinter.Checkbutton) -> None:
        """
        Resets a check box to be deselected
        :param check_box: the check box to be reset
        :return: void
        """
        raise NotImplementedError("reset_check_box not implemented")

    def reset_radio_button(self, radio_button: tkinter.Radiobutton) -> None:
        """
        Resets a radio button to be deselected
        :param radio_button: the radio button to be deselected
        """
        raise NotImplementedError("reset_radio_button not implemented")
