from unittest import TestCase
from Clac import Calc

class Testdevision(TestCase):
    def testdev1(self):
        num1=8
        num2=2
        num=4

        c=Calc()
        r=c.devision(num1,num2)
        self.assertEqual(num,r)

    def testdev2(self):
        num1=-90
        num2=-3
        num=30

        c=Calc()
        r=c.devision(num1,num2)
        self.assertEqual(num,r)



    def testdev3(self):
        num1=-88
        num2=2
        num=-44

        c=Calc()
        r=c.devision(num1,num2)
        self.assertEqual(num,r)



    def testdev4(self):
        num1=66.6
        num2=-3
        num=-22.8

        c=Calc()
        r=c.devision(num1,num2)
        self.assertEqual(num,r)


















