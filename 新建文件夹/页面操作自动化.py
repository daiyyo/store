import time
from selenium import  webdriver


driver = webdriver.Chrome()
#弹窗alert
'''
driver.get(r'F:/自动化框架/练习的html/弹框的验证/dialogs.html')


driver.maximize_window()

driver.find_element_by_xpath('//*[@id = "alert"]').click()

driver.switch_to.alert.accept()
'''

#弹窗confirm
'''
driver.get(r'F:/自动化框架/练习的html/弹框的验证/dialogs.html')


driver.maximize_window()

driver.find_element_by_xpath('//*[@id = "confirm"]').click()

driver.switch_to.alert.accept()

driver.switch_to.alert.dismiss()
'''




#上传文件
#
# '''
# driver.get(r'F:/自动化框架/练习的html/上传文件和下拉列表/autotest.html')
#
#
# driver.maximize_window()
#
#
# driver.find_element_by_xpath('//*[@id="accountID"]').send_keys('阿飞')
#
# driver.find_element_by_xpath('//*[@id="passwordID"]').send_keys(88888888)
#
# driver.find_element_by_xpath('//*[@id="areaID"]').click()
#
# driver.find_element_by_xpath('//*[@value="beijing"]').click()
#
# driver.find_element_by_xpath('//*[@id="sexID1"]').click()
#
# driver.find_element_by_xpath('//*[@value="summer"]').click()
#
# driver.find_element_by_xpath('//*[@name="file" and @type="file"]').send_keys(r'C:\Users\dell\Pictures\Saved Pictures\蒂法.jpg')
#
#
# time.sleep(3)
#
# driver.quit()
# '''


#跳转页面
# '''
# driver.get(r'F:/自动化框架/练习的html/跳转页面/pop.html')
#
# driver.maximize_window()
#
# driver.find_element_by_xpath('//*[@id="goo" and @href="http://www.baidu.com/"]').click()
#
# time.sleep(5)
# driver.quit()
# '''



