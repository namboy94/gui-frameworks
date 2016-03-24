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

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gfworks.interfaces.widgetdatamanipulators.GenericValueSetter import GenericValueSetter


class Gtk3ValueSetter(GenericValueSetter):
    """
    Implements methods to set values of widgets in Gtk3/GObject
    """

    @staticmethod
    def set_label_string(label: Gtk.Label, text: str) -> None:
        """
        Sets the displayed text of a label widget
        :param label: the label to be modified
        :param text: the text to be displayed
        :return: void
        """
        label.set_text(text)

    @staticmethod
    def set_text_entry_string(text_entry: Gtk.Entry, text: str) -> None:
        """
        Sets the current text of a text entry widget
        :param text_entry: the text entry widget to be modified
        :param text: the text to be entered into th widget
        :return: void
        """
        text_entry.set_text(text)

    @staticmethod
    def set_button_string(button: Gtk.Button, text: str) -> None:
        """
        Sets the displayed text of a button widget
        :param button: the button widget to be modified
        :param text: the text to be displayed
        :return: void
        """
        button.get_label().set_text(text)

    @staticmethod
    def set_check_box_boolean(check_box: Gtk.CheckButton, checked: bool) -> None:
        """
        Sets the state of a check box widget
        :param check_box: the check box widget to be modified
        :param checked: flag to determine if the check box should be activated or not:
                True: Selected, False: Deselected
        :return: void
        """
        check_box.set_active(checked)

    @staticmethod
    def set_radio_button_boolean(radio_button: Gtk.RadioButton, checked: bool) -> None:
        """
        Sets the state of a radio button widget
        :param radio_button: The radio button widget to be modified
        :param checked: flag to determine if the radio button should be activated or not:
                True: Selected, False: Deselected
        :return: void
        """
        radio_button.set_active(checked)

    @staticmethod
    def set_progress_bar_float_percentage(progress_bar: Gtk.ProgressBar, percentage: float) -> None:
        """
        Sets the completed percentage of a progress bar widget
        :param progress_bar: the progress bar widget to be modified
        :param percentage: the percentage to be displayed, represented by a
                float value between 0.0 and 1.0
        :return: void
        """
        progress_bar.set_fraction(percentage)

    @staticmethod
    def set_combo_box_string_options(combo_box: Gtk.ComboBox, string_options: list) -> None:
        """
        Sets a list of strings as the combo box options. This clears all previous entries!
        :param combo_box: the combo box widget to be modified
        :param string_options: the options to be displayed as a list of strings
        :return: void
        """
        combo_box.option_store.clear()
        for option in string_options:
            combo_box.option_store.append((option,))
        combo_box.set_active(0)

    @staticmethod
    def set_multi_list_box_elements_options(multi_list_box: Gtk.ScrolledWindow, list_of_elements: list) -> None:
        """
        Sets a list of elements(tuples) to be displayed by a multi list box.
        This clears the multi list box beforehand!
        :param multi_list_box: the multi list box widget to be manipulated
        :param list_of_elements: List of elements, which are themselves tuples of primitive
                data types.
        :return: void
        """
        multi_list_box.list_store.clear()
        for element in list_of_elements:
            multi_list_box.list_store.append(element)
