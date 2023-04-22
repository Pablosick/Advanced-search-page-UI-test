import allure

from Page.PageOptions import SearchHelper


@allure.feature("Open pages")
@allure.story('Открытие страницы расширенного поиска на сайте "Кинопоиск"')
@allure.severity("normal")
def test_film_search(data_supply):
    """
    Insert advanced search page options
    """
    chrome_search_page = SearchHelper(data_supply)
    chrome_search_page.go_to_site()
    chrome_search_page.find_by_name("Загадочная ")
    chrome_search_page.screenshot("Шаг 1. Ввод имени фильма", "Entering_name")
    chrome_search_page.find_by_country()
    chrome_search_page.screenshot("Шаг 2. Выбор страны", "Entering_country")
    chrome_search_page.find_by_genre()
    chrome_search_page.screenshot("Шаг 3. Выбор жанра", "Entering_country")
    chrome_search_page.find_button()