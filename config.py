import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ACCOUNT_PATH = 'data/'

RECIPIENT_PATH = os.path.join(os.path.join(
    BASE_DIR, 'data'), 'mail.txt')

HTML_PATH = os.path.join(os.path.join(
    BASE_DIR, 'template'), 'html.html')

email = "mz@myzweb.com"
passwd = "AAcyyfKp4HWMbc9N"


# email = "V13086771210@outlook.com"
# passwd = "aabbcc123123"

# email = "mz@myzweb.com"
# passwd = "pioFkSLbKkq5rPhW"
# email = "1211558160@qq.com"
# passwd = "aabb8778"

# email_list = ['1449627412@qq.com', 'mz@myzweb.com']
# email_subject = "Test"
# email_content = "this is Test content."


with open(HTML_PATH, 'r', encoding='UTF-8') as f:
    content_html = f.read()

MAIL_CONTENT = {
    'subject': '计划包输，实力违规操作预知结果百分百百分百准确率，-- + 1718415819',
    'content_text': 'hei ke ji计划包 输跟，实力违规违规 操作 预知结果百分百准确准确率，百分百BAOZHUANG科技最新黑想搞的+1718415819'
    # 'attachments': ['/Users/zyh/Documents/example.zip', '/root/1.jpg'],
}
