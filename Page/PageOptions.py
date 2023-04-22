from BasePage.AdvancedSearchPage import AdvancedSearchPage

from selenium.webdriver.common.by import By


class ChromeSearchLocators:
    CHROME_LOCATOR_SEARCH_NAME = (By.ID, "find_film")
    CHROME_LOCATOR_SEARCH_COUNTRY = (By.XPATH, '//div//select[@id="country"]/option[@value="1"]')
    CHROME_LOCATOR_SEARCH_GENRE = (By.XPATH, '//div//select[@id="m_act[genre]"]/option[@value="8"]')
    CHROME_LOCATOR_FIND_BUTTON = (By.XPATH, '//input[@class="el_18 submit nice_button"]')


class SearchHelper(AdvancedSearchPage):


    def find_by_name(self, name):
        movie_title = self.find_element(ChromeSearchLocators.CHROME_LOCATOR_SEARCH_NAME)
        movie_title.send_keys(name)
        return movie_title


    def find_by_country(self):
        country_selection = self.find_element(ChromeSearchLocators.CHROME_LOCATOR_SEARCH_COUNTRY)
        country_selection.click()
        return country_selection


    def find_by_genre(self):
        genre_selection = self.find_element(ChromeSearchLocators.CHROME_LOCATOR_SEARCH_GENRE)
        genre_selection.click()
        return genre_selection


    def find_button(self):
        enter_button = self.find_element(ChromeSearchLocators.CHROME_LOCATOR_FIND_BUTTON)
        enter_button.click()
        return enter_button