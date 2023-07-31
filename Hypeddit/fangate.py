import time
from selenium.webdriver.common.by import By
class Fangate():

    def __init__(self, driver):
        self.driver = driver

        self.Download_gate_xpath = "//li[@id='li-gates']//a[contains(text(),'Download Gates')]"
        self.Create_gate_xpath = "//div[@class='table-row-item ud1']//img[@alt='green-plus-icon']"
        self.trackurl_click_xpath = "//input[@type='text'][@id='track_url']"
        self.next_button_id = "next_box_button_source"
        self.Select_genre_xpath = "//button[@title='Select genre']"
        self.Select_Bass_xpath = "//li[@data-original-index='2']//span[contains(text(),'Bass')]"
        self.genre_next_button_id = "next_box_button_genre"


    def Fangate(self, trackurl):
        # self.driver.get("https://dev2.hypeddit.com/gate/create")
        # self.driver.implicitly_wait(2)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Download_gate_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Create_gate_xpath).click()
        self.driver.find_element(By.XPATH, self.trackurl_click_xpath).send_keys(trackurl)
        time.sleep(1)
        self.driver.find_element(By.ID, self.next_button_id).click()
        self.driver.find_element(By.XPATH, self.Select_genre_xpath).click()
        self.driver.find_element(By.XPATH, self.Select_Bass_xpath).click()
        self.driver.find_element(By.ID, self.genre_next_button_id).click()
        time.sleep(2)


time.sleep(2)

print("Task Done")

