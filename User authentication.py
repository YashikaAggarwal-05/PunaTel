import tkinter as tk
from tkinter import messagebox
import hashlib
import os

# Path to store user credentials
CREDENTIALS_FILE = "users.txt"

# Function to hash the password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to read users from the credentials file
def load_users():
    if not os.path.exists(CREDENTIALS_FILE):
        return {}

    users = {}
    with open(CREDENTIALS_FILE, "r") as f:
        for line in f:
            username, password_hash = line.strip().split(",")
            users[username] = password_hash
    return users

# Function to save a new user to the credentials file
def save_user(username, password_hash):
    with open(CREDENTIALS_FILE, "a") as f:
        f.write(f"{username},{password_hash}\n")

# Registration Page Class
class RegisterPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Register - PunaTel")
        self.root.geometry("300x250")

        # Labels and Input Fields
        username_label = tk.Label(self.root, text="Username:")
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        password_label = tk.Label(self.root, text="Password:")
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        register_button = tk.Button(self.root, text="Register", command=self.register_user)
        register_button.pack(pady=10)

        # Already have an account?
        login_button = tk.Button(self.root, text="Already have an account? Login", command=self.go_to_login)
        login_button.pack(pady=5)

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required.")
            return

        users = load_users()

        if username in users:
            messagebox.showerror("Error", "Username already exists.")
        else:
            password_hash = hash_password(password)
            save_user(username, password_hash)
            messagebox.showinfo("Success", "Registration successful!")
            self.root.destroy()  # Close registration window
            LoginPage(tk.Toplevel(self.root))  # Open login window

    def go_to_login(self):
        self.root.destroy()  # Close the registration window
        LoginPage(tk.Toplevel(self.root))  # Open the login page

# Login Page Class
class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - PunaTel")
        self.root.geometry("300x250")

        # Labels and Input Fields
        username_label = tk.Label(self.root, text="Username:")
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        password_label = tk.Label(self.root, text="Password:")
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        login_button = tk.Button(self.root, text="Login", command=self.login_user)
        login_button.pack(pady=10)

        # Don't have an account?
        register_button = tk.Button(self.root, text="Don't have an account? Register", command=self.go_to_register)
        register_button.pack(pady=5)

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required.")
            return

        users = load_users()

        if username in users and users[username] == hash_password(password):
            messagebox.showinfo("Success", f"Welcome, {username}!")
            self.root.destroy()  # Close login window
            HomePage(tk.Toplevel(self.root), username)  # Open home page
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def go_to_register(self):
        self.root.destroy()  # Close the login window
        RegisterPage(tk.Toplevel(self.root))  # Open the registration page

# PunaTel Home Page Class
class HomePage:
    def __init__(self, root, username):
        self.root = root
        self.root.title("PunaTel - Home Page")
        self.root.geometry("400x300")

        # Welcome Message
        welcome_label = tk.Label(self.root, text=f"Welcome, {username}!", font=("Arial", 16))
        welcome_label.pack(pady=20)

        # Logout button
        logout_button = tk.Button(self.root, text="Logout", command=self.logout)
        logout_button.pack(pady=20)

    def logout(self):
        self.root.destroy()  # Close home window
        LoginPage(tk.Toplevel(self.root))  # Go back to login page

# Main Application Launcher
if __name__ == "__main__":
    root = tk.Tk()
    LoginPage(root)  # Start with the login page
    root.mainloop()
