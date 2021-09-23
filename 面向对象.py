'''
    分析一个水杯的属性和功能，使用类描述并创建对象
        高度，容积，颜色，材质
        能存放液体

'''
class cup:
    high=''
    capacity=''
    color=''
    material=''
    liquid=''

    def carry(self):
        print('水杯中可容纳',self.capacity,'的',self.liquid)
c=cup()
c.high='20cm'
c.capacity='5l'
c.color='白色'
c.material='玻璃'
c.liquid='水'
c.carry()


'''
    有笔记本电脑
        屏幕大小，价格，cpu型号，内存大小，待机时长
        行为（打字，打游戏，看视频）
'''
class notebook:
    screen=''
    price=0
    cpu=''
    size=''
    time=0
    def type(self):
        print('待机时长还有',self.time,'价格',self.price,'cpu',self.cpu)

    def game(self):
        print('待机时长还有',self.time,'价格',self.price,'cpu',self.cpu)
    def movie(self):
        print('待机时长还有',self.time,'价格',self.price,'cpu',self.cpu)
n=notebook()
n.time=1.5
n.price=3000
n.cpu=1
n.size='30.0Gb'
n.screen=12.5
n.type()

n1=notebook()
n1.size='1.0g'
n1.price=5000
n1.screen=2.5
n1.time=14
n1.cpu=2
n1.game()

m=notebook()
m.time=1.5
m.price=3000
m.cpu=3
m.size='30.0Gb'
m.screen=12.5
m.movie()


'''
    定义了一个学生类：
        属性:学号，姓名，年龄，性别，身高，体重，成绩，家庭地址，电话号码。
        行为：
            学习（要求参数传入学习的时间），
            玩游戏（要求参数传入游戏名），
            编程（要求参数传入写代码的行数），
            数的求和（要求参数用变长参数来做，返回求和结果）
'''
class student:
    __sn=''
    name=''
    __age=0
    __sex=''
    __high=0.0
    __weight=0.0
    __score=0.0
    __address=''
    __phonenumber=''
    def study(self,hour):
        print('学生',self.name,'已经学习了',hour,'小时')
    def game(self,gamename):
        print('学生',self.name,'正在玩',gamename)
    def program(self,line):
        print(self.name,'正在编程','已经写了',line,'行了')
    def addnum(self):
        pass

s=student()
s.sn='006'
s.name='张三'
s.age=19
s.sex='男'

s.study(3)
s.game('TIMI')
s.program(2)
s.addnum()

'''
ii.	车类：
    属性：车型号，车轮数，车身颜色，车重量，油箱存储大小 。
    功能：跑（要求参数传入车的具体功能，比如越野，赛车）
        创建：法拉利，宝马，铃木，五菱，拖拉机对象
'''
class car:
    brand=''
    wheel=0
    color=''
    weight='0g'
    size=0.0
    def run(self,use):
        print(self.brand,'的车能够',use)

c=car()
c.brand='法拉利'
c.wheel=4
c.color='黄色'
c.weight="500g"
c.size=50
c.run('赛车')

a=car()
a.brand='宝马'
a.wheel=4
a.color='黑色'
a.weight='200g'
a.size=50
a.run('通勤')

b=car()
b.brand='铃木'
b.wheel=4
b.color='黑色'
b.weight='200g'
b.size=50
b.run('越野')

d=car()
d.brand='五菱'
d.wheel=4
d.color='黑色'
d.weight='200g'
d.size=50
d.run('越野')

e=car()
e.brand='拖拉机'
e.wheel=4
e.color='黑色'
e.weight='200g'
e.size=50
e.run('拉货')

'''
    笔记本：
        属性：型号，待机时间，颜色，重量，cpu型号，内存大小，硬盘大小。  
        行为：打游戏（传入游戏的名称）,办公。
'''
class computer:
    type=''
    time=0
    color=''
    weight=''
    cpu=0
    size=0
    disk=0

    def game(self,gamename):
        print(self.cpu,'的电脑玩',gamename,'不卡')
    def work(self):
        print(self.cpu,'的电脑进行办公')



'''
    猴子类：
	    属性：类别，性别，身体颜色，体重。
	    行为：造火（要求传入造火的材料：比如木棍还是石头），
	        学习事物（要求参数传入学习的具体事物，可以不止学习一种事物）
'''
class monkey:
    kind=''
    __sex=''
    __color=''
    __weight=0.0

    def fire(self,material):
        print(self.kind,'可以用',material,'造火')
    def study(self,learn):
        print(self.kind,'可以学习使用',learn)
m=monkey()
m.kind='长臂猿'
m.color='黄色'
m.fire('石头')

m1=monkey()
m1.kind='金丝猴'
m1.color='黄色'
m1.study('电脑')













