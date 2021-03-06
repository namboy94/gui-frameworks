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

from typing import List


class GenericValueGetter(object):
    """
    Interface that defines the requirements for a GUI framework to read values from widgets.
    """

    @staticmethod
    def get_string_from_label(label: object) -> str:
        """
        Returns the displayed string from a label
        :return: the label string
        """
        raise NotImplementedError("get_string_from_label not implemented")

    @staticmethod
    def get_string_from_text_entry(text_entry: object) -> str:
        """
        Returns the currently entered string from a text entry
        :return: the current text entered
        """
        raise NotImplementedError("get_string_from_text_entry not implemented")

    @staticmethod
    def get_string_from_button(button: object) -> str:
        """
        Returns the displayed string from a button
        :return: the button string
        """
        raise NotImplementedError("get_string_from_button not implemented")

    @staticmethod
    def get_boolean_from_check_box(check_box: object) -> bool:
        """
        Checks if a check box is currently selected and returns the value
        :return: True if the check box is selected, False otherwise
        """
        raise NotImplementedError("get_boolean_from_check_box not implemented")

    @staticmethod
    def get_boolean_from_radio_button(radio_button: object) -> bool:
        """
        Checks if a radio button is currently selected and returns the value
        :return: True if the radio button is selected, False otherwise
        """
        raise NotImplementedError("get_boolean_from_radio_button not implemented")

    @staticmethod
    def get_float_percentage_from_progress_bar(progress_bar: object) -> float:
        """
        Gets the current progress of a progress bar as a float value between 0.0 and 1.0
        :return: the current progress as a float
        """
        raise NotImplementedError("get_float_percentage_from_progress_bar not implemented")

    @staticmethod
    def get_string_from_current_selected_combo_box_option(combo_box: object) -> str:
        """
        Gets the currently selected string value of a combo box
        :return: the currently selected string
        """
        raise NotImplementedError("get_string_from_current_selected_combo_box not implemented")

    @staticmethod
    def get_list_of_selected_elements_from_multi_list_box(multi_list_box: object) -> List[object]:
        """
        Gets the currently selected element from a multi list box
        :return: the currently selected multi list box element as a tuple
        """
        raise NotImplementedError("get_list_of_selected_elements_from_multi_list_box not implemented")
