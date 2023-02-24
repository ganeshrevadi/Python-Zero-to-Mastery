import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Ganesh'
email['subject'] = 'testing smtb'
email['to'] = 'ganeshrevadi16@gmail.com'

email.set_content('Testing yoooo')

with smtplib.SMTP(host = 'smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ridewithpride12@gmail.com', 'ffedvknpvqahvjan')
    smtp.send_message(email)
    print('All goood!')