import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class main(Gtk.Window):
    def __init__(self):
        super().__init__(title="Test for boxes")

        # widgets
        self.button1 = Gtk.Button(label="Button1")
        self.button1.connect("clicked", self.onClick)

        self.button2 = Gtk.Button(label="Button2")
        self.button2.connect("clicked", self.onClick)

        self.titleLabel = Gtk.Label(label="Top Label")
        
        # boxes

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 10)
        self.hbox.pack_start(self.button1, True, True, 0)
        self.hbox.pack_start(self.button2, True, True, 0)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.vbox.pack_start(self.titleLabel, True, True, 0)
        self.vbox.pack_start(self.hbox, True, True, 0)


        
    def onClick():
        print("Button(s) pressed")

window = main()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
        