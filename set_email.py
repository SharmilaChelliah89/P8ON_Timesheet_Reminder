from email.message import EmailMessage
import ssl
import smtplib
from datetime import datetime
import calendar

email_sender = "p8on.reminder@gmail.com"
email_password = ""
email_recipients = []

email_server = "smtp.gmail.com"
email_port = 465

subject = "Sending test email from python"

def main():
      send_email(subject =subject,body=get_body(),sender= email_sender,recipients=email_recipients,password=email_password)


def get_body():
      
      return f"""
Hello Everyone,
      
Am reaching out regarding your time sheet for the period {get_date()}. We haven’t received notification of your submission yet.
      
Kindly submit your timesheets as soon as possible to avoid any last-minute issues with the tool.
      
Please note, our team will reach out to you via teams if necessary."""

 
def get_date():
      # Find todays date
      today = datetime.today()
      year = today.year
      month = today.month
      day = today.day
      

      # find the last date of the month
      last_day = calendar.monthrange(year,month)[1]

      if day < 15:
            date_obj = datetime(year, month, 15)
      else:
            date_obj = datetime(year, month, last_day)

      return date_obj.strftime("%b-%d-%Y")

def send_email(subject, body, sender, recipients, password):
    em = EmailMessage()
    em['From'] = sender
    em['To'] = recipients
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(email_server,email_port,context=context) as server:
    
            server.login(sender, password)
            server.sendmail(sender,recipients,em.as_string())

if __name__ == "__main__":
    main()