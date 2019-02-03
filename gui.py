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
        self.header = self.builder.get_object("header")
        if self.window != None or self.header != None:
            self.window.set_icon_from_file('128ico.png')
            self.header.get_parent().remove(self.header)
            self.window.set_titlebar(self.header)
            print(self.window.set_default_icon_from_file('128ico.png'))
            self.window.show_all()
        else:
            warn('No window and/or header found in glade file')
        
                
    def onDestroy(self, *args):
        Gtk.main_quit()

if __name__ == "__main__":
    GUI = gui()
    Gtk.main()