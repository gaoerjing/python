import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

smtpserver = 'smtp.qiye.aliyun.com'
user = ''
password = ''
sender = ''
receiver = ''
subject = 'Python Email Test'
print("path is {}".format(os.path.join(os.path.abspath("."),"SendHTMLEmail.py")))
filePath = os.path.join(os.path.abspath("."),"SendHTMLEmail.py")
if os.path.exists(filePath):
    fileID = open(filePath,'rb')
    sendFile = fileID.read()
    fileID.close()
    att = MIMEText(sendFile,'base64','utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename="SendHTMLEmail.py"'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
