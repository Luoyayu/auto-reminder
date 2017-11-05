# -*-coding:utf-8-*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from user import *

Content = """A day so happy.
Fog lifted early. I worked in the garden.
Hummingbirds were stopping over the honeysuckle flowers.
There was nothing on earth I wanted to possess.
I knew no one worth my envying him.
Whatever evil I had suffered, I forgot.
To think that once I was the same man did not embarrass me.
In my body I felt no pain.
When straightening up, I saw blue sea and sails.
"""


def send_mail(to_who, flag):
    message = MIMEText(Content, 'plain', 'utf-8')
    message['From'] = 'auto-reminder@luoyayu.cn'

    message['To'] = 'darling@receiver.com'
    message['Subject'] = Header(to_who + ' is LIVE now!', 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.qq.com')
        # smtpObj.set_debuglevel(1)
        smtpObj.connect(mail_host, mail_port)
        smtpObj.login(mail_username, mail_pw)
        if flag == 'ME': # 按需发给不同的人
            smtpObj.sendmail(sender, receivers, message.as_string())
        return True
    except smtplib.SMTPException:
        return False

# send_mail('HELLO','XXXX')
