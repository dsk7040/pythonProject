import time
from selenium.webdriver.common.by import By

class Smartlink():

    def __init__(self, driver):
        self.driver = driver

        self.trackurl_click_xpath = "//input[@type='text'][@id='track_url']"
        self.next_button_id = "next_box_button_source"
        self.Select_genre_xpath = "//button[@title='Select genre']"
        self.Select_chill_xpath = "//li[@data-original-index='5']//span[contains(text(),'Chill Out')]"
        self.genre_next_button_id = "next_box_button_genre"
        self.next_box_button_id = "next_box_button_title"
        self.dark_theme_xpath = "//div[@class='checkbox']//label[@for='dark_theme']"
        self.next_button_design_id = "next_box_button_design"
        self.next_box_button_links_ID = "next_box_button_links"
        self.next_box_button_linkurl_ID = "next_box_button_linkurl"
        self.next_box_button_newrelease_ID = "next_box_button_newrelease"
        self.next_box_button_audio_ID = "next_box_button_audio-preview"
        self.next_box_button_pixel_ID = "next_box_button_pixel"
        self.next_box_button_confirmation_ID = "next_box_button_confirmation"
        #self.Close_Popup_xpath = "//a[@class='button button-morelight']"
        self.dashboard_button_xpath = "//a[contains(text(),'DASHBOARD')]"

    def create_smartlink(self, trackurl):
        self.driver.get("https://dev2.hypeddit.com/smartlink/create")
        self.driver.implicitly_wait(10)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.trackurl_click_xpath).send_keys(trackurl)
        time.sleep(3)
        self.driver.find_element(By.ID, self.next_button_id).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Select_genre_xpath).click()
        self.driver.find_element(By.XPATH, self.Select_chill_xpath).click()
        self.driver.find_element(By.ID, self.genre_next_button_id).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.next_box_button_id).click()
        self.driver.find_element(By.XPATH, self.dark_theme_xpath).click()
        self.driver.find_element(By.ID, self.next_button_design_id).click()
        self.driver.find_element(By.ID, self.next_box_button_links_ID).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.next_box_button_linkurl_ID).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.next_box_button_newrelease_ID).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.next_box_button_audio_ID).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.next_box_button_pixel_ID).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.next_box_button_confirmation_ID).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.dashboard_button_xpath).click()
        time.sleep(2)
