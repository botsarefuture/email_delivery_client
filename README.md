# Email Client

This Python client interacts with the provided Flask API for sending emails. It allows you to send emails using the specified SMTP servers.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/botsarefuture/email_delivery_client.git
    ```

2. Navigate to the directory:

    ```bash
    cd email-client
    ```

3. Install the required dependencies:

    ```bash
    pip install requests
    ```

## Usage

1. Import the `EmailClient` class from `email_client.py`.
2. Create an instance of `EmailClient` by providing the base URL of the Flask API.
3. Use the `send_email` method to send emails with the required parameters.

Example usage:

```python
from email_client import EmailClient

client = EmailClient("http://localhost:5000")

email_from = "sender@example.com"
email_to = "recipient@example.com"
subject = "Test Email"
text = "This is a test email."
html = "<p>This is a <b>test</b> email.</p>"
email = "sender@example.com"
password = "password"
smtp_index = 0

response = client.send_email(email_from, email_to, subject, text=text, html=html, email=email, password=password, smtp_index=smtp_index)
print(response)
```

## API Specification

The client interacts with the following API endpoint:

- `POST /send_email`: Sends an email with the provided parameters.

Required Parameters:

- `email_from`: Sender's email address.
- `email_to`: Recipient's email address.
- `subject`: Email subject.

Optional Parameters:

- `text`: Plain text content of the email.
- `html`: HTML content of the email.
- `email`: Sender's email address (if not provided in session).
- `password`: Sender's email password (if not provided in session).
- `smtp_index`: Index of the SMTP server to use (if not using default configuration).
