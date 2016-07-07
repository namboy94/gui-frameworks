"""
LICENSE:
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
LICENSE
"""

from threading import Thread
from typing import Tuple
from gi.repository import GLib, GObject


class Gtk3Threading(object):
    """
    Implement threading in GTK 3/GObject
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
        if args is None:
            thread = Thread(target=target)
        else:
            thread = Thread(target=target, args=args)
        thread.daemon = daemon
        thread.start()
        return thread

    @staticmethod
    def run_sensitive_thread_in_parallel(target: callable, args: Tuple[object] = None,
                                         insensitive_target: callable = None, insensitive_args: Tuple[object] = None,
                                         daemon: bool = False) \
            -> Thread:
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
        GObject.threads_init()

        def called_thread():
            """
            The safe thread to be called
            """
            if insensitive_target is not None:
                if insensitive_args is not None:
                    insensitive_target(insensitive_args)
                else:
                    insensitive_target()

            def sensitive_thread():
                """
                The sensitive part of the thread to be called
                """
                if args is None:
                    target()
                else:
                    # noinspection PyArgumentList
                    target(*args)

            GLib.idle_add(sensitive_thread)

        thread = Thread(target=called_thread)
        thread.daemon = daemon
        thread.start()
        return thread

    @staticmethod
    def run_thread_safe(target: callable, args: Tuple[object] = None) -> None:
        """
        Runs a command in a thread-safe manner, avoiding memory errors
        :param target: The command to be executed
        :param args: Optional arguments for the command
        :return: void
        """
        def safe_thread():
            if args is not None:
                # noinspection PyArgumentList
                target(*args)
            else:
                target()

        GLib.idle_add(safe_thread)
