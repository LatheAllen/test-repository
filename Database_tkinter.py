from Tkinter import *
# imports python image library
from PIL import ImageTk, Image
# imports python database
import sqlite3


root = Tk()
root.title('Database')
root.geometry("400x400")
# Databases

# Creates a database or connect to one
# Create a connection to database
connection = sqlite3.connect('employee.db')# in () pass name of database you want to create or connect to

# create a cursor to interact with database
c = connection.cursor()

### Create Table-- only used when creating a table
##c.execute("""CREATE TABLE employees(
##        first_name text,
##        last_name text,
##        username text,
##        password integer,
##        position text,
##        length_of_service integer,
##        salary integer)
##        """)



# creates and update function
def update():
    # connects to the database
    connection = sqlite3.connect('employee.db')
    # create a cursor
    c = connection.cursor()
    
    record_id = delete_box.get()
    c.execute(""" UPDATE employees SET
            first_name = :first_name,
            last_name= :last_name,
            username= :username,
            password = :password,
            position = :position,
            length_of_service= :length_of_service,
            salary = :salary

            WHERE oid = :oid""",
            {'first_name':first_name_editor.get(),
            'last_name':last_name_editor.get(),
            'username':username_editor.get(),
            'password':password_editor.get(),
            'position':position_editor.get(),
            'length_of_service':length_of_service_editor.get(),
            'salary':salary_editor.get(),
            'oid':record_id})
    

    # commit changes
    connection.commit()
    # close connection
    connection.close()
    #closes the box
    editor.destroy()
    
# create function to delete a record
def delete():
    # connects to the database
    connection = sqlite3.connect('employee.db')
    # create a cursor
    c = connection.cursor()
    c.execute("DELETE FROM employees WHERE oid= " + delete_box.get())
    
    # commit changes
    connection.commit()
    # close connection
    connection.close()
# create submit button
# create a cursor inside database and connect to database inside a function
def submit():
    # connects to the database
    connection = sqlite3.connect('employee.db')
    # create a cursor
    c = connection.cursor()
    # submit information into table in database
    # creates key value pairs for each column in the database table
    c.execute("INSERT INTO employees VALUES (:first_name, :last_name, :username, :password, :position, :length_of_service, :salary)",
                                            {'first_name':first_name.get(),
                                             'last_name':last_name.get(),
                                             'username':username.get(),
                                             'password':password.get(),
                                             'position':position.get(),
                                             'length_of_service':length_of_service.get(),
                                             'salary':salary.get()})
    
    # commit changes
    connection.commit()
    # close connection
    connection.close()
    
    
    # clear each of the text boxes when submit is hit
    first_name.delete(0,END)
    last_name.delete(0,END)
    username.delete(0,END)
    password.delete(0,END)
    position.delete(0,END)
    length_of_service.delete(0,END)
    salary.delete(0,END)

def query():
    # connects to the database
    connection = sqlite3.connect('employee.db')
    # create a cursor
    c = connection.cursor()
    # query the database
    # Ioid returns the primary key
    c.execute("SELECT *, oid FROM employees")
    # fetches all of the records, can only fetch some if you want
    records = c.fetchall()
    #print(records)
    # loop throught the results
    # print the results of the records in the data base
    # print the # that prints at the end of the record is the key value 
    print_records = ''
    for record in records:
##        print_records += str(record) +  "\n"
        print_records += str(record[0]) + " " + str(record[1])+ "\t" + str(record[7]) +"\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=14,column=0, columnspan=2)
    # commit changes
    connection.commit()
    # close connection
    connection.close()

