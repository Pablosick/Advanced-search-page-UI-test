import allure
from allure_commons.types import AttachmentType

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conf.message import ErrorMessage


class AdvancedSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.kinopoisk.ru/s/"

    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=ErrorMessage.LackOfLocator.value,
        )

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def screenshot(self, step, name, attachment_type=AttachmentType.PNG):
        with allure.step(step):
            allure.attach(self.driver.get_screenshot_as_png(), name, attachment_type)
