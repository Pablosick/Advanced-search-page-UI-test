import allure
from allure_commons.types import AttachmentType

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conf.message import ErrorMessage

from BasePage.AdvancedSearchPage import AdvancedSearchPage


class ResultPage(AdvancedSearchPage):

    def checking_options_elements(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=ErrorMessage.LackOfLocator.value)


    def checking_options_name(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=ErrorMessage.LackOfLocator.value)