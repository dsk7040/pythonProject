from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service("C:\\Users\\Baltech\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://www.flipkart.com/")
driver.implicitly_wait(2)
driver.maximize_window()

driver.quit()
driver.close()

print("passes")