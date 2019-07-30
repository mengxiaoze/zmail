import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ACCOUNT_PATH = 'data/'

RECIPIENT_PATH = os.path.join(os.path.join(
    BASE_DIR, 'data'), 'mail.txt')

HTML_PATH = os.path.join(os.path.join(
    BASE_DIR, 'template'), 'html.html')

# email = "mz@myzweb.com"
# passwd = "pioFkSLbKkq5rPhW"


email = "zhangqingde12138@outlook.com"
passwd = "13661886709."

# email = "mz@myzweb.com"
# passwd = "pioFkSLbKkq5rPhW"
# email = "1211558160@qq.com"
# passwd = "aabb8778"

email_list = ['1449627412@qq.com', 'mz@myzweb.com']
# email_subject = "Test"
# email_content = "this is Test content."


with open(HTML_PATH, 'r', encoding='UTF-8') as f:
    content_html = f.read()

MAIL_CONTENT = {
    'subject': '系统提醒',
    'content_text': content_html
    # 'attachments': ['/Users/zyh/Documents/example.zip', '/root/1.jpg'],
}
