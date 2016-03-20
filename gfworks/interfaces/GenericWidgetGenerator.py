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


class GenericWidgetGenerator(object):
    """
    Interface that defines the requirements for a GUI framework to generate widgets.
    """

    def generate_label(self, label_text):
        raise NotImplementedError()

    def generate_image_label(self, image_path, width=None, height=None):
        raise NotImplementedError()

    def generate_button(self, button_text, command=None, args=None):
        raise NotImplementedError()

    def generate_text_entry(self, default_text, enter_command=None, enter_args=None):
        raise NotImplementedError()

    def generate_check_box(self, active=False):
        raise NotImplementedError()

    def generate_radio_button(self, radio_button_text):
        raise NotImplementedError()

    def generate_percentage_progress_bar(self, initial_percentage=0.0):
        raise NotImplementedError()

    def generate_string_combo_box(self, options_list):
        raise NotImplementedError()

    def generate_primitive_multi_list_box(self, options_dictionary_with_types):
        raise NotImplementedError()
