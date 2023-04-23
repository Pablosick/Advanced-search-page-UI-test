from BasePage.AdvancedSearchPage import AdvancedSearchPage

from selenium.webdriver.common.by import By


class ChromeSearchLocators:

    CHROME_LOCATOR_SEARCH_NAME = (By.ID, "find_film")
    CHROME_LOCATOR_FIND_BUTTON = (By.XPATH, '//input[@class="el_18 submit nice_button"]')

    def country(self, title):
        chrome_locator_search_country = (By.XPATH, f'//div//select[@id="country"]/option[@value=contains(text(),"{title}")]')
        return chrome_locator_search_country


    def genre(self,title):
        chrome_locator_search_genre = (By.XPATH, f'//div//select[@id="m_act[genre]"]/option[@value=contains(text(), "{title}")]')
        return chrome_locator_search_genre



class SearchHelper(AdvancedSearchPage):


    def find_by_name(self, name):
        movie_title = self.find_element(ChromeSearchLocators.CHROME_LOCATOR_SEARCH_NAME)
        movie_title.send_keys(name)
        return movie_title


    def find_by_country(self, country):
        country_film = ChromeSearchLocators()
        country_selection = self.find_element(country_film.country(country))
        country_selection.click()
        return country_selection


    def find_by_genre(self, genre):
        genre_film = ChromeSearchLocators()
        genre_selection = self.find_element(genre_film.genre(genre))
        genre_selection.click()
        return genre_selection


    def find_button(self):
        enter_button = self.find_element(ChromeSearchLocators.CHROME_LOCATOR_FIND_BUTTON)
        enter_button.click()
        return enter_button