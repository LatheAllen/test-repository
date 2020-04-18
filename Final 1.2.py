from Tkinter import *
currentPage = None
class Page(object):
	def __init__(self, title = "Page Title", bg = "grey"):
		self.title = title
		self.bg = bg

	@property
	def title(self):
		return self._title
	@title.setter
	def title(self, value):
		self._title = value
	@property
	def bg(self):
		return self._bg
	@bg.setter
	def bg(self, value):
		self._bg = value

class App(Frame):
	colorScheme = {\
	"background":"#23272a",\
	"foreground":"#2c2f33",\
	"foreground-bright":"#99aab5",\
	"accent":"#7289da",\
	"off-white":"#f9f9f9",\
	}
	def __init__(self, parent):
		Frame.__init__(self, parent)
	#make some pages
	def createPages(self):
		#it's not like there are going to be newly generated pages
		#as the app runs, so it's appropriate to just create some
		#predefined ones
		App.navigationPage = Page("Navigation", App.colorScheme["background"]) 
		App.omePage = Page("Home", App.colorScheme["background"])
		App.settingsPage = Page("Home", App.colorScheme["background"])
		App.personalPage = Page("Home", App.colorScheme["background"])
		App.currentPage = App.navigationPage
	def startGUI(self):
		root.geometry("{}x{}".format(WIDTH, HEIGHT))
		self.pack(fill=BOTH, expand = 1)
		#frames
		header = Frame(self, width = WIDTH)
		mainDisplay = Frame(self, width = WIDTH)
		#Header
		header.tkraise()
		App.backButton = Button(header, width = int(WIDTH/4), text = "<")
		App.headerText = Label(header, width = int(WIDTH - WIDTH/4), text = App.currentPage.title, bg = App.currentPage.bg)
		App.backButton.pack()
		App.headerText.pack()
		#main area
		mainDisplay.tkraise()
		App.jumpToHomeButton = Button(mainDisplay, text = "Home")
		App.jumpToUserButton = Button(mainDisplay, text = "User")
		App.jumpToSettingsButton = Button(mainDisplay, text = "Settings")
		App.jumpToHomeButton.pack()
		App.jumpToUserButton.pack()
		App.jumpToSettingsButton.pack()
	def setupGUI(self):
		root.geometry("{}x{}".format(WIDTH, HEIGHT))
		self.pack(fill = BOTH, expand = 1)
		header = Frame(self, width = WIDTH)
		mainDisplay = Frame(self, width = WIDTH)
		App.backButton = Button(header, width = int(WIDTH*0.25), text = "<")
		App.headerText = Label(header, width = int(WIDTH*0.75), text = App.currentPage.title)
		App.jumpToHomeButton = Button(mainDisplay, text = "Home")
		App.jumpToUserButton = Button(mainDisplay, text = "User")
		App.jumpToSettingsButton = Button(mainDisplay, text = "Settings")
		App.backButton.pack(side = RIGHT)
		App.headerText.pack(side = RIGHT, fill = X)
		App.headerText.configure(width = WIDTH)
		App.headerText.pack(fill = X)
		App.jumpToHomeButton.pack()
		App.jumpToUserButton.pack()
		App.jumpToSettingsButton.pack()

	def start(self):
		self.createPages()
		self.startGUI()



#===================================================
WIDTH = 600
HEIGHT = 800
root = Tk()
root.title("Home")
a = App(root)
a.start()
root.mainloop()