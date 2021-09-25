
    # 三个厨师，同时造蛋挞，每造一个放进篮子。篮子满，等三秒，判断是否已满，（篮子能装500个蛋挞）
    # 六个人，每人有3000元，一个蛋挞两元，蛋挞不够时等待两秒，直至钱花光
import threading
import time
from threading import Thread
lock=threading.Lock()
basket=0

class chef(Thread):
    user=''
    def run(self) -> None:
        global basket
        while True:
            if basket>=500:
                print('篮子满了，稍等')
                time.sleep(3)
            else:
                with lock:
                    basket = basket + 1
                    print("篮子中还有",basket,"个蛋挞")


class cake(Thread):
    name = ''
    count = 0
    money=3000
    def run(self) -> None:
        global money
        global basket
        while True:
            if self.money > 0:
                if basket > 0 and basket <=500:
                    self.money = self.money - 2
                    self.count = self.count + 1
                    basket = basket - 1
                    print(self.name,'您的余额为',self.money,'您现在有',self.count,'个蛋挞')
                else:
                    print('等一下')
                    time.sleep(2)

            else:
                print('余额不足')
                break
u1 = chef()
u2 = chef()
u3 = chef()

u1.setDaemon(True)
u2.setDaemon(True)
u3.setDaemon(True)


c1 = cake()
c2 = cake()
c3 = cake()
c4 = cake()
c5 = cake()
c6 = cake()



u1.start()
u2.start()
u3.start()

c1.name = 'a'
c2.name = 'b'
c3.name = 'c'
c4.name = 'r'
c5.name = 'g'
c6.name = 'e'

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()





