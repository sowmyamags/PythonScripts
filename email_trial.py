#!/usr/bin/env python3

import os.path
import mimetypes
import smtplib
from email.message import EmailMessage
import getpass

"""By importing EmailMessage class from email.message module we send a blank message"""

message = EmailMessage()
sender = "sowmyamaguluri@gmail.com"
recipent = "kiranpanem@gmail.com"

"""Adding the sender and recipent to the email"""
message['From'] = sender
message['To'] = recipent
 
"""Add subject to email"""
message['Subject'] = "Greetings from {} to {}".format(sender, recipent)

"""Body of the mail is added to the set_content of the message"""

body = """Hey there!
   My first email sent using a python code. Hooray"""
message.set_content(body)

print(message)
"""By importing mimetypes we can add the txt/image file to the mail and any file that attached 
   is tconverted to text string"""

attachment_path = "/mnt/c/users/sowmya/Pictures/Camera Roll/aari1.jpg"
attachment_filename = os.path.basename(attachment_path)

"""If we know the type of file taht is attached we can assign maintype and subtype directly or
   can use mimetypes.guess_type()"""
mime_type, _ = mimetypes.guess_type(attachment_path)

print(attachment_path, attachment_filename, mime_type)

mime_type, mime_subtype = mime_type.split('/', 1) 
print(mime_type)
print(mime_subtype)

"""With opeing th efile to read, we assign maintype and subtype and filename to message"""
with open(attachment_path, 'rb') as ap:
   message.add_attachment(ap.read(), 
                          maintype = mime_type,
                          subtype = mime_subtype,
                          filename = os.path.basename(attachment_path))

print(message)
""" by importing smtplib we send and receive the mails. we connect to email server using ssl/tls 
protocols."""
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)

"""by using getpass.getpass() we generate a passwrod that cant be displayed"""
mail_pass = getpass.getpass('Password? ')
print(mail_pass)

"""login to email by using login()"""

mail_server.login(sender,mail_pass)

"""send the email by using send_message(message)"""
mail_server.send_message(message)
mail_server.quit()

