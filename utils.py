import os
import xlrd
from datetime import date, datetime
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

def Excel():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    excleUrl = os.path.join(BASE_DIR, 'data', 'mailTo.xls')
    excleUrl = excleUrl.replace('\\', '/')
    def ExcelRead(excleUrl):
        dictMail=[]
        workbook = xlrd.open_workbook(excleUrl)  # 读取文件下面的所有sheet表
        sheet1 = workbook.sheet_names()[0]  # 读取第一个sheet表
        sheet1 = workbook.sheet_by_name('Sheet1')
        rows = sheet1.row_values(1)  # 一行，全部读取
        cols0 = sheet1.col_values(0)  # 一列全部读取
        cols1 = sheet1.col_values(1)  # 二列全部读取
        cols0 = list(cols0)
        cols1 = list(cols1)
        for i in range(len(cols0)):
            dictMail += [["@"+cols0[i].split('@')[-1], cols0[i], cols1[i]]]
        return dictMail
    return ExcelRead(excleUrl)
