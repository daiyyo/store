from unittest import TestCase
from Clac import Calc

class Testminus(TestCase):
    def testminus1(self):
        num1=10
        num2=3
        num=7

        d=Calc()
        m=d.minus(num1,num2)

        self.assertEqual(num,m)

    def testminus2(self):
        num1=-10
        num2=-9
        num=-1

        d=Calc()
        m=d.minus(num1,num2)
        self.assertEqual(num,m)

    def testminus3(self):
        num1=10
        num2=-10
        num=9

        d=Calc()
        m=d.minus(num1,num2)
        self.assertEqual(num,m)
    def teatminus4(self):
        num1=-10
        num2=2
        num=-12

        d=Calc()
        m=d.minus(num1,num2)
        self.assertEqual(num,m)

    def testminus5(self):
        num1=999999999999999999999999
        num2=1
        num=999999999999999999999998

        d=Calc()
        S=d.minus(num1,num2)
        self.assertEqual(num,S)