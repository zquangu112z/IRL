import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


s = smtplib.SMTP(host='smtp.googlemail.com', port=587)
s.starttls()
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
s.login(MAIL_USERNAME, MAIL_PASSWORD)

name = "Kilia"
email = "zquangu112z@gmail.com"

message_template = read_template('message.txt')

msg = MIMEMultipart()
# add in the actual person name to the message template
message = message_template.substitute(PERSON_NAME=name.title())

# setup the parameters of the message
msg['From'] = MAIL_USERNAME
msg['To'] = email
msg['Subject'] = "This is TEST"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# send the message via the server set up earlier.
s.send_message(msg)
