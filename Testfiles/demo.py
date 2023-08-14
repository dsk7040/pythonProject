from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(executable_path="C:/Users/Baltech/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver.get("https://www.freeconvert.com/mp3-to-mp4")
driver.implicitly_wait(1)
driver.maximize_window()

#driver.find_element(By.XPATH, "//input[@data-automation-id='DeviceUploaderInput']").send_keys("C:\\Users\\Baltech\\Downloads\\test 5.png")



driver.close()
driver.quit()
print("Done")