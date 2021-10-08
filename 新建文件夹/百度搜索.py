import time
from selenium import  webdriver


driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')
driver.find_element_by_xpath('//*[@id="kw" and @name="wd" and @class="s_ipt"]').send_keys('玫瑰花')


time.sleep(10)

driver.find_element_by_xpath('//*[@value="百度一下"]').click()

time.sleep(3)

driver.quit()