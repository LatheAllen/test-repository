from Tkinter import *
import tkMessageBox
from datetime import date
from calendar import monthrange
import sys
import os
import sqlite3
import os.path

WIDTH = 600
HEIGHT = 800
class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        #create and configure a frame
        container = Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, HomePage, UserPage, SettingsPage, SignInPage, EventEditor, customPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(SignInPage) #select initially displayed page
    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

class HomePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg = "#222831")
        #creating widgets

        jumpToStartPageButton = Button(self, text = "<",\
            font = ("Arial", 22), bd = 0, width = WIDTH/250, bg = "#222831", fg="white",\
            command = lambda : controller.show_frame(StartPage))

        header = Label(self, text = "Home", font = ("Arial", 26), bg = "#222831",\
            width = int(0.75*WIDTH), fg = "white")

        scrollBar = Scrollbar(self, bg = "green", orient = "vertical")

        calendar = Listbox(self,  bg = "#393e46", width = WIDTH, font = ("Arial", 16), fg = "white", height = 25, yscrollcommand = scrollBar.set)

        addEventButton = Button(self, text = "Add Event",\
            font = ("Arial", 22), bd = 0, bg = "#222831", fg = "white",\
            command = lambda : controller.show_frame(EventEditor))

        #put some contents into calendar
        calendar_information = {} #calendar will be dictionary of date : information
        with open("calendar.txt", "rt") as c:
            for line in c:
                line = line.strip()
                line = line.split("|")
                string = ""
                for i in range(1, len(line)-1):
                    string += "{}{}".format(line[i], " ")
                string+=line[len(line)-1] #this way there isn't an extra space at end of string
                calendar_information[line[0]] = string
            print calendar_information
        #we want the calendar to be able to display a few things:
            #dates
            dates = calendar_information.keys()
            dates.sort() #we want our dates to be in order
            #event descriptions
            descriptions = []
            #people associated with event
            people = []
            #for this we will have to look at the file staff.txt
            with open("staff.txt", "rt") as s:
                for line in s:
                    line = line.strip()
                    people.append(line)
            print people
            #since dates will be in order, we will also get descriptions in chronological order
            for x in range(0, len(dates)):
                #get the string associated with the date
                rawText = calendar_information[dates[x]]
                #find out when the actual description starts, as marked by an @ symbol
                descriptionStartIndex = rawText.index("@")
                #get just the description text
                actualDescription = rawText[descriptionStartIndex+1:len(rawText)]
                #add it to a list of descriptions to later match with the date
                descriptions.append(actualDescription)
            print dates
            print descriptions
            for i in range(len(dates)):
                calendarSize=calendar.size()
                #max character length for a line is 39 before it goes off page.
                if len("{}: {}".format(dates[i], descriptions[i])) >= 50:
                    firstLine = "{}: {}".format(dates[i], descriptions[i])
                    calendar.insert(END, firstLine[0:50])
                    calendar.insert(END, firstLine[50:len(firstLine)])
                else:
                    #if the date and the description combined are not long enough to cause
                    #the description to go off the screen, just insert them as are.
                    calendar.insert(END, "{}: {}".format(dates[i], descriptions[i]))
                    #now, on a new line, list all the people involved with that date
                associatedPeople = []
                for p in range(0, len(people)):
                    if people[p] in calendar_information[dates[p]]:
                        associatedPeople.append(people[p])
                for n in range(0, len(associatedPeople)):
                    if n == 0:
                        calendar.insert(END, "People: {}".format(associatedPeople[n]))
                    else:
                        calendar.insert(END, "{}{}".format(" "*13, associatedPeople[n]))
                calendar.insert(END, " ")
                #how many days until event listing
                #time of day (as in 3:00pm-6:00pm)
                #related personnel
            #packing widgets
        jumpToStartPageButton.pack(padx = 10, pady = 10, side = LEFT)
        header.pack(padx = 10, pady = 10, side = TOP)
        scrollBar.pack(side = RIGHT, fill = "y")
        calendar.pack(pady = 10)
        scrollBar.config( command = calendar.yview)
        addEventButton.pack(padx = 10, pady = 10)

class UserPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg = "#222831")
        #creating widgets
        jumpToStartPageButton = Button(self, text = "<",\
            font = ("Arial", 22), bd = 0, bg = "#222831", fg = "white",\
            command = lambda : controller.show_frame(StartPage))
        header = Label(self, text = "User", font = ("Arial", 26), bg = "#222831", fg = "white") #replace via text file at later point
        #packing widgets
        jumpToStartPageButton.pack(padx = 10, pady = 10, side = LEFT)
        header.pack(padx = 10, pady = 10, side = TOP)

class customPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg = "#222831")
        #creating widgets
        jumpToStartPageButton = Button(self, text = "<",\
            font = ("Arial", 22), bd = 0, bg = "#222831", fg = "white",\
            command = lambda : controller.show_frame(StartPage))
        header = Label(self, text = "Notice", font = ("Arial", 26), bg = "#222831", fg = "white") #replace via text file at later point
        #packing widgets
        jumpToStartPageButton.pack(padx = 10, pady = 10, side = LEFT)
        header.pack(padx = 10, pady = 10, side = TOP)

class SettingsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg = "#222831")
        def themeChange():
            pass
        #creating widgets
        jumpToStartPageButton = Button(self, text = "<",\
            font = ("Arial", 22), bd = 0,\
            command = lambda : controller.show_frame(StartPage))
        header = Label(self, text = "Settings", font = ("Arial", 26)) #replace via text file at later point
        themeButton = Button(self, text = "Switch to Light Theme", font = ("Arial", 22), bg = "#393e46", fg = "white", command = themeChange)
        theme = "dark"
        #packing widgets
        jumpToStartPageButton.pack(padx = 10, pady = 10, side = LEFT)
        header.pack(padx = 10, pady = 10, side = TOP)

class SignInPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg = "#222831")
        #used to update StartPage after login confirmation
        #sign in boxes and labels
        self.userNameEntryLabel = Label(self, text = "Username: ", bg = "#222831", fg = "white", font = ("Arial", 22))
        self.userNameEntry = Entry(self, bg = "#393e46", width = int(0.8*WIDTH), font = ("Arial", 20), fg = "white")
        self.passWordEntryLabel = Label(self, text = "Password: ", bg = "#222831", fg = "white", font = ("Arial", 22))
        self.passWordEntry = Entry(self, bg = "#393e46", width = int(0.8*WIDTH), font = ("Arial", 20), fg = "white", show = "*")
        signInButton = Button(self, text = "Sign-In",\
            anchor = W, width = (WIDTH - 400), font = ("Arial", 22),\
            bd = 0, bg = "#222831", fg = "white", activebackground = "#d65a31",
            activeforeground = "white",\
            command = self.validateCredentials)
        label = Label(self, text = "Sign-In", font = ("Arial", 26), bg = "#222831", fg = "white")
        label.pack(padx = 10, pady = 30)
        self.userNameEntryLabel.pack(padx=50, pady=10)
        self.userNameEntry.pack(padx=50, pady=10)
        self.passWordEntryLabel.pack(padx=50, pady=10)
        self.passWordEntry.pack(padx=50, pady=10)
        signInButton.pack(padx = 50, pady = 10)
    def validateCredentials(self):
                while True:
                        username = self.userNameEntry.get()
                        password = self.passWordEntry.get()

                        with sqlite3.connect("employee.db") as db:
                            cursor = db.cursor()
                        find_user = ("SELECT * FROM employees WHERE username = ? AND password = ?")
                        cursor.execute(find_user, [(username),(password)])
                        results = cursor.fetchall()
                        
                        if results:
                            for i in results:
                                App.show_frame(app, StartPage)
                            return("exit")
                        else:
                            return("Username and password not recognized")
                            

