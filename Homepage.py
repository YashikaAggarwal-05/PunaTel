import tkinter as tk
from tkinter import messagebox


# Ensure you have the Pillow library installed: pip install Pillow

# Sample user credentials (In a real system, use a database)
import hashlib  # For password hashing

users_db = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
}

# Login Page class (from previous code)
class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - PunaTel System")
        self.root.geometry("300x250")
        self.root.configure(bg="#f0f0f0")

        
    
# Main Home Page class with PunaTel branding
class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to PunaTel")
        self.root.geometry("600x400")
        self.root.configure(bg="#ffffff")  # Set background color to white

        # Load and display the PunaTel logo (optional)
        # Make sure you have a logo image file named 'punatel_logo.png' in the same directory
        try:
            logo_image = Image.open("punatel_logo.png")
            logo_image = logo_image.resize((200, 100), Image.ANTIALIAS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            logo_label = tk.Label(self.root, image=self.logo_photo, bg="#ffffff")
            logo_label.pack(pady=20)
        except Exception as e:
            # If logo image is not found, display company name instead
            company_label = tk.Label(self.root, text="PunaTel", font=("Arial", 36, "bold"), bg="#ffffff", fg="#004080")
            company_label.pack(pady=20)

        # Welcome message or tagline
        welcome_label = tk.Label(self.root, text="Innovating Communication Solutions", font=("Arial", 16), bg="#ffffff", fg="#0066cc")
        welcome_label.pack(pady=10)

        # Login button
        login_button = tk.Button(self.root, text="Proceed to Login", font=("Arial", 14), command=self.open_login_page, bg="#0066cc", fg="#ffffff", width=20, height=2)
        login_button.pack(pady=40)

        # Footer or additional info
        footer_label = tk.Label(self.root, text="© 2024 PunaTel. All rights reserved.", font=("Arial", 10), bg="#ffffff", fg="#808080")
        footer_label.pack(side=tk.BOTTOM, pady=10)

    def open_login_page(self):
        # Open the login page
        login_root = tk.Toplevel(self.root)
        login_page = LoginPage(login_root)

# Main application launcher
def main_app(username):
    # This function would launch the main dashboard after successful login
    # For demonstration purposes, we'll show a simple message
    root = tk.Tk()
    root.title("PunaTel System Dashboard")
    root.geometry("500x300")
    welcome_label = tk.Label(root, text=f"Welcome to the Dashboard, {username}", font=("Arial", 16))
    welcome_label.pack(pady=50)
    root.mainloop()

# Main application starts with the home page
if __name__ == "__main__":
    root = tk.Tk()
    home_page = HomePage(root)
    root.mainloop()
