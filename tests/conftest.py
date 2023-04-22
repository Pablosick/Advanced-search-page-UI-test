import pytest

from selenium import webdriver

from security.private import PATH


@pytest.fixture(scope="session")
def data_supply():
    driver = webdriver.Chrome(executable_path=PATH)
    yield driver
    driver.close()
    driver.quit()
