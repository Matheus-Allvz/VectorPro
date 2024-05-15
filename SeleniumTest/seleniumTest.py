
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

drive = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

drive.get("https://matheus-allvz.github.io/VectorPro/")

time.sleep(2)

button = drive.find_element(By.CLASS_NAME, "sign-in")
button.click()

time.sleep(2)

button = drive.find_element(By.CSS_SELECTOR, "a")
button.click()

time.sleep(2)
drive.close()
drive.quit()

print("Test executed!")