class StartPage(Frame):
    def __init__(self, parent, controller):

        Frame.__init__(self, parent, bg = "#222831")
        jumpToHomePageButton = Button(self, text = "Home",\
            anchor = W, width = (WIDTH - 400), font = ("Arial", 22),\
            bd = 0, bg = "#222831", fg = "white", activebackground = "#d65a31",
            activeforeground = "white",\
            command = lambda : controller.show_frame(HomePage))
        self.jumpToUserPageButton = Button(self, text = "Me",\
            anchor = W, width = (WIDTH - 400), font = ("Arial", 22),\
            bd = 0, bg = "#222831", fg = "white", activebackground = "#d65a31",\
            activeforeground = "white",\
            command = lambda : controller.show_frame(UserPage))
        jumpToSettingsPageButton = Button(self, text = "Settings",\
            anchor = W, width = (WIDTH - 400), font = ("Arial", 22),\
            bd = 0, bg = "#222831", fg = "white", activebackground = "#d65a31",\
            activeforeground = "white",\
            command = lambda : controller.show_frame(SettingsPage))
        label = Label(self, text = "Navigation", font = ("Arial", 26), bg = "#222831", fg = "white")
        label.pack(padx = 10, pady = 30)
        jumpToHomePageButton.pack(padx = 50, pady = 10)
        self.jumpToUserPageButton.pack(padx = 50, pady = 10)
        jumpToSettingsPageButton.pack(padx = 50, pady = 10)
    def jumpToUserPage(self):
        global user
        userpage.header.configure(text=user)
        App.show_frame(app, UserPage)

