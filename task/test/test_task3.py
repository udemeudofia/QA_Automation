# type: ignore
"""
UI testing on task 3
"""
from selenium.webdriver.common.keys import Keys
from task.helper import to_highlight


def task_3(url_, driver):
    """The test function"""
    print("Test case started ....")
    driver.get(url_)
    table_path = "//*[@id='content']/div/div/div/div[2]/table/tbody"
    path1 = driver.find_element_by_xpath(f"{table_path}/tr[3]/td[6]")
    path2 = driver.find_element_by_xpath(f"{table_path}/tr[8]/td[7]/a[2]")
    path3 = driver.find_element_by_xpath(f"{table_path}/tr[3]/td[7]/a[1]")
    path4 = driver.find_element_by_xpath(f"{table_path}/tr[8]/td[4]")
    path5 = driver.find_element_by_xpath(f"{table_path}/tr[8]/td[1]")

    to_highlight(path1, "red", 5)
    to_highlight(path2, "red", 5)
    to_highlight(path3, "red", 5)
    to_highlight(path4, "red", 5)
    to_highlight(path5, "red", 5)

    driver.find_element_by_css_selector("a.button.success").send_keys(Keys.ENTER)
    return "Test case finished ...."


def test_3(setup):
    """UI testing on a specific url using pytest"""
    assert (
        task_3("http://the-internet.herokuapp.com/challenging_dom", setup)
        == "Test case finished ...."
    )
