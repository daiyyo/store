'''
    1.用金钱
    2.空的购物车
    3.有足够商品
    4.正常购物
        是否有这个商品
        金钱是否足够
            添加购物车

    技术选型：
        1.判断
        2.循环
        3.容器技术
        4.输入input
        5.打印
    任务1：
        10张联想优惠券，0.5
        20张老干妈优惠券：0.6
        10张乌江榨菜优惠券，0.9
    最后使用优惠券来结算。
'''

import random
lenovo = ['联想电脑',0.5]
laoganma = ['老干妈',0.6]
zhacai = ['乌江榨菜',0.9]
discount = []
for i in range(10):
    discount.append(lenovo)
for i in range(20):
    discount.append(laoganma)
for i in range(10):
    discount.append(zhacai)
count = random.sample(discount,1)
count1 = count[0]
print(f'恭喜你抽到{count1}')


#购买
shop = [
    ["联想电脑",4500],
    ["Mac Pc",12000],
    ["HUA WEI WATCH",1200],
    ["海尔洗衣机",5000],
    ["卫龙辣条",3.5],
    ["老干妈",15],
    ["乌江榨菜",1.5]
]
money=int(input("请输入您的金额："))
mycart=[]
i=0

while i<10:
    print("------全部商品------")
    print(" 编号" " 商 品 ""  价 格 ")
    for key,value in enumerate(shop):
        print(key,value)
    chose=input("请输入您想要购买商品的编号：")
    if chose.isdigit():
        chose=int(chose)
        if chose > len(shop) or chose<0:
            print("您输入的商品不存在，请重新输入！！")
        else:
            if money < shop[chose][1]:
                print('余额不足')
            else:
                mycart.append(shop[chose])
                if shop[chose][0] == coupon[ch][0]:
                    money= money - shop[chose][1] * coupon[ch][1]
                else:
                    money=money-shop[chose][1]

                print("加人购物车成功，您的余额还有",money)

    elif chose=="q":
        print("欢迎下次光临！")
        break


    else:
        print("输入非法")
print("购物小票！")
for key,value in enumerate(mycart):
    print(key,value)
print("您的余额还有",money,"!欢迎下次光临")