class EventEditor(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg = "#222831")
        #creating widgets
        jumpEventEditorToHomePageButton = Button(self, text = "<",\
            font = ("Arial", 22), bd = 0, bg = "#222831", fg = "white",\
            command = lambda : controller.show_frame(HomePage))

        header = Label(self, text = "Event Editor", font = ("Arial", 26), bg = "#222831", fg = "white")
        dateEntryLabel = Label(self, text = "Date (mm/dd)", font = ("Arial", 22), bg = "#222831", fg = "white")
        dateEntry = Entry(self, font = ("Arial", 22), bg = "#393e46", fg = "white")
        peopleSelectionLabel = Label(self, text = "People", font = ("Arial", 22), bg = "#222831", fg = "white")
        peopleSelection = Listbox(self, bg = "#393e46", width = 30,\
            font = ("Arial", 16), fg = "white", selectmode = MULTIPLE,\
            selectbackground = "orange")
        eventDescriptionEntryLabel = Label(self, text = "Event Description", font = ("Arial", 22), bg = "#222831", fg = "white")
        eventDescriptionEntry = Entry(self, font = ("Arial", 16), bg = "#393e46", fg = "white", width = 26)
        people = []

        #for this we will have to look at the file staff.txt
        with open("staff.txt", "rt") as s:
            for line in s:
                line = line.strip()
                people.append(line)
        for x in range(0, len(people)):
            peopleSelection.insert(END, people[x])

        def validateDate():
            months = ["0{}".format(x) for x in range(1, 10)]
            for x in range(0, 3):
                months.append("1{}".format(x))
            userDate = dateEntry.get()
            currentYear = date.today().year
            userDate = userDate.split("/")
            #the data the user gave us
            month = str(userDate[0])
            day = str(userDate[1])
            #there are 2 possibilities for the month:
                #month is correct
                    #correct if:
                        #month found in dictionary months
                #month is incorrect
                    #incorrect if not found in dictionary months
                        #lets consider some ways this can go wrong
                            #User entered a month that exists, but it is formatted wrong
                                #we can fix this by correcting their format
                                    #how can it be formatted wrong?
                                        #Could have forgotten to 0(number) as their month, say:
                                        #they put may as 5 instead of 05
                            #User entered a month that does not exist
                                #we cannot correct this, we will have to make them re-enter it
            #if the month is fine, we don't have to do anything, but if it is not:
            if not month in months:
                if len(month) == 1:
                    if month == "0":
                        print "Erroneous data, no 0th month"
                        month = "erroneous"
                    else:
                        month = "0{}".format(month)
                else:
                    if month[0] == "0":
                        if month[1] == "0":
                            print "Erroneous data, format is correct (mm) but there is no 0th month."
                            month = "erroneous"
                    elif month[0] == "1":
                        intMonth = int(month[1])
                        if intMonth > 2:
                            print "Erroneous data, format is correct (mm), but there are only 12 months (1{} is outside this)".format(str(intMonth))
                            month = "erroneous"
                    else:
                        print "Okay, you seriously messed up this time."
                        month = "erroneous"
            #okay now that our month should be formatted the right way, we can find out what amount of
            #days exist in that month for this year, this way we can prevent the user from putting in
            #a date that doesn't exist

            #monthrange doesn't accept "05," rather just 5 up until 10, 11, 12. So if it is the case that we are dealing with
            #january up until september, we will have to only pass in the 1st index of the month
            if not "erroneous" in month:
                if month[0] == "0":
                    daysInMonth = monthrange(currentYear, int(month[1]))[1]
                else:
                    daysInMonth = monthrange(currentYear, int(month))[1]
                print "There are {} days in the month {}".format(daysInMonth, month)

            #now let's see if the user put the date in the right way.
            #we also expect 00, 01, 02, etc. format, so we will have to redo this with them too.
            if not "erroneous" in month:
                if len(day) == 1:
                        if day == "0":
                            print "Erroneous data, no 0th day"
                            day = "erroneous"
                        else :
                            day = "0{}".format(day)
                else:
                    if day[0] == "0":
                        if day[1] == "0":
                            print "Erroneous data, format is correct (mm) but there is no 0th day."
                            day = "erroneous"
                    else:
                        if int(day) > daysInMonth:
                            print "There are not that many days in that month.\n\
                            The month {} has {} days.".format(month, daysInMonth)
                            day = "erroneous"
            if not "erroneous" in "{}/{}".format(month, day):
                eventDate = "{}/{}".format(month, day)
                print "{} is a valid date.".format(eventDate)
                return str(eventDate)
            else:
                return "invalid"

        def updateCalendar(event):
            with open("calendar.txt", "a") as u:
                u.write("\n{}".format(event))

        def submitEvent():
            date = validateDate()
            if date != "invalid":
                people = []
                for i in peopleSelection.curselection():
                    people.append(peopleSelection.get(i))
                eventDescription = eventDescriptionEntry.get()
                data = "{}|{}|".format(date, len(people))
                for p in range(0, len(people)):
                    data+="{}, ".format(people[p])
                data = data[:-2]
                data+="|@{}".format(eventDescription)
                print data
                updateCalendar(data)
                tkMessageBox.showinfo("Event Submitted", "Your event went through. Please restart the application to view it in the calendar.")
            else:
                print "Event erroneous, give user a popup."
        def restart():
            python = sys.executable
            os.execl(python, *sys.argv)
            app.mainloop()
            controller.show_frame(StartPage)
        submitEvent = Button(self, text = "Submit", font = ("Arial", 22),\
            bg = "#222831", fg = "white", command = submitEvent, bd = 0)
        restartButton = Button(self, text = "Restart", font = ("Arial", 22),\
            bg = "#222831", fg = "white", command = restart, bd = 0)

        #packing widgets
        jumpEventEditorToHomePageButton.pack(padx = 10, pady = 10, side = LEFT)
        header.pack(padx = 10, pady = 10, side = TOP)
        dateEntryLabel.pack(padx = 10, pady = 10)
        dateEntry.pack(padx = 10, pady = 10)
        eventDescriptionEntryLabel.pack(padx = 10, pady = 10)
        eventDescriptionEntry.pack(padx = 10, pady = 10)
        peopleSelectionLabel.pack(padx = 10, pady = 10)
        peopleSelection.pack(padx = 10, pady = 10)
        submitEvent.pack(padx = 10, pady = 10)
        restartButton.pack(padx = 10, pady = 10)





app = App()
app.geometry("{}x{}".format(WIDTH, HEIGHT))
app.title("haha subscribe.")
app.mainloop()


