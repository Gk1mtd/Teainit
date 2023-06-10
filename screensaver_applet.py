#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')  # Requires Gtk version 3.0
gi.require_version('AppIndicator3', '0.1')  # Requires AppIndicator3 version 0.1
from gi.repository import Gtk, AppIndicator3
import subprocess

screensaver_enabled = False

def toggle_screensaver(widget):
    global screensaver_enabled

    if screensaver_enabled:
        # Set the screensaver delay to 15 minutes
        subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.session', 'idle-delay', '900'])
        screensaver_enabled = False
    else:
        # Set the screensaver delay to 0 (disabled)
        subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.session', 'idle-delay', '0'])
        screensaver_enabled = True

def build_menu():
    menu = Gtk.Menu()

    screensaver_item = Gtk.CheckMenuItem('Toggle Screensaver')
    screensaver_item.connect('activate', toggle_screensaver)  # Connect toggle_screensaver function to the menu item
    menu.append(screensaver_item)

    quit_item = Gtk.MenuItem('Quit')
    quit_item.connect('activate', Gtk.main_quit)  # Connect Gtk.main_quit function to the menu item
    menu.append(quit_item)

    menu.show_all()
    return menu

def main():
    image_data = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAABlJREFU\nOMtjYBhggC8AAxUAj1sKIPAPQBHFAKPCuBrxgAHgTgCGYpgCUEUGAMAYEpK4Xw6MwAAAAASUVORK5C\nYII='

    indicator = AppIndicator3.Indicator.new(
        'screensaver-indicator',
        '/home/michael/Repository/Teeinit/123.png',  # Path to the indicator's symbol image
        AppIndicator3.IndicatorCategory.APPLICATION_STATUS
    )
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)  # Set the indicator status to active
    indicator.set_menu(build_menu())  # Create the indicator's menu

    Gtk.main()  # Start the main Gtk event loop

if __name__ == '__main__':
    main()  # Call the main function if the script is executed directly
