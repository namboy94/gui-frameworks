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

from threading import Thread
from typing import Tuple


class Threading(object):
    """
    Interface that defines the requirements for a GUI framework to use multiple threads correctly
    """

    @staticmethod
    def run_thread_in_parallel(target: callable, args: Tuple[object] = None, daemon: bool = False) -> Thread:
        """
        Runs a thread in parallel to the GUI main loop
        :param target: The command to be executed
        :param args: Optional arguments for the command
        :param daemon: Can be set to true to run this thread as a daemon
        :return: The created Thread
        """
        raise NotImplementedError("run_threads_in_parallel not implemented")

    @staticmethod
    def run_sensitive_thread_in_parallel(target: callable, args: Tuple[object] = None,
                                         insensitive_target: callable = None, insensitive_args: Tuple[object] = None,
                                         daemon: bool = False) -> Thread:
        """
        Runs a thread in parallel to the GUI main loop which may interfere with the actual main loop
        by changing widget elements.
        :param target: The command to be executed
        :param args: Optional arguments for the command
        :param insensitive_target: Command that is executed before the sensitive command
        :param insensitive_args: Optional arguments for the insensitive target
        :param daemon: Can be set to true to run this thread as a daemon
        :return: The created Thread
        """
        raise NotImplementedError("run_sensitive_thread_in_parallel not implemented")

    @staticmethod
    def run_thread_safe(target: callable, args: Tuple[object] = None) -> None:
        """
        Runs a command in a thread-safe manner, avoiding memory errors
        :param target: The command to be executed
        :param args: Optional arguments for the command
        :return: void
        """
        raise NotImplementedError("run_thread_safe not implemented")
