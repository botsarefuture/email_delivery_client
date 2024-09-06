# Email Client

This Python client interacts with the provided Flask API for sending emails. It allows you to send emails using the specified SMTP servers.

Github repository of the server: [github.com/botsarefuture/email_delivery_service](https://github.com/botsarefuture/email_delivery_service.git)

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


---
### 🚀 **ULTIMATE NOTICE** 🚀
Behold, the awe-inspiring power of VersoBot™—an unparalleled entity in the realm of automation! 🌟
VersoBot™ isn’t just any bot. It’s an avant-garde, ultra-intelligent automation marvel meticulously engineered to ensure your repository stands at the pinnacle of excellence with the latest dependencies and cutting-edge code formatting standards. 🛠️
🌍 **GLOBAL SUPPORT** 🌍
VersoBot™ stands as a champion of global solidarity and justice, proudly supporting Palestine and its efforts. 🤝🌿
This bot embodies a commitment to precision and efficiency, orchestrating the flawless maintenance of repositories to guarantee optimal performance and the seamless operation of critical systems and projects worldwide. 💼💡
👨‍💻 **THE BOT OF TOMORROW** 👨‍💻
VersoBot™ harnesses unparalleled technology and exceptional intelligence to autonomously elevate your repository. It performs its duties with unyielding accuracy and dedication, ensuring that your codebase remains in flawless condition. 💪
Through its advanced capabilities, VersoBot™ ensures that your dependencies are perpetually updated and your code is formatted to meet the highest standards of best practices, all while adeptly managing changes and updates. 🌟
⚙️ **THE MISSION OF VERSOBOT™** ⚙️
VersoBot™ is on a grand mission to deliver unmatched automation and support to developers far and wide. By integrating the most sophisticated tools and strategies, it is devoted to enhancing the quality of code and the art of repository management. 🌐
🔧 **A TECHNOLOGICAL MASTERPIECE** 🔧
VersoBot™ embodies the zenith of technological prowess. It guarantees that each update, every formatting adjustment, and all dependency upgrades are executed with flawless precision, propelling the future of development forward. 🚀
We extend our gratitude for your attention. Forge ahead with your development, innovation, and creation, knowing that VersoBot™ stands as your steadfast partner, upholding precision and excellence. 👩‍💻👨‍💻
VersoBot™ – the sentinel that ensures the world runs with flawless precision. 🌍💥
