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
import tkinter
from functools import partial
from tkinter import ttk

from gfworks.interfaces.generators.GenericWidgetGenerator import GenericWidgetGenerator


class TkWidgetGenerator(GenericWidgetGenerator, tkinter.Tk):
    """
    Implements the Widget Generating commands for Tk/Tkinter
    """

    def generate_label(self, label_text: str):
        """
        Generates a label widget that shows text
        :param label_text: The text to be displayed by the label
        :return: the label widget
        """
        label = tkinter.Label(self, text=label_text)
        return label

    def generate_image_label(self, image_path: str,
                             maintain_aspect_ratio: bool = True, width: int = None, height: int = None):
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
        # TODO Implement
        super().generate_image_label(image_path, maintain_aspect_ratio, width, height)

    def generate_button(self, button_text: str, command=None, args=None):
        """
        Generates a button widget that shows some text and may execute a command if pressed.
        :param button_text: The text to be displayed on the button
        :param command: the command to be executed when the button is pressed
        :param args: optional arguments for the executed method as a tuple
        :return: the button widget
        """
        button = tkinter.Button(self, text=button_text, command=partial(command, args))
        return button

    def generate_text_entry(self, default_text: str, enter_command=None, enter_args=None):
        """
        Generates a text entry widget that allows a user to enter text. It may also execute a
        command when it is in focus and the enter key is pressed.
        :param default_text: the text to be displayed per default.
        :param enter_command: the command to be executed when the enter key is pressed
        :param enter_args: Optional arguments for the enter command
        :return: the text entry widget
        """
        text_var = tkinter.StringVar(self, default_text)
        entry = tkinter.Entry(self, textvariable=text_var)
        entry.text_var = text_var
        if enter_command is not None:
            entry.bind('<Return>', partial(enter_command, enter_args))
        return entry

    def generate_check_box(self, combo_box_text: str, active: bool = False):
        """
        Generates a Check Box widget that allows selecting and deselecting options
        :param combo_box_text: The text to be displayed beside the combo box
        :param active: The starting state of the widget, default to False
        :return: the check box widget
        """
        number_var = tkinter.IntVar()
        check_button = tkinter.Checkbutton(self, text=combo_box_text, variable=number_var)
        check_button.number_var = number_var
        if active:
            check_button.select()
        return check_button

    def generate_radio_button(self, radio_button_text: str):
        """
        Generates a Radio Button which can be used for selecting and deselecting options
        :param radio_button_text: the text to be displayed with the radio_button
        :return: the radio button widget
        """
        # TODO Implement
        super().generate_radio_button(radio_button_text)

    def generate_percentage_progress_bar(self, initial_percentage: float = 0.0):
        """
        Generates a percentage-based progress bar
        :param initial_percentage: the initial percentage of the progress bar to
                be filled out at the start
        :return: the progress bar widget
        """
        # TODO implement
        super().generate_percentage_progress_bar(initial_percentage)

    def generate_string_combo_box(self, options_list: list(str)):
        """
        Generates a combo box comprising of string values
        :param options_list: list of strings that will be selectable options in the
                combo box
        :return: the combo box widget
        """
        combo_box = ttk.Combobox(self)
        combo_box['values'] = tuple(options_list)
        combo_box.current(0)
        combo_box.state(['readonly'])
        return combo_box

    def generate_primitive_multi_list_box(self, options_dictionary_with_types: dict(str)):
        """
        Generates a multi list box displaying primitive data types (str, int, float, etc.)
        Multiple elements can be selected
        :param options_dictionary_with_types: a dictionary containing the column titles and
                their types, combined with their position starting from 0 in a tuple.
                The form of the dictionary is: {title1: (position1, type1), title2: (position2, type2), ...}
        :return the multi list box widget
        """
        # TODO Find a better solution
        list_box = tkinter.Listbox(self, selectmode=tkinter.MULTIPLE)
        for item in options_dictionary_with_types:
            list_box.insert(tkinter.END, options_dictionary_with_types[item][1])
        return list_box
