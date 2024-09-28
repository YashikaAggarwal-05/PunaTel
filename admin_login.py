import tkinter as tk
from tkinter import messagebox

class AdminPage:
    def __init__(self, root):
        self.root = root
        self.root.title("PunaTel - Admin Page")
        self.root.geometry("400x400")

        welcome_label = tk.Label(self.root, text="Admin Dashboard", font=("Arial", 16))
        welcome_label.pack(pady=20)

        # Admin Rights
        view_logs_button = tk.Button(self.root, text="View Logs", command=self.view_logs)
        view_logs_button.pack(pady=10)

        add_user_button = tk.Button(self.root, text="Add User", command=self.add_user)
        add_user_button.pack(pady=10)

        delete_user_button = tk.Button(self.root, text="Delete User", command=self.delete_user)
        delete_user_button.pack(pady=10)

        manage_users_button = tk.Button(self.root, text="Manage Users", command=self.manage_users)
        manage_users_button.pack(pady=10)

        settings_button = tk.Button(self.root, text="System Settings", command=self.system_settings)
        settings_button.pack(pady=10)

        logout_button = tk.Button(self.root, text="Logout", command=self.logout)
        logout_button.pack(pady=20)

    # Functions for Admin Rights
    def view_logs(self):
        messagebox.showinfo("Logs", "Viewing system logs...")

    def add_user(self):
        messagebox.showinfo("Add User", "Adding a new user...")

    def delete_user(self):
        messagebox.showinfo("Delete User", "Deleting a user...")

    def manage_users(self):
        messagebox.showinfo("Manage Users", "Managing users...")

    def system_settings(self):
        messagebox.showinfo("Settings", "Accessing system settings...")

    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    AdminPage(root)
    root.mainloop()
