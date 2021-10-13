'''
    1.数据类：
        只准备数据部分：不参与任何操作。
    任务1：
        将这个框架的数据源集中写到excel表里，使用xlrd读取
        xlrd参数化，mysql的参数化。
'''
# '''excel表
import xlrd

wd = xlrd.open_workbook(filename='HKR.xlsx',encoding_override=True)

exp = wd.sheet_by_index(0)
list= []
for i in range(1,3):
    ture = exp.row_values(i)
    if isinstance(ture[1],float):
        ture[1] = int(ture[1])
    a = {"username": ture[0], "password": ture[1], "expect": ture[2]}
    list.append(a)


list1=[]
for j in range (3,5):
    faile = exp.row_values(j)
    if isinstance(faile[1],float):
        faile[1] = int(faile[1])
    b = {"username": faile[0], "password": faile[1], "expect": faile[2]}
    list1.append(b)


class  Initpage:

    login_success_data = list

    login_error_data = list1

    # login_success_data = [
    #     {"username": "jason", "password": "1234567", "expect": "Student Login"},
    #     {"username": "不再爱了", "password": "1234567", "expect": "Student Login"}
    # ]
    #
    # login_error_data = [
    #     # id : msg_uname
    #     {"username": "jason1213123123123", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
    #     {"username": "不再爱了", "password": "123456789898945", "expect": "账户名错误或密码错误!别瞎弄!"}
    # ]
# '''
'''
import pymysql

list = []
list1 = []

con = pymysql.connect(host="localhost", user="root", password="root", database="hkrtest",charset='utf8')
cursor = con.cursor()
sql = "select * from success"
cursor.execute(sql)
date = cursor.fetchall()
for i in range(2):
    dict = {'username': date[i][0], 'password': date[i][1], 'expect': date[i][2]}
    list.append(dict)

for j in range(2,4):
    dict = {'username': date[j][0], 'password': date[j][1], 'expect': date[j][2]}
    list1.append(dict)


# sql1 = "select * from error"
# cursor.execute(sql1)
# date1 = cursor.fetchall()
# for i in range(len(date1)):
#     dict1 = {'username': date1[i][0], 'password': date1[i][1], 'expect': date1[i][2]}
#     list1.append(dict1)

con.commit()
cursor.close()
con.close()

# class  InitPage:
#
#     login_success_data = list
#
#     login_error_data = list1
'''













