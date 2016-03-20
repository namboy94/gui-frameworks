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


class GenericValueGetter(object):
    """
    Interface that defines the requirements for a GUI framework to read values from widgets.
    """

    @staticmethod
    def get_string_from_label(label):
        raise NotImplementedError()

    @staticmethod
    def get_string_from_text_entry(text_entry):
        raise NotImplementedError()

    @staticmethod
    def get_string_from_button(button):
        raise NotImplementedError()

    @staticmethod
    def get_boolean_from_check_box(check_box):
        raise NotImplementedError()

    @staticmethod
    def get_boolean_from_radio_button(radio_button):
        raise NotImplementedError()

    @staticmethod
    def get_float_percentage_from_progress_bar(progress_bar):
        raise NotImplementedError()

    @staticmethod
    def get_string_from_current_selected_combo_box_option(combo_box):
        raise NotImplementedError()

    @staticmethod
    def get_list_of_selected_elements_from_multi_list_box(multi_list_box):
        raise NotImplementedError()
