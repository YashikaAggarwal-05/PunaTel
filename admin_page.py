import logging
import smtplib
from email.mime.text import MIMEText

# Configure logging
logging.basicConfig(filename='email_log.txt', level=logging.DEBUG, format='%(asctime)s %(message)s')

def send_email(user_email, user_id, username):
    try:
        # Email setup
        sender_email = "sansari_entc@jspmrscoe.edu.in"
        subject = "Error Notification"
        body = f"Dear {username},\n\nAn error has been found in the system regarding your logs. Please contact our support care at punatel@gmail.com.\nUser ID: {user_id}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = user_email

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Start TLS
            server.login(sender_email, "your_password")  # Use your Gmail password or app password
            server.send_message(msg)

        logging.info(f"Email sent successfully to {user_email}")
        print("Email sent successfully!")

    except Exception as e:
        logging.error(f"Failed to send email: {e}")
