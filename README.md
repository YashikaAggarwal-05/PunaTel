Management System
1. Introduction
This document serves as a user guide for the Design Log Monitoring Application’s GUI Module. It provides comprehensive instructions on installing the software, navigating the GUI, and accessing key functionalities i.e. log management and email notifications
2 Installation Steps
•	Download and Install Python
o	Visit the Python website and download the latest version.
o	Follow the installation instructions specific to your operating system.
•	Install Required Libraries
o	Open your terminal or command prompt.
o	Run the following command to install necessary libraries: - Tkinter, Pillow, Hashlib, SQLite3 (comes bundled with Python), messagebox, MIMEText, Plyer
------pip install [enter_above_library_names].
o	Download the GUI Module from GitHub
o	Run the following command to clone the repository: 
                     ------- git clone GitHub - YashikaAggarwal-05/PunaTel
•	Navigate to the Project Directory
o	After cloning the repository, navigate to the project directory:
               ------ cd PunaTel
•	Run the Application
               ----- python main.py
3. Usage Instructions
3.1 Creating a New User Account
•	When the application starts, the home page will appear.
•	Click the Sign Up button to create a new user account.
•	Enter your email and password into the provided fields.
•	Click Submit to create your account. Your details will be saved in the SQLite database under the users table.
•	After successful registration, you will be redirected back to the login page.


3.2	Logging In
•	For Users: Enter the email and password that you used during the sign up process . Upon successful authentication, you will be directed to the user dashboard.
•	For Admins: Enter the admin credentials (provided by the system administrator) to access the admin dashboard.
3.3 Accessing Logs
•	Once logged in as a user or admin, navigate to the "Logs" section.
•	Click on the "View Logs" button to access the call logs.
•	The logs will display the following details:
o	User: The user who made the call.
o	Recipient: The person the user called.
o	Call Duration: The total time (in minutes) that the call lasted.
o	Start Time: The time the call began.
o	End Time: The time the call ended.
•	Admin Functionality: Admins have additional privileges to manage users and view detailed system logs, but cannot create call logs themselves.
3.3	Notifications
•	The users are notified about the error logs occurred in real time via mail.
SQLite Database Integration
In this system:
•	User information (email and password) is stored in an SQLite database (users.db).
•	When a user signs up, their details are automatically added to the database.
•	The system will check the database for valid credentials when a user attempts to log in.
•	Admin login credentials are hardcoded in the system for security reasons and cannot be created via the sign-up page.

