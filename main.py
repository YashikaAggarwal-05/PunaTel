from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# Admin login window
def open_admin_login():
    admin_window = Toplevel(tele)
    admin_window.title("Admin Login")
    admin_window.configure(background='pink')
    admin_window.geometry("500x400")

    # Welcome message for Admin
    welcome_label = Label(admin_window, text="Welcome to Admin Login", fg='black', bg='pink')
    welcome_label.config(font=('Babus neue', 25))
    welcome_label.pack(pady=(20, 25))

    # Email and password fields for Admin
    email_label = Label(admin_window, text='Enter Email', fg='black', bg='pink')
    email_label.config(font=('Babus neue', 20))
    email_label.pack(pady=(20, 25))

    email_input = Entry(admin_window, width=50)
    email_input.pack(ipady=10, pady=(5, 15))

    password_label = Label(admin_window, text='Enter Password', fg='black', bg='pink')
    password_label.config(font=('Babus neue', 20))
    password_label.pack(pady=(10, 15))

    password_input = Entry(admin_window, width=50, show="*")
    password_input.pack(ipady=10, pady=(5, 15))

    # Function to handle login logic
    def handle_login():
        email = email_input.get()
        password = password_input.get()

        if email == 'ericsson@gmail.com' and password == '123':
            messagebox.showinfo('Success', 'Login successful!')
        else:
            messagebox.showinfo('Error', 'Login failed!')

    # Add login button
    login_button = Button(admin_window, text="Login", command=handle_login, bg="green", fg="white")
    login_button.pack(pady=(20, 20))

# User login window
def open_user_login():
    user_window = Toplevel(tele)
    user_window.title("User Login")
    user_window.configure(background='pink')
    user_window.geometry("500x400")

    # Welcome message for User
    welcome_label = Label(user_window, text="Welcome to User Login Page", fg='black', bg='pink')
    welcome_label.config(font=('Babus neue', 25))
    welcome_label.pack(pady=(20, 25))

    # Email and password fields for User
    email_label = Label(user_window, text='Enter Email', fg='black', bg='pink')
    email_label.config(font=('Babus neue', 20))
    email_label.pack(pady=(20, 25))

    email_input = Entry(user_window, width=50)
    email_input.pack(ipady=10, pady=(5, 15))

    password_label = Label(user_window, text='Enter Password', fg='black', bg='pink')
    password_label.config(font=('Babus neue', 20))
    password_label.pack(pady=(10, 15))

    password_input = Entry(user_window, width=50, show="*")
    password_input.pack(ipady=10, pady=(5, 15))

    # Function to handle login logic
    def handle_login():
        email = email_input.get()
        password = password_input.get()

        if email == 'user@gmail.com' and password == 'abc':
            messagebox.showinfo('Success', 'Login successful!')
        else:
            messagebox.showinfo('Error', 'Login failed!')

    # Add login button
    login_button = Button(user_window, text="Login", command=handle_login, bg="green", fg="white")
    login_button.pack(pady=(20, 20))

# Main window
tele = Tk()
tele.title('Punatel Login')
tele.minsize(200, 250)
tele.configure(background='pink')

# Title and logo
img1 = Image.open('logo.png')
resize_img = img1.resize((200, 100))
img1 = ImageTk.PhotoImage(resize_img)
img_label = Label(tele, image=img1)
img_label.pack(pady=(40, 20))

text_label = Label(tele, text='Punatel', fg='black', bg='pink')
text_label.pack()
text_label.config(font=('Babus neue', 50))

# Frame for buttons and icons
button_frame = Frame(tele, bg='pink')
button_frame.pack(pady=(20, 20))

# Admin login icon and button
admin_frame = Frame(button_frame, bg='pink')
admin_frame.grid(row=0, column=0, padx=20)

img2 = Image.open('admin.png')
resize_img2 = img2.resize((50, 50))
img2 = ImageTk.PhotoImage(resize_img2)
img2_label = Label(admin_frame, image=img2, bg='pink')
img2_label.pack(pady=(10, 5))

admin_login = Button(admin_frame, text='Admin Login', fg='black', bg='green', width=15, height=2, command=open_admin_login)
admin_login.pack()
admin_login.config(font=('Babus neue', 15))

# User login icon and button
user_frame = Frame(button_frame, bg='pink')
user_frame.grid(row=0, column=1, padx=20)

img3 = Image.open('user.png')
resize_img3 = img3.resize((50, 50))
img3 = ImageTk.PhotoImage(resize_img3)
img3_label = Label(user_frame, image=img3, bg='pink')
img3_label.pack(pady=(10, 5))

user_login = Button(user_frame, text='User Login', fg='black', bg='green', width=15, height=2, command=open_user_login)
user_login.pack()
user_login.config(font=('Babus neue', 15))

tele.mainloop()
