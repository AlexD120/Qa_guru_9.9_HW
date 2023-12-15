import allure
from selene.support.shared import browser
import pytest
from selenium import webdriver


@pytest.fixture()
def browser_config():
    browser.config.window_height = 720
    browser.config.window_width = 1080

@pytest.fixture()
def open_browser(browser_config):
    with allure.step("Открываем главную страницу"):
        browser.open('https://github.com')
    yield
    with allure.step("Закрываем браузер"):
        browser.quit()
