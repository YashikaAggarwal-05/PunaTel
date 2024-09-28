import tkinter as tk
from tkinter import messagebox, ttk
import random

# Admin Page Class
class AdminPage:
    def __init__(self, root):
        self.root = root
        self.root.title("PunaTel - Admin Page")
        self.root.geometry("800x500")

        # Initialize user data
        self.user_data = []
        self.dark_mode = False

        # Navigation Bar Frame
        nav_frame = tk.Frame(self.root)
        nav_frame.pack(pady=10)

        # Navigation Buttons
        self.view_logs_button = tk.Button(nav_frame, text="View Logs", command=self.view_logs)
        self.view_logs_button.pack(side=tk.LEFT, padx=5)

        self.add_user_button = tk.Button(nav_frame, text="Add User", command=self.add_user)
        self.add_user_button.pack(side=tk.LEFT, padx=5)

        self.delete_user_button = tk.Button(nav_frame, text="Delete User", command=self.delete_user)
        self.delete_user_button.pack(side=tk.LEFT, padx=5)

        self.manage_users_button = tk.Button(nav_frame, text="Manage Users", command=self.manage_users)
        self.manage_users_button.pack(side=tk.LEFT, padx=5)

        self.settings_button = tk.Button(nav_frame, text="System Settings", command=self.system_settings)
        self.settings_button.pack(side=tk.LEFT, padx=5)

        self.logout_button = tk.Button(nav_frame, text="Logout", command=self.logout)
        self.logout_button.pack(side=tk.LEFT, padx=5)

        # Welcome label for Admin
        self.welcome_label = tk.Label(self.root, text="Admin Dashboard", font=("Arial", 16))
        self.welcome_label.pack(pady=20)

        # Table for User Data
        self.user_table = ttk.Treeview(self.root, columns=("UserID", "Username", "Password", "PhoneNumber", "EmailID", "Billing"), show="headings")
        self.user_table.pack(pady=20)

        # Define headings
        self.user_table.heading("UserID", text="User ID")
        self.user_table.heading("Username", text="Username")
        self.user_table.heading("Password", text="Password (hashed)")
        self.user_table.heading("PhoneNumber", text="Phone Number")
        self.user_table.heading("EmailID", text="Email ID")
        self.user_table.heading("Billing", text="Billing")

        # Example Data
        self.sample_data = [
            (1, "user1", "hashed_pass1", "1234567890", "user1@example.com", "$10.00"),
            (2, "user2", "hashed_pass2", "0987654321", "user2@example.com", "$15.00"),
            (3, "user3", "hashed_pass3", "5554443333", "user3@example.com", "$20.00"),
            (4, "user4", "hashed_pass4", "7778889999", "user4@example.com", "$25.00"),
        ]

        # Inserting sample data into the table
        for item in self.sample_data:
            self.user_table.insert("", tk.END, values=item)
            self.user_data.append(item)  # Store user data for later use

    # Function to handle View Logs action
    def view_logs(self):
        selected_item = self.user_table.selection()
        if not selected_item:
            messagebox.showwarning("Select User", "Please select a user to view logs.")
            return

        user = self.user_table.item(selected_item)["values"]
        phone_number = user[3]  # Get the phone number

        # Generate random logs for the selected user
        logs = [f"Call from {phone_number} to {random.randint(1000000000, 9999999999)} at {random.randint(0, 23)}:{random.randint(0, 59)}"
                for _ in range(5)]  # Random log messages

        log_message = "\n".join(logs)
        messagebox.showinfo("User Logs", f"Logs for {user[1]}:\n{log_message}")

    # Function to handle Add User action
    def add_user(self):
        add_user_window = tk.Toplevel(self.root)
        add_user_window.title("Add User")

        # User input fields
        tk.Label(add_user_window, text="User ID:").grid(row=0, column=0)
        tk.Label(add_user_window, text="Username:").grid(row=1, column=0)
        tk.Label(add_user_window, text="Password:").grid(row=2, column=0)
        tk.Label(add_user_window, text="Phone Number:").grid(row=3, column=0)
        tk.Label(add_user_window, text="Email ID:").grid(row=4, column=0)
        tk.Label(add_user_window, text="Billing:").grid(row=5, column=0)

        user_id_entry = tk.Entry(add_user_window)
        username_entry = tk.Entry(add_user_window)
        password_entry = tk.Entry(add_user_window)
        phone_number_entry = tk.Entry(add_user_window)
        email_id_entry = tk.Entry(add_user_window)
        billing_entry = tk.Entry(add_user_window)

        user_id_entry.grid(row=0, column=1)
        username_entry.grid(row=1, column=1)
        password_entry.grid(row=2, column=1)
        phone_number_entry.grid(row=3, column=1)
        email_id_entry.grid(row=4, column=1)
        billing_entry.grid(row=5, column=1)

        def submit_user():
            new_user = (
                int(user_id_entry.get()),
                username_entry.get(),
                password_entry.get(),
                phone_number_entry.get(),
                email_id_entry.get(),
                billing_entry.get()
            )
            self.user_table.insert("", tk.END, values=new_user)
            self.user_data.append(new_user)  # Add to user data
            add_user_window.destroy()

        tk.Button(add_user_window, text="Add User", command=submit_user).grid(row=6, columnspan=2)

    # Function to handle Delete User action
    def delete_user(self):
        selected_item = self.user_table.selection()
        if not selected_item:
            messagebox.showwarning("Select User", "Please select a user to delete.")
            return

        user = self.user_table.item(selected_item)["values"]
        self.user_table.delete(selected_item)
        self.user_data.remove(user)  # Remove from user data
        messagebox.showinfo("Delete User", f"User {user[1]} deleted successfully.")

    # Function to handle Manage Users action
    def manage_users(self):
        total_users = len(self.user_data)
        active_users = total_users  # For simplicity, assuming all are active
        past_users = random.randint(0, 10)  # Generate random past users
        messagebox.showinfo("User Management", f"Total Users: {total_users}\nActive Users: {active_users}\nPast Users: {past_users}")

    # Function to handle System Settings action
    def system_settings(self):
        if self.dark_mode:
            self.root.config(bg="white")
            self.welcome_label.config(bg="white", fg="black")
            self.user_table.config(bg="white", fg="black")
            self.dark_mode = False
            messagebox.showinfo("Settings", "Switched to Light Mode")
        else:
            self.root.config(bg="black")
            self.welcome_label.config(bg="black", fg="white")
            self.user_table.config(bg="black", fg="white")
            self.dark_mode = True
            messagebox.showinfo("Settings", "Switched to Dark Mode")

    # Function to logout
    def logout(self):
        self.root.destroy()

# Start the Admin Page
if __name__ == "__main__":
    root = tk.Tk()
    AdminPage(root)
    root.mainloop()
