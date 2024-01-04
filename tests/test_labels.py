import allure
import pytest
from selene import be, by, have
from selene.support.shared.jquery_style import s
from conftest import open_browser


@pytest.mark.usefixtures("open_browser")
def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(allure.severity_level.BLOCKER)
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