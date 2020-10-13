import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
print('Test case started ....')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/challenging_dom')
time.sleep(3)

def to_highlight(element, duration, color, border_size):
    """Highlights a web element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border_size, color))
    time.sleep(duration)
    apply_style(original_style)

table_path = "//*[@id='content']/div/div/div/div[2]/table/tbody"
t1 = driver.find_element_by_xpath(f"{table_path}/tr[3]/td[6]")
t2 = driver.find_element_by_xpath(f"{table_path}/tr[8]/td[7]/a[2]")
t3 = driver.find_element_by_xpath(f"{table_path}/tr[3]/td[7]/a[1]")
t4 = driver.find_element_by_xpath(f"{table_path}/tr[8]/td[4]")
t5 = driver.find_element_by_xpath(f"{table_path}/tr[8]/td[1]")

to_highlight(t1, 2, 'red', 5)
to_highlight(t2, 2, 'red', 5)
to_highlight(t3, 2, 'red', 5)
to_highlight(t4, 2, 'red', 5)
to_highlight(t5, 2, 'red', 5)
# time.sleep(2)
driver.find_element_by_css_selector('a.button.success').send_keys(Keys.ENTER)

time.sleep(5)
driver.close()
print('Test case finished ....')