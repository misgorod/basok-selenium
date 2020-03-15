import pytest
from selenium import webdriver
from time import sleep
import re

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    try:
        driver.get('http://onlinepasswordgenerator.ru')
        yield driver
    finally:
        driver.close()

def check_num(driver, checked):
    gen_numbers_checkbox = driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[3]/div[1]/form/fieldset/label[1]/input")
    if gen_numbers_checkbox.is_selected() != checked:
        gen_numbers_checkbox.click()

def check_upper(driver, checked):
    gen_uppercase_checkbox = driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[3]/div[1]/form/fieldset/label[2]/input")
    if gen_uppercase_checkbox.is_selected() != checked:
        gen_uppercase_checkbox.click()

def check_lower(driver, checked):
    gen_lowercase_checkbox = driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[3]/div[1]/form/fieldset/label[3]/input")
    if gen_lowercase_checkbox.is_selected() != checked:
        gen_lowercase_checkbox.click()

def check_special(driver, checked):
    gen_special_checkbox = driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[3]/div[1]/form/fieldset/label[4]/input")
    if gen_special_checkbox.is_selected() != checked:
        gen_special_checkbox.click()

def generate(driver):
    generate_button = driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[3]/input")
    generate_button.click()

def get_passwords(driver):
    return driver.find_elements_by_xpath("//*[@id=\"content\"]/div/div[3]/ul/li")

def get_message(driver):
    return driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[3]/h3").text

def set_password_length(driver, value):
    input = driver.find_element_by_xpath("//*[@id=\"content\"]/div/div[3]/div[1]/form/fieldset/label[5]/input")
    input.clear()
    input.send_keys(value)

def test_generate_singlenumber(driver):
    check_num(driver, True)
    check_upper(driver, False)
    check_lower(driver, False)
    check_special(driver, False)
    set_password_length(driver, 1)
    generate(driver)
    passwords = get_passwords(driver)
    assert len(passwords) == 10
    assert all([len(password.text) == 1 for password in passwords])

def test_generate_allsamelength(driver):
    check_num(driver, True)
    check_upper(driver, False)
    check_lower(driver, False)
    check_special(driver, False)
    set_password_length(driver, 99)
    generate(driver)
    passwords = get_passwords(driver)
    assert len(passwords) == 10
    assert all([len(password.text) == 99 for password in passwords])

def test_generate_anycontainlower(driver):
    check_num(driver, True)
    check_upper(driver, True)
    check_lower(driver, True)
    check_special(driver, True)
    set_password_length(driver, 1)
    generate(driver)
    passwords = get_passwords(driver)
    assert len(passwords) == 10
    assert any([re.match(r'[a-z]', password.text) != None for password in passwords])

def test_generate_invalidinput(driver):
    set_password_length(driver, "abc")
    generate(driver)
    assert get_message(driver) == "ошибка: введите число от 1 до 100"

def test_generate_greaterthanhundred(driver):
    set_password_length(driver, "111")
    generate(driver)
    assert get_message(driver) == "ошибка: длина пароля ограничена 100 символами"