# create edit function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title('Update A Record')
    editor.geometry("400x200")

    # connects to the database
    connection = sqlite3.connect('employee.db')
    # create a cursor
    c = connection.cursor()
    record_id = delete_box.get()
    # fills boxes with selected information to edit
    c.execute("SELECT * FROM employees WHERE oid = " + record_id)
    # fetches all of the records, can only fetch some if you want
    records = c.fetchall()

    # create global variables for text box names
    global first_name_editor
    global last_name_editor
    global username_editor
    global password_editor
    global position_editor
    global length_of_service_editor
    global salary_editor

    # creates the text boxes
    first_name_editor = Entry(editor, width = 30)
    first_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))

    last_name_editor = Entry(editor, width = 30)
    last_name_editor.grid(row=1, column=1)

    username_editor = Entry(editor, width = 30)
    username_editor.grid(row=2, column=1)

    password_editor = Entry(editor, width = 30)
    password_editor.grid(row=3, column=1)

    position_editor = Entry(editor, width = 30)
    position_editor.grid(row=4, column=1)

    length_of_service_editor = Entry(editor, width = 30)
    length_of_service_editor.grid(row=5, column=1)

    salary_editor = Entry(editor, width = 30)
    salary_editor.grid(row=6, column=1)

    # creates the labels for the above text boxes
    first_name_label = Label(editor, text="Employee's First Name")
    first_name_label.grid(row=0, column=0, pady=(10,0))

    last_name_label = Label(editor, text="Employee's Last Name")
    last_name_label.grid(row=1, column=0)

    username_label = Label(editor, text="Employee's Username")
    username_label.grid(row=2, column=0)

    password_label = Label(editor, text="Employee's Password")
    password_label.grid(row=3, column=0)

    position_label = Label(editor, text="Employee's Position")
    position_label.grid(row=4, column=0)

    length_of_service_label = Label(editor, text="Employee's Length of Time with Company")
    length_of_service_label.grid(row=5, column=0)

    salary_label = Label(editor, text="Employee's Salary Hourly")
    salary_label.grid(row=6, column=0)

    # loop throught the results
    for record in records:
        first_name_editor.insert(0,record[0])
        last_name_editor.insert(0,record[1])
        username_editor.insert(0,record[2])
        password_editor.insert(0,record[3])
        position_editor.insert(0,record[4])
        length_of_service_editor.insert(0,record[5])
        salary_editor.insert(0,record[6])
    
    # creates a save button
    save_btn = Button(editor, text="Save Record", command=update)
    save_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

# creates the text boxes
first_name = Entry(root, width = 30)
first_name.grid(row=0, column=1, padx=20, pady=(10,0))

last_name = Entry(root, width = 30)
last_name.grid(row=1, column=1)

username = Entry(root, width = 30)
username.grid(row=2, column=1)

password = Entry(root, width = 30)
password.grid(row=3, column=1)

position = Entry(root, width = 30)
position.grid(row=4, column=1)

length_of_service = Entry(root, width = 30)
length_of_service.grid(row=5, column=1)

salary = Entry(root, width = 30)
salary.grid(row=6, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=11, column=1, pady=5)

# creates the labels for the above text boxes
first_name_label = Label(root, text="Employee's First Name")
first_name_label.grid(row=0, column=0, pady=(10,0))

last_name_label = Label(root, text="Employee's Last Name")
last_name_label.grid(row=1, column=0)

username_label = Label(root, text="Employee's Username")
username_label.grid(row=2, column=0)

password_label = Label(root, text="Employee's Password")
password_label.grid(row=3, column=0)

position_label = Label(root, text="Employee's Position")
position_label.grid(row=4, column=0)

length_of_service_label = Label(root, text="Employee's Length of Time with Company")
length_of_service_label.grid(row=5, column=0)

salary_label = Label(root, text="Employee's Salary Hourly")
salary_label.grid(row=6, column=0)

delete_box_label = Label(root, text="Select ID Number")
delete_box_label.grid(row=11, column=0, pady=5)

# Create a submit button
submit_btn = Button(root, text="Add Record To Database", command = submit)
submit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=110)#stretches

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create an Update button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=145)


# any time a change is made to a database we need to commit those changes
connection.commit()
# when done commiting need to close connnection
connection.close()



root.mainloop()
