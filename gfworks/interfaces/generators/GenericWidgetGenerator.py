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

from typing import List, Dict, Tuple


class GenericWidgetGenerator(object):
    """
    Interface that defines the requirements for a GUI framework to generate widgets.
    """

    def generate_label(self, label_text: str) -> object:
        """
        Generates a label widget that shows text
        :param label_text: The text to be displayed by the label
        :return: the label widget
        """
        raise NotImplementedError("generate_label not implemented")

    def generate_image_label(self, image_path: str,
                             maintain_aspect_ratio: bool = True, width: int = None, height: int = None) -> object:
        """
        Generates an image label that shows an image
        :param image_path: The path to the file to be displayed
        :param maintain_aspect_ratio: Flag to define if the aspect ratio of the image should
                stay the same if the image is scaled
        :param width: The desired width of the image label
        :param height: The desired height of the image label
        Note: if width and height are not filled in, the actual size of the image
        will be displayed, if only one is defined, the image will be scaled accordingly according
        to the maintain_aspect_ratio flag
        :return: the image label widget
        """
        raise NotImplementedError("generate_image_label not implemented")

    def generate_button(self, button_text: str, command: callable = None, args: Tuple[object] = None) -> object:
        """
        Generates a button widget that shows some text and may execute a command if pressed.
        :param button_text: The text to be displayed on the button
        :param command: the command to be executed when the button is pressed
        :param args: optional arguments for the executed method as a tuple
        :return: the button widget
        """
        raise NotImplementedError("generate_button not implemented")

    def generate_text_entry(self, default_text: str, enter_command: callable = None, enter_args: Tuple[object] = None,
                            on_changed_command: callable = None, on_changed_args: Tuple[object] = None) -> object:
        """
        Generates a text entry widget that allows a user to enter text. It may also execute a
        command when it is in focus and the enter key is pressed.
        :param default_text: the text to be displayed per default.
        :param enter_command: the command to be executed when the enter key is pressed
        :param enter_args: Optional arguments for the enter command
        :param on_changed_command: the command to be executed when the content of the entry changes
        :param on_changed_args: Optional arguments for the on changed command
        :return: the text entry widget
        """
        raise NotImplementedError("generate_text_entry not implemented")

    def generate_password_entry(self, enter_command: callable = None, enter_args: Tuple[object] = None) -> object:
        """
        Generates a password entry widget that allows a user to enter a password while the input is obfuscated
        :param enter_command: a command to be run when the entry is selected and the Enter/Return key is pressed.
        :param enter_args: optional arguments for the enter_command
        :return: the password entry
        """
        raise NotImplementedError("generate_password_entry not implemented")

    def generate_check_box(self, combo_box_text: str, active: bool = False) -> object:
        """
        Generates a Check Box widget that allows selecting and deselecting options
        :param combo_box_text: The text to be displayed beside the combo box
        :param active: The starting state of the widget, default to False
        :return: the check box widget
        """
        raise NotImplementedError("generate_check_box not implemented")

    def generate_radio_button(self, radio_button_text: str) -> object:
        """
        Generates a Radio Button which can be used for selecting and deselecting options
        :param radio_button_text: the text to be displayed with the radio_button
        :return: the radio button widget
        """
        raise NotImplementedError("generate_radio_button not implemented")

    def generate_percentage_progress_bar(self, initial_percentage: float = 0.0) -> object:
        """
        Generates a percentage-based progress bar
        :param initial_percentage: the initial percentage of the progress bar to
                be filled out at the start
        :return: the progress bar widget
        """
        raise NotImplementedError("generate_percentage_progress_bar not implemented")

    # noinspection PyTypeChecker
    def generate_string_combo_box(self, options_list: List[str]) -> object:
        """
        Generates a combo box comprising of string values
        :param options_list: list of strings that will be selectable options in the
                combo box
        :return: the combo box widget
        """
        raise NotImplementedError("generate_string_combo_box not implemented")

    def generate_primitive_multi_column_list_box(self, options_dictionary_with_types: Dict[str, Tuple[int, type]],
                                                 multi_selectable: bool = True) -> object:
        """
        Generates a multi list box displaying primitive data types (str, int, float, etc.)
        Multiple elements can be selected
        :param options_dictionary_with_types: a dictionary containing the column titles and
                their types, combined with their position starting from 0 in a tuple.
                The form of the dictionary is: {title1: (position1, type1), title2: (position2, type2), ...}
        :param multi_selectable: Flag that defines if more than one element may be selected at any
                given time.
        :return the multi list box widget
        """
        raise NotImplementedError("generate_primitive_multi_list_box not implemented")
