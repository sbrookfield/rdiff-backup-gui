#!/usr/bin/python3

import configparser
from pip._internal import self_outdated_check

configfile = "rdiff-backup-gui.conf"
config = configparser.ConfigParser()
config.read(configfile)

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class NotePage(Gtk.Grid): # add name to title
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.label = Gtk.Label(label=self.name)
        self.add(self.label)
        builder = Gtk.Builder()
        builder.add_from_file('gtk/Notepage.glade')
        grid = builder.get_object('notepagegrid')
        window = builder.get_object('window')
        window.remove(grid)
        self.add(grid)
        
        backupnow = builder.get_object('backupnow')
        backupnow.connect('clicked', self.on_backupnow_clicked)
        self.sourcefolder = builder.get_object('sourcefolder')
        self.backupfolder = builder.get_object('backupfolder')
    
    def on_backupnow_clicked(self, button):
        dialog = Gtk.MessageDialog(
            transient_for=None,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Running backup command",
        )
        dialog.format_secondary_text(
            ( "Running Backup source " + str(self.sourcefolder.get_filename()) + " and backup " + str(self.backupfolder.get_filename()))
)
        dialog.run()
        dialog.destroy()
        
        
class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Gnome RDiff Backup Tool")
        #self.set_border_width(5)
        
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        
        self.notepages = {'newpage' : NotePage('newpage') }
        for key in self.notepages:
            self.notebook.append_page(self.notepages[key])


win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

with open('example.ini', 'w') as configfile:
    config.write(configfile)