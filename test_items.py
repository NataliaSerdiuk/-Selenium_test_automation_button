import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_button_add_to_basket_existence(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button_add_to_basket_list = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    button = len(button_add_to_basket_list)
    assert button > 0, "There is no add to cart button"