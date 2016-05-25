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
import tkinter.font as tk_font
from tkinter import ttk
from functools import partial
from PIL import Image, ImageTk
from typing import List, Dict, Tuple

from gfworks.interfaces.generators.GenericWidgetGenerator import GenericWidgetGenerator


class TkWidgetGenerator(GenericWidgetGenerator, tkinter.Toplevel):
    """
    Implements the Widget Generating commands for Tk/Tkinter
    """

    def generate_label(self, label_text: str) -> tkinter.Label:
        """
        Generates a label widget that shows text
        :param label_text: The text to be displayed by the label
        :return: the label widget
        """
        label = tkinter.Label(self, text=label_text)
        return label

    def generate_image_label(self, image_path: str, maintain_aspect_ratio: bool = True,
                             width: int = None, height: int = None) -> tkinter.Label:
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
        image = Image.open(image_path)
        if width is not None or height is not None:
            if maintain_aspect_ratio:
                image.thumbnail((width, height), Image.ANTIALIAS)
            else:
                image.resize((width, height), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        image_label = tkinter.Label(self, image=image)
        image_label.image_reference = image
        return image_label

    def generate_button(self, button_text: str, command: callable = None, args: Tuple[object] = None) -> tkinter.Button:
        """
        Generates a button widget that shows some text and may execute a command if pressed.
        :param button_text: The text to be displayed on the button
        :param command: the command to be executed when the button is pressed
        :param args: optional arguments for the executed method as a tuple
        :return: the button widget
        """
        if command is not None:
            cmd_args = (object,)
            if args is not None:
                try:
                    cmd_args += args
                except TypeError:
                    cmd_args += (args,)
            button = tkinter.Button(self, text=button_text, command=partial(command, *cmd_args))
        else:
            button = tkinter.Button(self, text=button_text)
        return button

    def generate_text_entry(self, default_text: str, enter_command: callable = None, enter_args: Tuple[object] = None,
                            on_changed_command: callable = None, on_changed_args: Tuple[object] = None)\
            -> tkinter.Entry:
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
        text_var = tkinter.StringVar(self, default_text)
        entry = tkinter.Entry(self, textvariable=text_var)
        entry.text_var = text_var
        if enter_command is not None:
            if enter_args is not None:
                # noinspection PyArgumentList
                entry.bind('<Return>', partial(enter_command, *enter_args))
            else:
                entry.bind('<Return>', enter_command)

        if on_changed_command is not None:
            on_changed_command_with_args = on_changed_command
            if on_changed_args:
                on_changed_command_with_args = partial(on_changed_command, on_changed_args)
            text_var.trace("w", lambda name, index, mode, sv=text_var: on_changed_command_with_args(sv))
        return entry

    def generate_password_entry(self, enter_command: callable = None, enter_args: Tuple[object] = None) -> object:
        """
        Generates a password entry widget that allows a user to enter a password while the input is obfuscated
        :param enter_command: a command to be run when the entry is selected and the Enter/Return key is pressed.
        :param enter_args: optional arguments for the enter_command
        :return: the password entry
        """
        text_var = tkinter.StringVar(self, "")
        entry = tkinter.Entry(self, textvariable=text_var, show="*")
        entry.text_var = text_var
        if enter_command is not None:
            if enter_args is not None:
                # noinspection PyArgumentList
                entry.bind('<Return>', partial(enter_command, *enter_args))
            else:
                entry.bind('<Return>', enter_command)
        return entry

    def generate_check_box(self, combo_box_text: str, active: bool = False) -> tkinter.Checkbutton:
        """
        Generates a Check Box widget that allows selecting and deselecting options
        :param combo_box_text: The text to be displayed beside the combo box
        :param active: The starting state of the widget, default to False
        :return: the check box widget
        """
        bool_var = tkinter.BooleanVar()

        def toggle():
            """
            Callback method that toggles the value of the variable associated with the checkbox

            :return: None
            """
            bool_var.set(not bool_var.get())

        check_button = tkinter.Checkbutton(self, text=combo_box_text, variable=bool_var, command=toggle)
        check_button.bool_var = bool_var

        if active:
            check_button.select()
            bool_var.set(True)
        return check_button

    def generate_radio_button(self, radio_button_text: str) -> tkinter.Radiobutton:
        """
        Generates a Radio Button which can be used for selecting and deselecting options
        :param radio_button_text: the text to be displayed with the radio_button
        :return: the radio button widget
        """
        # TODO Implement
        super().generate_radio_button(radio_button_text)

    def generate_percentage_progress_bar(self, initial_percentage: float = 0.0) -> ttk.Progressbar:
        """
        Generates a percentage-based progress bar
        :param initial_percentage: the initial percentage of the progress bar to
                be filled out at the start
        :return: the progress bar widget
        """
        progress_bar = ttk.Progressbar(self, value=int(initial_percentage * 100.0), orient="horizontal")
        return progress_bar

    # noinspection PyTypeChecker
    def generate_string_combo_box(self, options_list: List[str]) -> ttk.Combobox:
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

    def generate_primitive_multi_column_list_box(self, options_dictionary_with_types: Dict[str, Tuple[int, type]],
                                                 multi_selectable: bool = True) -> ttk.Treeview:
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
        def sortby(treea, col, descending):
            data = [(treea.set(child, col), child) for child in tree.get_children('')]
            data.sort(reverse=descending)
            for ix, item in enumerate(data):
                treea.move(item[1], '', ix)
            treea.heading(col, command=lambda column=col: sortby(treea, column, int(not descending)))

        types = ()
        titles = []
        priority = 0

        while len(titles) < len(options_dictionary_with_types):
            for title in options_dictionary_with_types:
                if options_dictionary_with_types[title][0] == priority:
                    titles.append(title)
                    types += (options_dictionary_with_types[title][1],)
                    priority += 1

        tree = ttk.Treeview(self, columns=titles, show="headings")
        vertical_scroll_bar = ttk.Scrollbar(orient="vertical", command=tree.yview)
        horizontal_scroll_bar = ttk.Scrollbar(orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vertical_scroll_bar.set, xscrollcommand=horizontal_scroll_bar.set)

        for title in titles:
            tree.heading(title, text=title, command=lambda c=title: sortby(tree, c, 0))
            tree.column(title, width=tk_font.Font().measure(title))

        tree.types = types

        return tree
