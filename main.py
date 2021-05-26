# CHROME DRIVER: https://sites.google.com/a/chromium.org/chromedriver/downloads

import os
import logging
import smtplib

from email.message import EmailMessage
from selenium import webdriver

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

PATH: str = "C:\Program Files (x86)\chromedriver.exe"  # Windows
# PATH: str = "/usr/local/bin/chromedriver.exe" # Docker

driver = webdriver.Chrome(PATH)

logging.info("Going to Google!")
driver.get("https://www.google.com")

logging.info("Exiting the browser.")
driver.quit()

logging.info("Get ENV variables")
EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

logging.info("Configures email message")
msg = EmailMessage()
msg["Subject"] = "TEST Email"
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS
msg.set_content("This is a test email from your frendly python bot.")

logging.info("Send email message to gmail")
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("Email sent")
