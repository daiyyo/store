info='''
****************************
*         中国工商银行       *
*         账户管理系统       *
*          V 1.0           *
****************************
*                          *
*          1.开户           *
*          2.存钱           *
*          3.取钱           *
*          4.转账           *
*          5.查询           *
*          6.bye           *
****************************
'''
import random
print(info)
users={}     #100个
#银行名
bank_name="中国工商银行的昌平支行"
#银行开户逻辑
def bank_adduser(account,name,password,country,province,street,door):
    #判断是否已满
    if len(users)>=100:
        return 3

    #判断是否存在
    if account in users:
        return 2
    #正常开户
    users[account]={
        'name': name,
        'password': password,
        'country': country,
        'province': province,
        'street': street,
        'door': door,
        'bank_name': bank_name,
        "money":0,   #默认余额为0

    }

    return 1


# def findByAccount(account):
#     if account in users:
#         return users[account]
#     return False
def adduser():
    li=['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    account=""
    for i in range(8):
        index =random.randint(0,len(li)-1)
        account=account+li[index]
    print("您的账户为：",account)
    name = input("请输入用户名：")
    password = input("请输入六位数字密码：")
    print("请输入您的地址：")
    country = input("\t请输入国家：")
    province = input("\t请输入省份：")
    street = input("\t请输入街道：")
    door = input("\t请输入门牌号：")

    status=bank_adduser(account,name,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
        info='''
        -------------个人信息-------------
        账号：%s
        用户名：%s
        密码：*****
        地址：
            国家：%s
            省份：%s
            街道：%s
            门牌号：%s
        余额：%s
        开户行:%s
        '''
        print(info %(account,name,country,province,street,door,users[account]["money"],bank_name))
    elif status == 2:
        print("账号已经存在，")
    elif status == 3:
        print("本行数据库已满，请到其他行办理！")


#银行存钱逻辑
def bank_savemoney(account,money):
    #用户库里有该用户，存钱
    if account in users.keys():
        users[account]['money']=users[account]['money']+money
        print("存款成功，您的余额为：",users[account]['money'])
    #没有该用户，False
    else:
        print('False')
#存钱
def savemoney():
    account=input('请输入您的存款账户：')
    money=int(input("请输入您的存款金额："))
    bank_savemoney(account,money)

#取款
def out_money():
    account = input("请输入您的账户：")
    money = users[account]['money']
    money1 = money
    money1 = int(money1)
    if account in users:
        password = input("请输入您的密码：")
    else:
        print("该账户不存在，请重新输入")
    if password == users[account]['password']:
        put_money = int(input("请输入取款金额："))
    else:
        print("输入密码错误，请重新输入")
    if money1 >= put_money:
        money1 = money1 - put_money
        print("取款成功，您的余额为:", money1)
    else:
        print("余额不足")

#银行转账
def bank_transfer(account1,account2,password,money):
    if account1 in users.keys():
        if password == users[account1]["password"]:
            if account2 in users.keys():
                if users[account1]["money"]>=money:
                    users[account1]["money"]=users[account1]["money"]-money  #1的余额
                    users[account2]["money"]=users[account2]["money"]=money   #2的余额
                    print("转账成功",money)
                    print("转出账户的金额为：",users[account1]["money"])
                    print("转入账户的金额为：",users[account2]["money"])
                else:
                    print("您的余额不足，无法转出")
            else:
                print("转入账户不存在")
        else:
            print("密码输入错误")
    else:
        print("转出账户不存在")
#转账：
def transfer():
    account1=input("请输入转出账户：")
    password=input("请输入账户密码：")
    account2=input("请输入转入账户：")
    money=int(input("请输入转账金额："))
    bank_transfer(account1,account2,password,money)

#查询
def qwery():
    account=input("请输入您的账号：")
    if account in users:
        password=input("请输入账户密码：")
        if password==users[account]['password']:
            print("-------------个人信息-------------")
            print("账号：",account)
            print("密码：*******")
            print("余额：",users[account]["money"])
            print("居住地址：",users[account]["door"])
            print("国家：",users[account]['country'])
            print("省份：",users[account]["province"])
            print("街道：",users[account]["street"])
            print("门牌号：",users[account]["door"])
            print("开户行：",bank_name)
        else:
            print('密码输入错误！')
    else:
        print("该账户不存在！")


while True:
    num = input("请输入业务编号：")
    if num.isdigit():
        num=int(num)
        if num == 1:
            adduser()
        elif num == 2:
            savemoney()
        elif num == 3:
            out_money()
        elif num == 4:
            transfer()
        elif num == 5:
            qwery()
        elif num == 6:
            print('bye')
            break
        else:
            print('输入非法')
    else:
        print('输入非法，请重新输入')