import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from helper import to_highlight

print('Test case started ....')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
url_ = 'http://the-internet.herokuapp.com/challenging_dom'
driver.get(url_)


table_path = "//*[@id='content']/div/div/div/div[2]/table/tbody"
t1 = driver.find_element_by_xpath(f"{table_path}/tr[3]/td[6]")
t2 = driver.find_element_by_xpath(f"{table_path}/tr[8]/td[7]/a[2]")
t3 = driver.find_element_by_xpath(f"{table_path}/tr[3]/td[7]/a[1]")
t4 = driver.find_element_by_xpath(f"{table_path}/tr[8]/td[4]")
t5 = driver.find_element_by_xpath(f"{table_path}/tr[8]/td[1]")

to_highlight(t1, 'red', 5)
to_highlight(t2, 'red', 5)
to_highlight(t3, 'red', 5)
to_highlight(t4, 'red', 5)
to_highlight(t5, 'red', 5)

driver.find_element_by_css_selector('a.button.success').send_keys(Keys.ENTER)

driver.close()
print('Test case finished ....')
