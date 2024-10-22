import tkinter as tk
from tkinter import messagebox
import hashlib
import os
import sqlite3

# SQLite Database setup
DB_NAME = "users.db"
CREDENTIALS_FILE = "users.txt"


# Create users table if it doesn't exist
def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Add new user to the database
def add_user_to_db(email, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Email already exists
    finally:
        conn.close()


# Check if user exists in the database
def validate_user(email, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()

    if result is None:
        return False
    return result[0] == hash_password(password)


# Login Page Class
class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - PunaTel")
        self.root.geometry("400x300")

        title_label = tk.Label(self.root, text="PunaTel", font=("Arial", 24), fg="blue")
        title_label.pack(pady=20)

        username_label = tk.Label(self.root, text="Email:")
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        password_label = tk.Label(self.root, text="Password:")
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        login_button = tk.Button(self.root, text="Login", command=self.login_user)
        login_button.pack(pady=10)

        signup_button = tk.Button(self.root, text="Sign Up", command=self.open_signup_page)
        signup_button.pack(pady=5)

    def login_user(self):
        email = self.username_entry.get()
        password = self.password_entry.get()

        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required.")
            return

        if validate_user(email, password):
            messagebox.showinfo("Success", f"Welcome, {email}!")
            self.root.destroy()
            HomePage(tk.Toplevel(self.root), email)
        else:
            messagebox.showerror("Error", "Invalid email or password.")

    def open_signup_page(self):
        self.root.withdraw()  # Hide the root window
        SignUpPage(tk.Toplevel(self.root), self.root)


# Sign Up Page Class
class SignUpPage:
    def __init__(self, root, login_page_root):
        self.root = root
        self.login_page_root = login_page_root  # Reference to the login page root
        self.root.title("Sign Up - PunaTel")
        self.root.geometry("400x300")

        title_label = tk.Label(self.root, text="Create New Account", font=("Arial", 20), fg="green")
        title_label.pack(pady=20)

        email_label = tk.Label(self.root, text="Email:")
        email_label.pack(pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)

        password_label = tk.Label(self.root, text="Password:")
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        submit_button = tk.Button(self.root, text="Submit", command=self.create_account)
        submit_button.pack(pady=20)

    def create_account(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required.")
            return

        if add_user_to_db(email, password):
            messagebox.showinfo("Success", "Account created successfully!")
            self.root.destroy()  # Close the signup window
            self.login_page_root.deiconify()  # Show the login window again
        else:
            messagebox.showerror("Error", "User already exists.")


# Home Page Class
class HomePage:
    def __init__(self, root, username):
        self.root = root
        self.root.title("PunaTel - Home Page")
        self.root.geometry("400x300")

        welcome_label = tk.Label(self.root, text=f"Welcome, {username}!", font=("Arial", 16))
        welcome_label.pack(pady=20)

        logout_button = tk.Button(self.root, text="Logout", command=self.logout)
        logout_button.pack(pady=20)

    def logout(self):
        self.root.destroy()
        LoginPage(tk.Toplevel(self.root))


# Main Application
if __name__ == "__main__":
    initialize_db()  # Create the users table if it doesn't exist
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()
