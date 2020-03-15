from selenium import webdriver
from time import sleep
import os
import random
import string

def main():
    try:
        driver = webdriver.Chrome()
        driver.get('https://vk.com/')
        username = 'and-bulgaru@mail.ru'
        password = os.environ['VK_PASS']
        username_input = driver.find_element_by_xpath(r'//*[@id="index_email"]')
        username_input.clear()
        username_input.send_keys(username)
        password_input = driver.find_element_by_xpath(r'//*[@id="index_pass"]')
        password_input.clear()
        password_input.send_keys(password)
        remember_checkbox = driver.find_element_by_xpath(r'//*[@id="index_expire"]')
        if not remember_checkbox.is_selected():
            remember_checkbox.click()
        login_button = driver.find_element_by_xpath(r'//*[@id="index_login_button"]')
        login_button.click()
        sleep(5)
        communities_button = driver.find_element_by_xpath(r'//*[@id="l_gr"]/a/span/span[3]')
        communities_button.click()
        sleep(2)
        communities_create_button = driver.find_element_by_xpath(r'//*[@id="wide_column"]/div[1]/h2/ul/a')
        communities_create_button.click()
        sleep(2)
        interest_community_create_button = driver.find_element_by_xpath(r'//*[@id="wk_content"]/div/div/div[3]/div[4]')
        interest_community_create_button.click()
        sleep(2)
        letters = string.ascii_lowercase
        community_name_length = 10
        community_name = ''.join(random.choice(letters) for i in range(community_name_length))
        community_name_input = driver.find_element_by_xpath(r'//*[@id="groups_create_box_title"]') # ввести название группы
        community_name_input.clear()
        community_name_input.send_keys(community_name)
        community_subject_input = driver.find_element_by_xpath(r'//*[@id="container2"]/table/tbody/tr/td[1]/input[1]') # выбрать тематику
        community_subject_input.click()
        auto_subject_community_ref = driver.find_element_by_xpath(r'//*[@id="option_list_options_container_2_2"]') # выбрать тематику авто
        auto_subject_community_ref.click()
        community_create_button = driver.find_element_by_xpath(r'//*[@id="box_layer"]/div[2]/div/div[3]/div[1]/table/tbody/tr/td[2]/button') # создать сообщество
        community_create_button.click()
        sleep(10)
        community_close_info = driver.find_element_by_xpath(r'//*[@id="box_layer"]/div[2]/div/div[2]/div/div[1]') # закрыть информацию о группах
        community_close_info.click()
        sleep(10)
        community_invite_button = driver.find_element_by_xpath(r'//*[@id="page_menu_group_invite"]') # приглашения
        community_invite_button.click()
        sleep(2)
        community_invite_user = driver.find_element_by_xpath(r'//*[@id="page_members_box"]/div[2]/div[2]/a') # пригласить человека
        community_invite_user.click()
        sleep(2)
        community_close_invite_button = driver.find_element_by_xpath(r'//*[@id="box_layer"]/div[2]/div/div[3]/div[1]/table/tbody/tr/td/button') # закрыть приглашения
        community_close_invite_button.click()
        community_participant_dropdown = driver.find_element_by_xpath(r'//*[@id="page_actions_btn"]/span') # вы участник
        community_participant_dropdown.click()
        sleep(2)
        community_exit = driver.find_element_by_xpath(r'//*[@id="page_actions_wrap"]/div[2]/a[1]') # выход из группы
        community_exit.click()
        community_exit_confirmation = driver.find_element_by_xpath(r'//*[@id="box_layer"]/div[2]/div/div[3]/div[1]/table/tbody/tr/td[2]/button') # нажатие на выход
        community_exit_confirmation.click()


        sleep(600)
    finally:
        driver.close()

if __name__ == '__main__':
    main()