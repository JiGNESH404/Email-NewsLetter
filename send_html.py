from os import name
import smtplib
import pandas as pd
import imghdr
df = pd.read_csv("emails.csv")
mylist = df['Email'].tolist()
from email.message import EmailMessage
SENDER= '' #enter sender's email id
PASS= '' #enter the password for the sender's email
#make sure the login credentials are correct
msg=EmailMessage()
msg['Subject'] = 'Your today\'s newsletter form xyz'
msg['From'] = SENDER
msg['to'] = mylist
msg.set_content('New News-letter is here!')
#-----------FOR ATTATCHING IMAGE-----------#
msg.add_alternative(  
  """\
    <!DOCTYPE html>
    <html>
    <body>
  <h1 style="color:red;">NEWS LETTER</h1>
    </body>
    </html>

  """, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: #replace smpt.google.com with smpt.mail.yahoo.com for yahoo mail provider
  smtp.login(SENDER,PASS)
  smtp.send_message(msg)