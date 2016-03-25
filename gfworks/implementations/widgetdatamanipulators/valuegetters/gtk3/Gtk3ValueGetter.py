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

from gfworks.interfaces.widgetdatamanipulators.GenericValueGetter import GenericValueGetter


class Gtk3ValueGetter(Gtk.Window, GenericValueGetter):
    """
    Interface that defines the requirements for a GUI framework to read values from widgets.
    """

    @staticmethod
    def get_string_from_label(label: Gtk.Label) -> str:
        """
        Returns the displayed string from a label
        :return: the label string
        """
        return label.get_text()

    @staticmethod
    def get_string_from_text_entry(text_entry: Gtk.Entry) -> str:
        """
        Returns the currently entered string from a text entry
        :return: the current text entered
        """
        return text_entry.get_text()

    @staticmethod
    def get_string_from_button(button: Gtk.Button) -> str:
        """
        Returns the displayed string from a button
        :return: the button string
        """
        return button.get_label()

    @staticmethod
    def get_boolean_from_check_box(check_box: Gtk.CheckButton) -> bool:
        """
        Checks if a check box is currently selected and returns the value
        :return: True if the check box is selected, False otherwise
        """
        return check_box.get_active()

    @staticmethod
    def get_boolean_from_radio_button(radio_button: Gtk.RadioButton) -> bool:
        """
        Checks if a radio button is currently selected and returns the value
        :return: True if the radio button is selected, False otherwise
        """
        return radio_button.get_active()

    @staticmethod
    def get_float_percentage_from_progress_bar(progress_bar: Gtk.ProgressBar) -> float:
        """
        Gets the current progress of a progress bar as a float value between 0.0 and 1.0
        :return: the current progress as a float
        """
        return progress_bar.get_fraction()

    @staticmethod
    def get_string_from_current_selected_combo_box_option(combo_box: Gtk.ComboBox) -> str:
        """
        Gets the currently selected string value of a combo box
        :return: the currently selected string
        """
        combo_iter = combo_box.get_active_iter()
        if combo_iter is None:
            return None
        return combo_box.option_store.get(combo_iter, 0)[0]

    @staticmethod
    def get_list_of_selected_elements_from_multi_list_box(multi_list_box: Gtk.ScrolledWindow) -> list:
        """
        Gets the currently selected element from a multi list box
        :return: the currently selected multi list box element as a tuple
        """
        selected = []
        (model, path_list) = multi_list_box.tree_selection.get_selected_rows()
        for path in path_list:
            tree_iter = model.get_iter(path)
            i = 0
            element = ()
            added_all_element_components = False
            while not added_all_element_components:
                try:
                    element += (model.get_value(tree_iter, i),)
                except TypeError:
                    added_all_element_components = True
                i += 1
            selected.append(element)
        return selected
