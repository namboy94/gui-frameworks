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
from setuptools import setup, find_packages


def readme():
    """
    Reads the readme file.
    :return: the readme file as a string
    """
    with open('README.md') as f:
        return f.read()


setup(name='gfworks',
      version='0.1.1',
      description='A cross-framework GUI interface',
      long_description=readme(),
      classifiers=['Development Status :: 1 - Planning',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Programming Language :: Python :: 3',
                   'Topic :: Software Development :: User Interfaces',
                   'Natural Language :: English',
                   'Operating System :: OS Independent'
                   ],
      url='http://gitlab.namibsun.net/namboy94/gfworks',
      author='Hermann Krumrey',
      author_email='hermann@krumreyh.com',
      license='GNU GPL3',
      packages=find_packages(),
      install_requires=[],
      dependency_links=['https://git.gnome.org/browse/pygobject'],
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=[],
      zip_safe=False)

# How to upload to pypi:
# python setup.py register sdist upload
