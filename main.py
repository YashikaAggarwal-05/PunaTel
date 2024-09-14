from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'ericsson@gmail.com' and password == '123':
        messagebox.showinfo('Lessgoo', 'Welcome')
    else:
        messagebox.showinfo('OOPSS!!','Login failed')



tele = Tk()

tele.title('Punatel Login')
#tele.iconbitmap('logo.png')
tele.minsize(200,250)
tele.configure(background='pink')

icon = PhotoImage('D:/Personal_DOCS/Ericsson/logo.png')
img1 = Image.open('logo.png')
resize_img = img1.resize((200, 100))
img1 = ImageTk.PhotoImage(resize_img)
img_label = Label(tele, image = img1)
img_label.pack(pady=(40,20))

text_label = Label(tele, text='Punatel', fg='black', bg='pink')
text_label.pack()
text_label.config(font=('Babus neue', 50))

icon2 = PhotoImage('D:/Personal_DOCS/Ericsson/admin.png')
img2 = Image.open('admin.png')
resize_img2 = img2.resize((50, 50))
img2 = ImageTk.PhotoImage(resize_img2)
img2_label = Label(tele, image = img2)
img2_label.pack(pady=(40,20))

text_label2 = Label(tele, text='Admin Login', fg='black', bg='pink')
text_label2.pack()
text_label2.config(font=('Babus neue', 20))

admin_login = Button(tele, text='Admin Login', fg='black', bg='green', width=10, height=2, command=handle_login)
admin_login.pack(pady=(10,10))
admin_login.config(font=('Babus neue', 15))

aemail_label = Label(tele, text='Enter Email', fg='black', bg='pink' )
aemail_label.config(font=('Babus neue', 20))
aemail_label.pack(pady=(20,25))

aemail_input = Entry(tele, width=70)
aemail_input.pack(ipady=10, pady=(5,50))
#email_input.pack(ipadx=70)

apassword_label = Label(tele, text='Enter Password', fg='black', bg='pink' )
apassword_label.config(font=('Babus neue', 20))
apassword_label.pack(pady=(10,15))

apassword_input = Entry(tele, width=70)
apassword_input.pack(ipady=10, pady=(1,10))

icon3 = PhotoImage('D:/Personal_DOCS/Ericsson/user.png')
img3 = Image.open('user.png')
resize_img3 = img3.resize((50, 50))
img3 = ImageTk.PhotoImage(resize_img3)
img3_label = Label(tele, image = img3)
img3_label.pack(pady=(40,20))

user_login = Button(tele, text='User Login', fg='black', bg='green', width=10, height=2, command=handle_login)
user_login.pack(pady=(10,10))
user_login.config(font=('Babus neue', 15))

uemail_label = Label(tele, text='Enter Email', fg='black', bg='pink' )
uemail_label.config(font=('Babus neue', 20))
uemail_label.pack(pady=(20,25))

uemail_input = Entry(tele, width=70)
uemail_input.pack(ipady=10, pady=(5,50))
#email_input.pack(ipadx=70)

upassword_label = Label(tele, text='Enter Password', fg='black', bg='pink' )
upassword_label.config(font=('Babus neue', 20))
upassword_label.pack(pady=(10,15))

upassword_input = Entry(tele, width=70)
upassword_input.pack(ipady=10, pady=(1,10))

login_button =  Button(tele,text='Login now', fg='black', bg='Teal', width=20, height=2, command=handle_login)
login_button.config(font=('Babus neue', 15))
login_button.pack(pady=(20,25))


tele.mainloop()
