import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'xxx@email.com'
email_password = 'xxxx'
email_send = 'xxxx@gmail.com'

subject = 'Alert!!!'

msg = MIMEMultipart()
msg['From'] = "From Python <"+email_user+">"
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi, this email is sent from Python! \n Please find the attachment'
msg.attach(MIMEText(body,'plain'))

filename='icon.png'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
try:  
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.mail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()
    print ('Email sent!'),email_send
except:  
    print ('Something went wrong...')
