import allure
import pytest
from selene import browser, be, by, have
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@pytest.mark.usefixtures("open_browser")
def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Проверка наличия текста 'by AlexD120' в Issue")
    allure.dynamic.link("https://github.com", name="Testing")
    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("AlexD120/Qa_guru_9.9").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("AlexD120/Qa_guru_9.9")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 1 и содержание текста - by AlexD120"):
        s(by.partial_text("#1")).should(be.visible).should(have.text("by AlexD120"))


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Davydov")
@allure.feature("Задачи в репозитории")
@allure.story("Проверка наличия текста 'by AlexD120' в Issue")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    open_main_page("https://github.com")
    search_for_repository("AlexD120/Qa_guru_9.9")
    go_to_repository("AlexD120/Qa_guru_9.9")
    open_issue_tab()
    should_see_issue_with_number("#1", "by AlexD120")
    close_browser()


@allure.step("Открываем главную страницу")
def open_main_page(page):
    browser.open(page)


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo).submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number} и содержание текста - by AlexD120")
def should_see_issue_with_number(number, text):
    s(by.partial_text(number)).should(be.visible).should(have.text(text))


@allure.step("Закрываем браузер")
def close_browser():
    browser.close()
