# driver.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import subprocess
import os

def set_driver():
    try:
        import chromedriver_autoinstaller
    except ImportError:
        subprocess.check_call(["pip3", "install", "chromedriver-autoinstaller"])
        import chromedriver_autoinstaller

    chromedriver_autoinstaller.install(True)
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    driver_path = chromedriver_autoinstaller.get_chrome_version().split(".")[0] + "/chromedriver.exe"
    driver_path = os.path.realpath(driver_path)

    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    # options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(driver_path, options=options)

    return driver
