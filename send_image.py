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
files=['1.png','2.png']
for file in files:
  with open(file,'rb') as img:
    image_file=img.read()
    type=imghdr.what(img.name)
    name=img.name
  msg.add_attachment(image_file,maintype='image',subtype=type,filename=name)
   
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: #replace smpt.google.com with smpt.mail.yahoo.com for yahoo mail provider
  smtp.login(SENDER,PASS)
  smtp.send_message(msg)