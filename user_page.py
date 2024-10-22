import tkinter as tk
from tkinter import messagebox
import hashlib
import sqlite3

DB_NAME = "punatel.db"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def get_user_from_db(username):
    """Get user credentials from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user


class LoginPage:
    def _init_(self, root):
        self.root = root
        self.root.title("Login - PunaTel")
        self.root.geometry("400x300")

        title_label = tk.Label(self.root, text="PunaTel", font=("Arial", 24), fg="blue")
        title_label.pack(pady=20)

        username_label = tk.Label(self.root, text="Username:")
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        password_label = tk.Label(self.root, text="Password:")
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        login_button = tk.Button(self.root, text="Login", command=self.login_user)
        login_button.pack(pady=20)

    def login_user(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required.")
            return

        password_hash = hash_password(password)

        user = get_user_from_db(username)

        if user and user[0] == password_hash:
            messagebox.showinfo("Success", f"Welcome, {username}!")
            self.root.destroy()  # Close login window
            UserPage(tk.Toplevel(self.root), username)  # Open user page
        else:
            messagebox.showerror("Error", "Invalid username or password.")


class UserPage:
    def _init_(self, root, username):
        self.root = root
        self.root.title("User Page - PunaTel")
        self.root.geometry("500x400")

        welcome_label = tk.Label(self.root, text=f"Welcome, {username}!", font=("Arial", 16))
        welcome_label.pack(pady=20)

        error_log_button = tk.Button(self.root, text="View Error Logs", command=self.view_error_logs)
        error_log_button.pack(pady=10)

        logout_button = tk.Button(self.root, text="Logout", command=self.logout)
        logout_button.pack(pady=10)

    def view_error_logs(self):
        log_window = tk.Toplevel(self.root)
        log_window.title("Error Logs")
        log_window.geometry("500x300")

        logs = get_logs()
        log_text = tk.Text(log_window, wrap=tk.WORD)
        log_text.pack(expand=True, fill=tk.BOTH)

        for log in logs:
            log_text.insert(tk.END, f"{log[3]} - {log[1]}\n")

    def logout(self):
        self.root.destroy()
        LoginPage(tk.Toplevel(self.root))


if __name__ == "_main_":
    root = tk.Tk()
    LoginPage(root)  # Start with the login page
    root.mainloop()