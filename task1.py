import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
print('Test case started ....')
# driver = webdriver.Chrome(r"C:\Users\Udeme\PycharmProjects\QA_Engineer\Browsers\chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.tiketa.lt/EN/search')
driver.find_element_by_name('sf_TextFilter').send_keys('Forum')
time.sleep(3)
driver.find_element_by_xpath("//*[@id='dropdownMenu3']").send_keys(Keys.ARROW_DOWN)
time.sleep(3)
driver.find_element_by_xpath("//*[@id='search-city']/div[2]/div/div/div/div/ul/li[3]/a[text()='Kaunas']").click()
time.sleep(3)
driver.find_element_by_name('sf_DateFrom').send_keys('2020-09-01')
driver.find_element_by_name('sf_DateTo').send_keys('2021-12-31')
time.sleep(3)
driver.find_element_by_css_selector('button.bn.btn-lg.btn-red.text-uppercase').send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
print('Test case finished ....')