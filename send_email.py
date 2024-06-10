import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

FROM_EMAIL = os.getenv('FROM_EMAIL')
PASSWORD = os.getenv('PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))
EMAIL_BODY = os.getenv('EMAIL_BODY')
EMAIL_SUBJECT = os.getenv('EMAIL_SUBJECT')
SENDER_NAME = os.getenv('SENDER_NAME')
ATTACHMENT_PATH = os.getenv('ATTACHMENT_PATH')

def send_email(subject, body, to_email, from_email, password, smtp_server, smtp_port, attachment_path=None):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    if attachment_path:
        attachment = open(attachment_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
        msg.attach(part)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

def send_emails(subject, body, to_emails, from_email, password, smtp_server, smtp_port, attachment_path=None):
    for to_email in to_emails:
        send_email(subject, body, to_email.strip(), from_email, password, smtp_server, smtp_port, attachment_path)
        print(f"Email to {to_email.strip()} has been sent.")

# Path to the text file with email addresses
email_list_path = 'email-adress-list.txt'

# Reading email addresses from the file
with open(email_list_path, 'r') as file:
    to_emails = file.readlines()

# Sending the emails
send_emails(EMAIL_SUBJECT, EMAIL_BODY, to_emails, FROM_EMAIL, PASSWORD, SMTP_SERVER, SMTP_PORT, ATTACHMENT_PATH)
