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


class GenericValueSetter(object):
    """
    Interface that defines the requirements for a GUI framework to write values to widgets.
    """

    @staticmethod
    def set_label_string(label: object, text: str) -> None:
        """
        Sets the displayed text of a label widget
        :param label: the label to be modified
        :param text: the text to be displayed
        :return: void
        """
        raise NotImplementedError("set_label_string not implemented")

    @staticmethod
    def set_text_entry_string(text_entry: object, text: str) -> None:
        """
        Sets the current text of a text entry widget
        :param text_entry: the text entry widget to be modified
        :param text: the text to be entered into th widget
        :return: void
        """
        raise NotImplementedError("set_text_entry_string not implemented")

    @staticmethod
    def set_button_string(button: object, text: str) -> None:
        """
        Sets the displayed text of a button widget
        :param button: the button widget to be modified
        :param text: the text to be displayed
        :return: void
        """
        raise NotImplementedError("set_button_string not implemented")

    @staticmethod
    def set_check_box_boolean(check_box: object, checked: bool) -> None:
        """
        Sets the state of a check box widget
        :param check_box: the check box widget to be modified
        :param checked: flag to determine if the check box should be activated or not:
                True: Selected, False: Deselected
        :return: void
        """
        raise NotImplementedError("set_check_box_boolean not implemented")

    @staticmethod
    def set_radio_button_boolean(radio_button: object, checked: bool) -> None:
        """
        Sets the state of a radio button widget
        :param radio_button: The radio button widget to be modified
        :param checked: flag to determine if the radio button should be activated or not:
                True: Selected, False: Deselected
        :return: void
        """
        raise NotImplementedError("set_radio_button_boolean not implemented")

    @staticmethod
    def set_progress_bar_float_percentage(progress_bar: object, percentage: float) -> None:
        """
        Sets the completed percentage of a progress bar widget
        :param progress_bar: the progress bar widget to be modified
        :param percentage: the percentage to be displayed, represented by a
                float value between 0.0 and 1.0
        :return: void
        """
        raise NotImplementedError("set_progress_bar_float_percentage not implemented")

    @staticmethod
    def set_string_combo_box_string_options(combo_box: object, string_options: List[str]) -> None:
        """
        Sets a list of strings as the combo box options. This clears all previous entries!
        :param combo_box: the combo box widget to be modified
        :param string_options: the options to be displayed as a list of strings
        :return: void
        """
        raise NotImplementedError("set_combo_box_string_options not implemented")

    @staticmethod
    def set_primitive_multi_list_box_elements(multi_list_box: object, list_of_elements: List[tuple]) -> None:
        """
        Sets a list of elements(tuples) to be displayed by a multi list box.
        This clears the multi list box beforehand!
        :param multi_list_box: the multi list box widget to be manipulated
        :param list_of_elements: List of elements, which are themselves tuples of primitive
                data types.
        :return: void
        """
        raise NotImplementedError("set_multi_list_box_elements_options not implemented")

    @staticmethod
    def add_primitive_multi_list_box_element(multi_list_box: object, element: tuple) -> None:
        """
        Adds an element to the end of a multi list box displaying primitive types
        :param multi_list_box: the multi list box widget to be manipulated
        :param element: The element to be added
        :return: void
        """
        raise NotImplementedError("set_multi_list_box_elements_options not implemented")
