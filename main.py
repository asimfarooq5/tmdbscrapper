import os
import urllib.request
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options as ChromeOptions


def generate_random_number():
    n = randint(5, 20)
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


# Driver for Chrome
def create_chrome_driver():
    options = ChromeOptions()
    options.add_argument("--headless")
    #options.add_argument("--no-sandbox")
    #options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    #options.add_argument("--disable-dev-shm-usage")
    #options.add_argument("--disable-application-cache")
    options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(options=options)
    return driver


def open_movie_db_site(driver):
    driver.get("https://www.themoviedb.org/movie")


def get_images(driver):
    os.makedirs("posture", exist_ok=True)
    # identify image to be captured
    for i in range(1, 21):
        l = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, f"/html/body/div[1]/main/section/div/div/div/div[2]/div[2]/div/section/div/div/div[{i}]/div[1]/div[1]/a/img"))
        )
        src = l.get_attribute('src')

        # download the image

        urllib.request.urlretrieve(src, f'posture/posture{i}.png')

        # with open(f'posture/posture{i}.png', 'wb') as file:
        #     # write file
        #     file.write(l.screenshot_as_png)




if __name__ == '__main__':
    driver = create_chrome_driver()
    driver.delete_all_cookies()
    open_movie_db_site(driver)
    get_images(driver)
    sleep(3)
    driver.quit()
