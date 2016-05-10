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

"""
The metadata is stored here. It can be used by any other module in this project this way, most
notably by the setup.py file
"""

project_name = "gfworks"
"""
The name of the project
"""

project_description = "A bot that interfaces with several different messenger services"
"""
A short description of the project
"""

version_number = "0.1.7"
"""
The current version of the program.
"""

development_status = "Development Status :: 1 - Planning"
"""
The current development status of the program
"""

project_url = "http://namibsun.net/namboy94/gfworks"
"""
A URL linking to the home page of the project, in this case a
self-hosted Gitlab page
"""

download_url = "http://gitlab.namibsun.net/namboy94/gfworks/repository/archive.zip?ref=master"
"""
A URL linking to the current source zip file.
"""

author_name = "Hermann Krumrey"
"""
The name(s) of the project author(s)
"""

author_email = "hermann@krumreyh.com"
"""
The email address(es) of the project author(s)
"""

license_type = "GNU GPL3"
"""
The project's license type
"""

python3_requirements = []
"""
Python 3 Python Packaging Index requirements
"""

python2_requirements = python3_requirements
"""
Python 2 Python Packaging Index requirements
"""

dependency_links=['https://git.gnome.org/browse/pygobject']
"""
Links to dependencies that are not packaged on pypi.
"""

scripts = []
"""
List of script files to be installed during installation
"""