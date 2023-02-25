import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Ganesh'
email['subject'] = 'testing smtb'
email['to'] = 'ganeshrevadi16@gmail.com'

email.set_content(html.substitute({'name' :'Tintin'}),'html')

with smtplib.SMTP(host = 'smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ridewithpride12@gmail.com', 'ffedvknpvqahvjan')
    smtp.send_message(email)
    print('All goood!')