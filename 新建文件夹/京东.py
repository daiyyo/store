

import time
from selenium import  webdriver


driver = webdriver.Chrome()

driver.get("https://www.jd.com/")

driver.maximize_window()
driver.find_element_by_xpath('//*[@type="text" and @autocomplete="off" and @id="key" and @accesskey="s"]').send_keys('电脑')
driver.find_element_by_xpath('//*[@clstag="h|keycount|head|search_a"]').click()
driver.find_element_by_xpath('//*[@src="//img12.360buyimg.com/n7/jfs/t1/196320/2/11808/263537/60e42411E1d16d7c4/4fea9c086bb802e2.jpg"]').click()

time.sleep(10)
driver.quit()