import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handle:
    def onClick(*args):
        print("You clicked a button somewhere")
    def destroy(*args):
        print("Exited")
        Gtk.main_quit()

builder = Gtk.Builder()
builder.add_from_file('gui.glade')
builder.connect_signals(Handle())

window = builder.get_object("main window")
window.show_all()

Gtk.main()