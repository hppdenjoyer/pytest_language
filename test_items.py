import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_add_to_basket_button_exists(browser):
    link = "https://selenium1py.pythonanywhere.com/" \
       "catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)

    try:
        add_to_basket_button = browser.find_element(
            By.CSS_SELECTOR, "button.btn-add-to-basket"
        )
    except NoSuchElementException:
        pytest.fail("Кнопка добавления в корзину не найдена на странице")

    # Кнопка добавления в корзину отображается
    assert add_to_basket_button.is_displayed()
    # Кнопка добавления в корзину активна
    assert add_to_basket_button.is_enabled()
