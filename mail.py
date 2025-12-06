import smtplib
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Mail:

    def __init__(self, email, message):
        print("Initializing Mail")

        self.email = email
        self.my_mail = "miniash3127@gmail.com"
        self.password = os.getenv("MAIL_APP_PASSWORD")
        self.message = message

    def send_mail(self):

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(self.my_mail, self.password)

            print(self.message)

            connection.sendmail(
                from_addr=self.my_mail,
                to_addrs=self.email,
                msg=f"Subject: New Message!!!\n\n{self.message}"
            )


