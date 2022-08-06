import json
import os
import smtplib

from email.message import EmailMessage


def send_email():
  to_email = os.environ["TO_EMAIL"]
  from_email = os.environ["FROM_EMAIL"]
  password = os.environ["PASSWORD"]
  smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
  smtpobj.ehlo()
  smtpobj.starttls()
  smtpobj.ehlo()
  smtpobj.login(from_email, password)
  msg = EmailMessage()
  msg.set_content('')
  msg['Subject'] = 'The subject!'
  msg['From'] = from_email
  msg['To'] = to_email
  smtpobj.send_message(msg)
  smtpobj.quit()

def lambda_handler(event, context):
    # TODO implement
    send_email()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
