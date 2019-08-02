import zmail
import smtplib
from utils import parser_account, parser_recipient
from config import *

cache_mail = set()

try:
    mail_list = parser_recipient()
    server = zmail.server(email, passwd, config='qq')
    if server.smtp_able():
        for i in mail_list:
            server.send_mail(i, MAIL_CONTENT)
            print('{}\t发送成功...'.format(i))
            cache_mail.add(i)
    else:
        print('账户验证失败....')
except Exception as e:
    print(e)
finally:
    with open(os.path.join(BASE_DIR, 'error_send_mail.txt'), 'a') as f:
        f.write(set(mail_list) - cache_mail)
