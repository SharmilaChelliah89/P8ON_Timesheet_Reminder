from email.message import EmailMessage
import ssl
import smtplib

email_sender = "p8on.reminder@gmail.com"

email_server = "smtp.gmail.com"
email_port = 465

subject = "Sending test email from python"
body = """
Sending out the python email.

"""
def main():
      send_email(subject =subject,body=body,sender= email_sender,recipients=email_recipients,password=email_password)

def set_body():
      TODO

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
            server.quit() 

if __name__ == "__main__":
    main()