from __future__ import absolute_import


import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import TwilioRestClient
from RMLApp.models import RemindMe
from celery import Celery
from celery.task import task
BROKER_URL = 'django://'
import os
celery = Celery('tasks',broker=BROKER_URL)


@task
def sendEmail(id):
    # me == my email address
    # you == recipient's email address


    reminder = RemindMe.objects.get(pk=id)
    if reminder is None:
        return
    sender = os.environ.get("EMAIL_SENDER")
    you = reminder.remind_email
    message = reminder.remind_message


    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Reminder"
    msg['From'] = sender
    msg['To'] = you


    text = message
    html = "<html><head></head><body><p>"+ message +"</p></body></html>"



    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')


    msg.attach(part1)
    msg.attach(part2)



    email_server =  os.environ.get("EMAIL_SERVER")
    email_port =  os.environ.get("EMAIL_PORT")
    email_password = os.environ.get("EMAIL_PASSWORD")

    server = smtplib.SMTP(email_server,email_port)
    server.starttls()
    server.login(sender,email_password )

    server.sendmail(sender, you, msg.as_string())
    server.quit()


@task
def sendSMS(id):
    reminder = RemindMe.objects.get(pk=id)
    if reminder is None:
        return
    account_sid = os.environ.get("TWILIO_SID")
    auth_token =os.environ.get("TWILIO_OAUTHTOKEN")

    f =os.environ.get("TWILIO_REGISTERED_NUMBER")

    message = reminder.remind_message
    if not message:
        message = "Reminder"
    to = reminder.remind_phone
    client = TwilioRestClient(account_sid, auth_token)
    client.messages.create(to=to, from_=f,body=message)