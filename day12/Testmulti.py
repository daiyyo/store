from unittest import TestCase
from Clac import Calc

class Testmulti(TestCase):
    def testmulti1(self):
        num1=2
        num2=40
        num=80

        c=Calc()
        r=c.multi(num1,num2)
        self.assertEqual(num,r)

    def testmulti2(self):
        num1=-20
        num2=-4
        num=80

        c=Calc()
        r=c.multi(num1,num2)
        self.assertEqual(num,r)

    def testmulit3(self):
        num1=20
        num2=-8
        num=-160

        c=Calc()
        r=c.multi(num1,num2)
        self.assertEqual(num,r)


    def testmulit4(self):
        num1=-20
        num2=8
        num=-160

        c=Calc()
        r=c.multi(num1,num2)
        self.assertEqual(num,r)

    def testmulit5(self):
        num1=20.6
        num2=-8
        num=-164.8

        c=Calc()
        r=c.multi(num1,num2)
        self.assertEqual(num,r)











