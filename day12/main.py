from HTMLTestRunner import HTMLTestRunner
import unittest


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


#加载用例
tests=unittest.defaultTestLoader.discover(r"E:\python\selenium\daima\day12",pattern="Test*.py")

#创建运行器
runner=HTMLTestRunner.HTMLTestRunner(
    title='计算器测试报告',
    description='加减乘除',
    verbosity=1,
    stream=open(file='计算器报告.html',mode="w+",encoding='utf-8')
)

runner.run(tests)


if __name__ == '__main__':

    fromaddr = '995716382@qq.com'
    password = 'amujinpiqizfbfhj'
    toaddrs = ['13552648187@163.com']

    pdfFile = '计算器报告.html'
    pdfApart = MIMEApplication(open(pdfFile,'rb').read())
    pdfApart.add_header('Content-Disposition','attachment',filename = pdfFile)

    m = MIMEMultipart()
    m.attach(pdfApart)
    m['Subject'] = '计算器报告'


    try:
        sever = smtplib.SMTP('smtp.qq.com')
        sever.login(fromaddr,password)
        sever.sendmail(fromaddr,toaddrs,m.as_string())
        print('success')
        sever.quit()
    except smtplib.SMTPException as e:
        print('error',e)









    # try:
    #     sever = smtplib.SMTP('smtp.qq.com')
    #     sever.login(fromaddr,password)
    #     sever.sendmail(fromaddr,toaddrs,m.as_string())
    #     print('success')
    #     sever.quit()
    # except smtplib.SMTPException as e:
    #     print('error',e)








