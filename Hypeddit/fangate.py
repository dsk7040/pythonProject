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
        self.uploadMp3_id = "inputFilemp3"
        self.next_upload_button_id = "next_box_button_upload"
        self.next_box_button_id = "next_box_button_title"
        self.dark_theme_xpath = "//div[@class='checkbox']//label[@for='dark_theme']"
        self.next_button_design_id = "next_box_button_design"
        self.spotify_profile_add_id = "spotify_profile_add_button"
        self.add_spotify_artist_id = "add_spotify_artist"
        self.spotify_artist_xpath = "//ul[@id='spotify_artist_search']//li[@data-userid='4YRxDV8wJFPHPTeXepOstw']"
        self.add_apple_button_xpath = "//div[@id='add_apple_button']"
        self.add_step_popup_xpath = "//div[@id='step_exceed_warning']//div[@class='modal-content']"

    def create_fangate(self, trackurl, uploadmp3, Arjitsingh):
        # self.driver.get("https://dev2.hypeddit.com/gate/create")
        # self.driver.implicitly_wait(2)
        #time.sleep(1)
        self.driver.find_element(By.XPATH, self.Download_gate_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Create_gate_xpath).click()
        self.driver.find_element(By.XPATH, self.trackurl_click_xpath).send_keys(trackurl)
        time.sleep(2)
        #self.driver.find_element(By.XPATH, self.trackurl_click_xpath).clear()
        self.driver.find_element(By.ID, self.next_button_id).click()
        self.driver.find_element(By.XPATH, self.Select_genre_xpath).click()
        self.driver.find_element(By.XPATH, self.Select_Bass_xpath).click()
        self.driver.find_element(By.ID, self.genre_next_button_id).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.uploadMp3_id).send_keys(uploadmp3)
        time.sleep(3)
        self.driver.find_element(By.ID, self.next_upload_button_id).click()
        self.driver.find_element(By.ID, self.next_box_button_id).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.dark_theme_xpath).click()
        self.driver.find_element(By.ID, self.next_button_design_id).click()
        self.driver.find_element(By.ID, self.spotify_profile_add_id).click()
        self.driver.find_element(By.ID, self.add_spotify_artist_id).send_keys(Arjitsingh)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.spotify_artist_xpath).click()
        self.driver.find_element(By.XPATH, self.add_apple_button_xpath).click()
        self.driver.find_element(By.XPATH, self.spotify_artist_xpath).click()
        self.driver.find_element(By.XPATH, self.add_apple_button_xpath).click()

        time.sleep(4)



print("Task Done")

