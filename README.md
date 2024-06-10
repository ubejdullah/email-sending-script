# Email Sending Script

This Python script facilitates sending emails to a list of recipients.

## Features

- The script automatically reads a list of email addresses from a text file and sends an email to each address.
- You can configure the subject, message body, and optionally an attachment for each email.

## Usage

1. Fill the `.env` file with the required information:

    ```dotenv
    FROM_EMAIL=your_email@gmail.com
    PASSWORD=your_email_password
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587
    EMAIL_BODY=Hello, this is a test email.
    EMAIL_SUBJECT=Test Email
    SENDER_NAME=Example Sender
    ATTACHMENT_PATH=/path/to/attachment/file.txt
    ```

2. Adjust the values accordingly to your email account information and attachment path.

3. Run the script by executing the following command:

    ```bash
    python email_sender.py
    ```

## Files

- `email_sender.py`: The Python script for sending emails.
- `.env`: The configuration file containing email account information and other parameters.
- `email-adress-list.txt`: The list of email addresses to which emails will be sent.

## Note

Ensure that the `email-adress-list.txt` file exists and contains valid email addresses before running the script.