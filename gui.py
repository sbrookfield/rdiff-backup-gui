#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class gui:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gtk/main.glade")
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("MainWindow")
        self.window.show_all()
    def onDestroy(self, *args):
        Gtk.main_quit()

if __name__ == "__main__":
    GUI = gui()
    Gtk.main()