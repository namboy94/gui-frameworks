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

"""
The metadata is stored here. It can be used by any other module in this project this way, most
notably by the setup.py file
"""

project_name = "gfworks"
"""
The name of the project
"""

project_description = "A mutiple-gui-framework wrapper for python"
"""
A short description of the project
"""

version_number = "0.3.2"
"""
The current version of the program.
"""

development_status = "Development Status :: 2 - Pre-Alpha"
"""
The current development status of the program
"""

project_url = "http://gitlab.namibsun.net/namboy94/gfworks"
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

dependencies = ["pillow"]
"""
Python Packaging Index requirements
"""

dependency_links = ['https://git.gnome.org/browse/pygobject']
"""
Links to dependencies that are not packaged on pypi.
"""

audience = "Intended Audience :: Developers"
"""
The intended audience of this software
"""

environment = "Environment :: Other Environment"
"""
The intended environment in which the program will be used
"""

programming_languages = ['Programming Language :: Python :: 3',
                         'Programming Language :: Python :: 2']
"""
The programming language used in this project
"""

topic = "Topic :: Software Development :: User Interfaces"
"""
The broad subject/topic of the project
"""

language = "Natural Language :: English"
"""
The (default) language of this project
"""

compatible_os = "Operating System :: OS Independent"
"""
The Operating Systems on which the program can run
"""

license_identifier = "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
"""
The license used for this project
"""
