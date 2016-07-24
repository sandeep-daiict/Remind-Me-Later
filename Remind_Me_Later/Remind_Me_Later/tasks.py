from __future__ import absolute_import


import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from RMLApp.models import RemindMe
from celery import Celery
from celery.task import task
BROKER_URL = 'django://'

celery = Celery('tasks',broker=BROKER_URL)


@task
def sendEmail(id):
    # me == my email address
    # you == recipient's email address


    reminder = RemindMe.objects.get(pk=id)
    if reminder is None:
        return
    me = "sandeepsharma.iiit4@gmail.com"
    you = reminder.remind_email
    message = reminder.remind_message

    if not you:
        return

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Reminder From BackTap"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\n" + message
    html = "\<html><head></head><body><p>Hi!<br>How are you?<br>"+ message +"</p></body></html>"


    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.


    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("sandeepsharma.iiit4@gmail.com", "python1991")

    server.sendmail(me, you, msg.as_string())
    server.quit()
