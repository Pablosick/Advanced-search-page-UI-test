from BasePage.ResultPage import ResultPage

from selenium.webdriver.common.by import By


class MovieParameters:
    CHROME_LOCATOR_ELEMENTS_NAME = (By.XPATH, '//div[@class="search_results search_results_last"]//p[@class="name"]/a')
    CHROME_LOCATOR_ELEMENTS_OPTIONS = (By.XPATH, '//*[@id="block_left_pad"]/div/div[3]/div/div/span[2]')



class SearchParameters(ResultPage):


    def examination_name(self, elem, name):
        return name in self.checking_options_name(MovieParameters.CHROME_LOCATOR_ELEMENTS_NAME)[elem].text


    def examination_options(self, opt, elem_country, elem_genre):
        film_country = elem_country in self.checking_options_elements(MovieParameters.CHROME_LOCATOR_ELEMENTS_OPTIONS)[opt].text
        film_genre = elem_genre in self.checking_options_elements(MovieParameters.CHROME_LOCATOR_ELEMENTS_OPTIONS)[opt].text
        return film_country and film_genre


    def check_films(self, name, country, genre):
        for i in range(5):
            if self.examination_name(i, name) and self.examination_options(i, country, genre):
                return f"Искомый фильм {self.examination_name(i, name)} в топ 5 выдачи результата поиска"
            else:
                return f"Искомый фильм {self.examination_name(i, name)} не найден в топ 5 выдачи результата поиска"