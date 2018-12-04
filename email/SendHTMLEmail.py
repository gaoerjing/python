import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver = 'smtp.qiye.aliyun.com'
user = ''
password = ''
sender = ''
receiver = ''
subject = 'Python Email Test'
msg = MIMEText('<html><h1>Hello!</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
