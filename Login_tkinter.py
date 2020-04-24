from Tkinter import *
import ttk

# from --insert project name-- import *
# I think the above is how you request the login for your program

class login:
    user = 'admin'
    passw = 'admin'

    def __init__(self, root):
        # sets and makes screen
        self.root = root
        self.root.title('Login Screen')
        
        # makes Username box
        Label(text = 'Username ', font ='Times 15').grid(row=1,column=1,pady=20)
        self.username = Entry()
        self.username.grid(row=1, column=2, columnspan=10)
        
        # makes Password box
        Label(text = 'Password ', font='Times 15').grid(row=2,column=1,pady=10)
        self.password = Entry(show='*')
        self.password.grid(row=2, column=2, columnspan=10)

        #
        ttk.Button(text='Login', command=self.login_user).grid(row=3,column=2)

    def login_user(self):
        #Checks to see if the Username and Password are correct
        # If it is correct this will verify and start our app
        if self.username.get() == self.user and self.password.get() == self.passw:
            root.destroy()
            newroot = Tk()
            # This is a class in the project that it would open
            application = App(newroot)
            # this would start my widget
            application.mainloop()
        # If it it is incorrect it will give an error message
        else:
            self.message = Label(text = 'Username or Password Incorrect. Please Try Again!', fg= 'Red')
            self.message.grid(row=6, column=2)
if __name__ == '__main__':

    root = Tk()
    root.geometry('425x225')
    application = login(root)
    root.mainloop()
