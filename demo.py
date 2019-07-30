import zmail
import smtplib
from config import *

# server = zmail.server(email, passwd)
# server = zmail.server(
#     email, passwd, smtp_host='smtp.exmail.qq.com', smtp_port=465, smtp_ssl=True, config='qq')
try:
    # server = zmail.server(email, passwd, config='qq')
    # server = zmail.server(email, passwd, smtp_host='smtp.exmail.qq.com',
    #                       smtp_port='465', smtp_ssl=True)
    server = zmail.server(email, passwd)
    server.send_mail(email_list, MAIL_CONTENT)
except smtplib.SMTPAuthenticationError as e:
    print(e)
except Exception as e:
    print(e)
