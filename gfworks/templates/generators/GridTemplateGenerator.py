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

# imports
from typing import Dict
from gfworks.interfaces.GenericWindow import GenericWindow


class GridTemplateGenerator(object):
    """
    Class that handles imports of different gfworks grid templates to avoid import errors
    """

    # noinspection PyUnresolvedReferences
    @staticmethod
    def get_grid_templates() -> Dict[str, GenericWindow]:
        """
        Returns a dictionary of gfworks grid templates, with an identifier string to mark which
        template implements which framework

        :return: the dictionary of templates
        """
        templates = []

        try:
            from gfworks.templates.gtk3.Gtk3GridTemplate import Gtk3GridTemplate
            templates.append(Gtk3GridTemplate)
        except ImportError:
            pass

        try:
            from gfworks.templates.tk.TkGridTemplate import TkGridTemplate
            templates.append(TkGridTemplate)
        except ImportError:
            pass

        return templates
