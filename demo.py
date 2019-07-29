import zmail
import smtplib
from config import *

# server = zmail.server(email, passwd)
# server = zmail.server(
#     email, passwd, smtp_host='smtp.exmail.qq.com', smtp_port=465, smtp_ssl=True, config='qq')
try:
    # server = zmail.server(email, passwd, config='qq')
    server = zmail.server(email, passwd, smtp_host='smtp.exmail.qq.com',
                          smtp_port='465', smtp_ssl=True)
    server.send_mail('964655356@qq.com', {
        'subject': email_subject, 'content_text': email_content})
except smtplib.SMTPAuthenticationError as e:
    print('用户名密码错误:')
    print(e)
except smtplib.SMTPSenderRefused as e:
    print('登陆地址与发件人地址不一致:')
    print(e)
except Exception as e:
    print(e)
