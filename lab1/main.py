from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os

def download_image(url, path):
    try:
        r = requests.get(url)
        with open(os.path.join(path, url.replace('/', '.')), 'wb') as f:
            f.write(r.content)
    except Exception as e:
        print(f"error while saving image with exception: {e}\nurl: {url}")

def main():
    driver = webdriver.Chrome()
    try:
        driver.get('https://mirea.ru')
        image_elements = driver.find_elements_by_tag_name('img')
        directory = os.path.join(os.path.dirname(__file__), 'images')
        if not os.path.exists(directory):
            os.makedirs(directory)
        for image_element in image_elements:
            url = image_element.get_attribute('src')
            download_image(url, directory)
    finally:
        driver.close()

if __name__ == '__main__':
    main()

