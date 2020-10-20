# type: ignore
"""Setting up fixtures to be used for testing"""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def setup():
    """Gets the appropriate chrome webdriver"""
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.close()
