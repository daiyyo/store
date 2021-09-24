

class oldphone():
     __brand=''
     def setbrand(self,brand):
         self.__brand=brand
     def getbrand(self):
         return self.__brand

     def call(self,phonenumber):
         print('正在给',phonenumber,'打电话')


class newphone(oldphone):
    def call(self,phonenumber):
         print('语音拨号中……')
         super().call(phonenumber)


    def show(self):
        print('品牌为：',self.getbrand(),'的手机很好用……')


class test():
    p=newphone()
    p.setbrand('华为')
    p.call(123)
    p.show()


class chef():
    __name=''
    __age=''
    def setname(self,name):
        self.__name = name

    def getname(self):
        return self.__name

    def setage(self,age):
        self.__age = age

    def getage(self):
        return self.__age
    def makerice(self):
        pass
        # print('蒸饭')
class chefson(chef):
    def fay(self):
        pass
        # print('炒菜')
class cook(chefson):#子类的子类
    def makerice(self):
        super().makerice()
        print('蒸饭')
    def fay(self):
        print('炒菜')
class test:
    c = chef()
    c.setname("张三")
    c.setage(44)
    print(c.getname(),c.getage())






class human():
    name=''
    age=0
    def work(self):
        print(self.age,'岁的',self.name,'在工地搬砖')
    def learn(self):
        print(self.age,'岁的',self.name,'在教室做wusan')
    def sing(self):
        print(self.age,'岁的',self.name,'在唱歌')
class worker(human):
    def work(self):
        super().work()
class student(human):
    def learn(self):
        super().learn()
    def sing(self):
        super().sing()

w = worker()
w.name='张一'
w.age=45
w.work()

s = student()
s.name='张翼'
s.age=8
s.sing()

s1 = student()
s1.name='lisa'
s1.age=18
s1.learn()








