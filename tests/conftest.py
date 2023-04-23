import pytest
import json

from selenium import webdriver

from security.private import chrome_service, o_json


@pytest.fixture(scope="session")
def driver_supply():
    driver = webdriver.Chrome(service=chrome_service)
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture(scope="session")
def data_supply():
    with open(f"{o_json}", encoding="utf8") as opt_films:
        opt_film = json.load(opt_films)['data']
    return opt_film