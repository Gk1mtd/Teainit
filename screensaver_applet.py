#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3
import subprocess

screensaver_enabled = False

def toggle_screensaver(widget):
    global screensaver_enabled

    if screensaver_enabled:
        subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.session', 'idle-delay', '900'])
        screensaver_enabled = False
    else:
        subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.session', 'idle-delay', '0'])
        screensaver_enabled = True

def build_menu():
    menu = Gtk.Menu()

    screensaver_item = Gtk.CheckMenuItem('Toggle Screensaver')
    screensaver_item.connect('activate', toggle_screensaver)
    menu.append(screensaver_item)

    quit_item = Gtk.MenuItem('Quit')
    quit_item.connect('activate', Gtk.main_quit)
    menu.append(quit_item)

    menu.show_all()
    return menu

def main():
    indicator = AppIndicator3.Indicator.new(
        'screensaver-indicator',
        '/home/michael/Repository/Teeinit/123.png',
        AppIndicator3.IndicatorCategory.APPLICATION_STATUS
    )
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())

    Gtk.main()

if __name__ == '__main__':
    main()
