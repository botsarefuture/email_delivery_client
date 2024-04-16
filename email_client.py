import requests
import time

class EmailClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_email(self, email_from, email_to, subject, text=None, html=None, email=None, password=None, smtp_index=None):
        data = {
            "email_from": email_from,
            "email_to": email_to,
            "subject": subject,
            "text": text,
            "html": html,
            "email": email,
            "password": password,
            "smtp_index": smtp_index
        }

        response = requests.post(f"{self.base_url}/send_email", json=data)
        return response.json()

if __name__ == "__main__":
    # Example usage
    client = EmailClient("http://localhost:5000")  # Change the base URL as needed

    # Example email data
    email_from = "sender@example.com"
    email_to = "recipient@example.com"
    subject = "Test Email"
    text = "This is a test email."
    html = "<p>This is a <b>test</b> email.</p>"
    email = "sender@example.com"
    password = "password"
    smtp_index = 0  # Index of SMTP server from the list

    # Send email
    response = client.send_email(email_from, email_to, subject, text=text, html=html, email=email, password=password, smtp_index=smtp_index)
    print(response)
