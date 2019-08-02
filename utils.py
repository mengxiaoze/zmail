import os
from config import BASE_DIR, RECIPIENT_PATH


def parser_recipient():
    try:
        with open(RECIPIENT_PATH, 'r') as f:
            lines = [_.strip() + '@qq.com' for _ in f.readlines()]
    except PermissionError as e:
        print('路径不正确，重新配置config文件\'RECIPIENT_PATH\'')
        print(e)
    except FileNotFoundError as e:
        print('文件不存在!')
        print(e)
    except Exception as e:
        print(e)
    return list(set(lines))


def parser_account():
    pass
