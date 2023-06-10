#!/usr/bin/env python3

# Import der benötigten Bibliotheken
import gi
gi.require_version('Gtk', '3.0')  # Erfordert die Gtk-Version 3.0
gi.require_version('AppIndicator3', '0.1')  # Erfordert die AppIndicator3-Version 0.1
from gi.repository import Gtk, AppIndicator3
import base64

# Funktion zum Ein- oder Ausschalten des Bildschirmschoners
def toggle_screensaver(widget):
    # Hier wird der Code zum Ein- oder Ausschalten des Bildschirmschoners eingefügt
    print("bla")  # Einfacher Ausdruck zum Testen, wird durch den eigentlichen Code ersetzt
    pass

# Funktion zum Erstellen des Menüs
def build_menu():
    menu = Gtk.Menu()

    # Menüelement zum Aktivieren/Deaktivieren des Bildschirmschoners
    screensaver_item = Gtk.CheckMenuItem('Screensaver aktivieren')
    screensaver_item.connect('activate', toggle_screensaver)  # Verknüpfung mit der Funktion zum Ein- oder Ausschalten des Bildschirmschoners
    menu.append(screensaver_item)

    # Menüelement zum Beenden des Programms
    quit_item = Gtk.MenuItem('Beenden')
    quit_item.connect('activate', Gtk.main_quit)  # Verknüpfung mit der Gtk-Funktion zum Beenden des Programms
    menu.append(quit_item)

    menu.show_all()
    return menu

# Hauptfunktion des Programms
def main():

     # Das Bild als Bytes im Code speichern
    image_data = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAABlJREFU\nOMtjYBhggC8AAxUAj1sKIPAPQBHFAKPCuBrxgAHgTgCGYpgCUEUGAMAYEpK4Xw6MwAAAAASUVORK5C\nYII='

    # Erstellen eines App-Indikators
    indicator = AppIndicator3.Indicator.new(
        'screensaver-indicator',
        '/home/michael/Repository/Teeinit/123.png',  # Pfad zum Symbolbild des Indikators
        AppIndicator3.IndicatorCategory.APPLICATION_STATUS
    )
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)  # Indikatorstatus auf aktiv setzen
    indicator.set_menu(build_menu())  # Menü des Indikators erstellen

    Gtk.main()  # Hauptschleife der Gtk-Anwendung starten

# Überprüfung, ob das Skript direkt ausgeführt wird
if __name__ == '__main__':
    main()  # Aufruf der Hauptfunktion