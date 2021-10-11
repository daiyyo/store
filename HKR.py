from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
#注册
# driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()
# driver.find_element_by_xpath("//*[@id='loginname']").send_keys('dyy')
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys("daiyao")
# driver.find_element_by_xpath("//*[@id='pwd']").send_keys("123456")
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys("123456")
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()
#
# driver.find_element_by_xpath("//*[@id='valid_age']").send_keys("23")
#
# select=driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/select[1]")
# time.sleep(1)
# select.find_element_by_xpath("//option[@value='女']").click()
#
# select=driver.find_element_by_xpath("//*[@id='classname']")
# select.find_element_by_xpath("//option[@value='Python自动化']").click()
#
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()
#
# driver.find_element_by_xpath('//*[@id="reg_mail"]').send_keys('123456654@qq.com')
# driver.find_element_by_xpath('//*[@id="reg_phone"]').send_keys('13543245632')
# driver.find_element_by_xpath('//*[@id="msform"]/fieldset[3]/textarea').send_keys('beijing')
# driver.find_element_by_xpath('//*[@id="btn_reg"]').click()
# time.sleep(3)

#教师登录
driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a[2]').click()
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('qiaoyueyang')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="submit"]').click()
'''
#教师管理
driver.find_element_by_xpath('//*[@id="_easyui_tree_11"]/span[4]/a').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="sear_teaname"]').send_keys("李艳")

driver.find_element_by_xpath('//*[@id="search_user"]/span/span[1]').click()
time.sleep(1)
#重置密码
driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[9]/div/a').click()
time.sleep(1)
driver.switch_to.alert.accept()
'''
'''
#学生管理
# driver.find_element_by_xpath('//*[@id="_easyui_tree_12"]/span[4]/a').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="J-stu"]').send_keys('jason')
#
# driver.find_element_by_xpath('//*[@id="J-phone"]').send_keys('13548554150')
# driver.find_element_by_xpath('//*[@id="stu_panel"]/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]').click()
# time.sleep(2)
#设置未毕业
# driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[11]').click()
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[8]/div[3]/a').click()
#设置毕业
driver.find_element_by_xpath('//*[@id="_easyui_tree_12"]/span[4]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-4"]/td[11]/div/a').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[8]/div[3]/a').click()
'''
'''
#课程管理
driver.find_element_by_xpath('//*[@id="_easyui_tree_13"]/span[4]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="course_panel"]/div/div/div[1]/table/tbody/tr/td/a/span').click()
driver.find_element_by_xpath('//*[@id="course_form_add"]/table/tbody/tr[1]/td[2]/input').send_keys('英')
driver.find_element_by_xpath('//*[@id="course_form_add"]/table/tbody/tr[2]/td[2]/textarea').send_keys('ENGLISH')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[7]/div[3]/a[1]/span').click()
driver.find_element_by_xpath('/html/body/div[10]/div[3]/a').click()
#取消添加
# driver.find_element_by_xpath('/html/body/div[7]/div[3]/a[2]/span').click()
# time.sleep(2)
'''
'''
#评价
driver.find_element_by_xpath('//*[@id="_easyui_tree_15"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="J-xl"]').click()
driver.find_element_by_xpath('//*[@id="laydate_YY"]/a[1]').click()
driver.find_element_by_xpath('//*[@id="laydate_YY"]/a[1]').click()
driver.find_element_by_xpath('//*[@id="laydate_MM"]/a[2]').click()
driver.find_element_by_xpath('//*[@id="laydate_table"]/tbody/tr[4]/td[1]').click()
driver.find_element_by_xpath('//*[@id="eva"]/div/div/div[1]/table/tbody/tr/td[2]/a/span').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="eva"]/div/div/div[1]/table/tbody/tr/td[4]/a/span').click()
'''



'''
#用户登录
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('lhs')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="submit"]').click()
#修改头像
# driver.find_element_by_xpath('//*[@id="img"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="ul_pic"]/li[8]').click()
# time.sleep(2)
#上传头像
# driver.find_element_by_xpath('//*[@id="img"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@name="pic"]').send_keys(r'F:\python自动化测试\自动化\dagongren.jpg')
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="pic_btn"]').click()



#提交评价
select=driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]/select")
select.find_element_by_xpath("//option[@value='9']").click()
time.sleep(2)
select=driver.find_element_by_xpath('//*[@id="tea_td"]/select')
select.find_element_by_xpath("//option[@value='贾生']").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[5]/td[3]/div/label[2]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[10]/td[3]/div/label[4]/div').click()
driver.find_element_by_xpath('//*[@id="subtn"]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[7]/div[3]/a').click()
time.sleep(1)


# 查询同学
# driver.find_element_by_xpath("//*[@id='_easyui_tree_10']").click()

# 修改信息
# driver.find_element_by_xpath("//*[@id='_easyui_tree_8']").click()
#
# ac = ActionChains(driver)
#
# age = driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']")
#
# ac.double_click(age).send_keys("34").perform()
# ac.release()
# driver.find_element_by_xpath("//*[@id='btn_modify']").click()
#
#
# driver.quit()
'''













