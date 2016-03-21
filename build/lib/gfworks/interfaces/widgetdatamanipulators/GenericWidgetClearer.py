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


class GenericValueClearer(object):
    """
    Interface that defines the requirements for a GUI framework to clear values from widgets.
    """

    def clear_text_entry(self, text_entry: object) -> None:
        """
        Clears a text entry widget and fills it with an empty string
        :param text_entry: The text entry to be cleared
        :return: void
        """
        raise NotImplementedError("clear_text_entry not implemented")

    def reset_percentage_progress_bar(self, percentage_progress_bar: object) -> None:
        """
        Resets a percentage-based progress bar to 0%
        :param percentage_progress_bar: the progress bar to be reset
        :return: void
        """
        raise NotImplementedError("reset_progress_bar not implemented")

    def clear_primitive_combo_box(self, primitive_combo_box: object) -> None:
        """
        Clears all entries of a primitive-type (str, int, etc.) storing combo box.
        :param primitive_combo_box: the combo box to be cleared
        :return: void
        """
        raise NotImplementedError("clear_primitive_combo_box not implemented")

    def clear_primitive_multi_list_box(self, primitive_multi_list_box: object) -> None:
        """
        Clears all entries of a primitive-type (str, int, etc.) storing multi list box.
        :param primitive_multi_list_box: the multi list box to be cleared
        :return: void
        """
        raise NotImplementedError("clear_primitive_multi_list_box not implemented")

    def reset_check_box(self, check_box: object) -> None:
        """
        Resets a check box to be deselected
        :param check_box: the check box to be reset
        :return: void
        """
        raise NotImplementedError("reset_check_box not implemented")

    def reset_radio_button(self, radio_button: object) -> None:
        """
        Resets a radio button to be deselected
        :param radio_button: the radio button to be deselected
        """
        raise NotImplementedError("reset_radio_button not implemented")
