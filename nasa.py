# nasa.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from driver import set_driver
from download import download_image
import time

def image_of_the_day():
    driver = set_driver()
    driver.get("https://www.nasa.gov/multimedia/imagegallery/iotd.html")
    driver.implicitly_wait(10)
    time.sleep(5)

    driver.find_elements(By.CLASS_NAME, "image")[0].click()
    driver.implicitly_wait(10)

    image_url = driver.find_element(By.CLASS_NAME, "img-responsive").get_attribute("src")
    title = driver.find_element(By.ID, "title").text
    description = driver.find_element(By.TAG_NAME, "p").text

    print(image_url)
    print(title)
    print(description)

    download_image(image_url, r"save\image_of_the_day.jpg")
