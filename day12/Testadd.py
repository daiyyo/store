from unittest import TestCase
from Clac import Calc

class TestCalc(TestCase):
    def testadd1(self):
        num1=9
        num2=12
        num=21
        c=Calc()
        s=c.add(num1,num2)
        self.assertEqual(num,s)
    def testadd2(self):
        num1=-9
        num2=-12
        num=-21
        c=Calc()
        s=c.add(num1,num2)
        self.assertEqual(num,s)

    def testadd3(self):
        num1=12
        num2=-9
        num=3
        c=Calc()
        s=c.add(num1,num2)
        self.assertEqual(num,s)


    def testadd4(self):
        num1=-2
        num2=-9
        num=-11
        c=Calc()
        s=c.add(num1,num2)
        self.assertEqual(num,s)

    def testadd5(self):
        num1=100000000000000000000000098
        num2=100
        num=100000000000000000000000198
        c=Calc()
        s=c.add(num1,num2)
        self.assertEqual(num,s)




