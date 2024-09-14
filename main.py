from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox







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
