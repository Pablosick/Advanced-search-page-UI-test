import allure

from Page.PageOptions import SearchHelper
from Page.MoviesPage import SearchParameters


@allure.feature("Open pages")
@allure.story('Открытие страницы расширенного поиска на сайте "Кинопоиск"')
@allure.severity("normal")
@allure.title("Поиск фильма с указанными параметрами")
def test_film_search(driver_supply, data_supply):
    """
    Insert advanced search page options
    """
    chrome_search_page = SearchHelper(driver_supply)
    chrome_search_page.go_to_site()
    chrome_search_page.find_by_name(data_supply["film_title"])
    chrome_search_page.screenshot("Шаг 1. Ввод имени фильма", "Entering_name")
    chrome_search_page.find_by_country(data_supply["country"])
    chrome_search_page.screenshot("Шаг 2. Выбор страны", "Entering_country")
    chrome_search_page.find_by_genre(data_supply["genres"])
    chrome_search_page.screenshot("Шаг 3. Выбор жанра", "Entering_country")
    chrome_search_page.find_button()


@allure.feature("Open pages")
@allure.story('Открытие страницы расширенного поиска на сайте "Кинопоиск"')
@allure.severity("normal")
@allure.title("Полученный результат и поиск нужного фильма")
def test_movie_result(driver_supply, data_supply):
    """
     Is there a movie on the advanced search page
    """
    check_list_films = SearchParameters(driver_supply)
    check_list_films.screenshot("Полученные фильмы", "lists_films")
    assert check_list_films.check_films(data_supply["film_title"], data_supply["country"], data_supply["genres"])
