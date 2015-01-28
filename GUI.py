#!/usr/bin/python
import pygtk
pygtk.require("2.0")
import gtk

class InvertedIndex:
	def __init__(self):
		interface = gtk.Builder()
		interface.add_from_file('Inverted_Index.glade')
		
		self.myLabel = interface.get_object("myLabel")
		interface.connect_signals(self)

	def on_mainWindow_destroy(self, widget):
		gtk.main_quit()

	def on_myButton_clicked(self, widget):
		self.myLabel.set_text("World!")

if __name__ == "__main__":
	InvertedIndex()
	gtk.main()
