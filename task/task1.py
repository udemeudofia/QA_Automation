from selenium.webdriver.common.keys import Keys


def task_1(url_, driver):
    print('Test case started ....')
    driver.get(url_)
    driver.find_element_by_name('sf_TextFilter').send_keys('Panic')
    driver.find_element_by_xpath("//*[@id='dropdownMenu3']").send_keys(Keys.ARROW_DOWN)
    driver.find_element_by_xpath("//*[@id='search-city']/div[2]/div/div/div/div/ul/li[3]/a[text()='Kaunas']").click()
    driver.find_element_by_name('sf_DateFrom').send_keys('2020-09-01')
    driver.find_element_by_name('sf_DateTo').send_keys('2021-12-31')
    driver.find_element_by_css_selector('button.bn.btn-lg.btn-red.text-uppercase').send_keys(Keys.ENTER)
    driver.implicitly_wait(2)
    driver.find_element_by_id('btnBuy-22396').click()
    driver.find_element_by_xpath("//*[@id='main-container']/div/div/div/div[2]/div/div[1]/div/div[12]/div[2]/div/div[4]/div/div/a").click()
    # driver.close()
    return 'Test case finished ....'


if __name__ == '__main__':
    task_1()
