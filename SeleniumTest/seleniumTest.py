
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time

drive = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
login_text = 'Matheus Alves'


drive.get("https://matheus-allvz.github.io/VectorPro/index.html")
time.sleep(2)

field = drive.find_element(by=id, value='session_key')
field.send_keys(login_text)
time.sleep(1)



drive.close()
drive.quit()

print("Test sucesfuly executed!")