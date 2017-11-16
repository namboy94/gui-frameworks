/*
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
*/
package main.java.net.namibsun.jfworks.interfaces;


/**
 * Abstract Class that defines how a window is initialized, run and closed
 * It offers a basic Constructor, and three methods to control the GUI control
 * flow.
 */
abstract class GenericWindow {

    /**
     * Constructor that defines a standardized method signature and calls the layOut()
     * method.
     * @param title The Title of the GUI Window
     * @param parent The parent of the GUI Window
     * @param hideParent If set to True, the parent window will be hidden
     */
    GenericWindow(String title, GenericWindow parent, boolean hideParent) {
        this.layOut();
    }

    /**
     * Handles the layout of the GUI Window
     */
    public abstract void layOut();

    /**
     * Starts the GUI
     */
    public abstract void start();

    /**
     * Forces the Gui to stop
     */
    public abstract void stop();

}

// Order:
// WidgetGenerator extends Framework implement WidgetGenerator
// -> Dialogshower
// => Threading
// -> Value Getter
// Setter
// Clearer
// __> Positioner