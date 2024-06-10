import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class videocreate():

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://dev2.hypeddit.com/bonustools")

        self.musicvideo_maker_xpath = "//div[@class='tool-selection-table-responsive']//div[1]//div[1]//div[2]//a[1]"
        self.choosefile_id  = "inputFilemp3"
        self.next_button_id = "next_box1_button"
        self.radio_button_xpath = "//b[normalize-space()='Portrait HD']"
        self.next_button_id2 = "next_box1_1_button"
        self.cover_art_id = "inputManualCoverart"
        self.video_effect_id = "show_video_effect"
        self.select_effect_xpath = "//div[normalize-space()='Chromatic Distortion (Audio Reactive)']"
        self.save_effect_id = "save_video_effect"
        self.next_box2_button = "next_box2_button"
        self.switch_icon_xpath = "//div[@class='switch']"
        self.select_social_icon_xpath = "//div[@class='panel focusIn']//div[4]//div[1]//div[1]//div[1]//div[1]//button[1]"
        self.select_spotify_xpath = "(//span[@class='text'][normalize-space()='Spotify'])[1]"
        self.select_social_icon2_xpath = "//div[@class='panel focusIn']//div[5]//div[1]//div[1]//div[1]//div[1]//button[1]"
        self.select_apple_xpath = "(//span[@class='text'][normalize-space()='Apple Music'])[2]"
        self.select_social_icon3_xpath = "//div[@class='panel focusIn']//div[6]//div[1]//div[1]//div[1]//div[1]//button[1]"
        self.select_soundcloud_xpath = "(//span[@class='text'][normalize-space()='SoundCloud'])[3]"
        self.next_box4_button = "next_box4_button"
        self.next_box3_button = "next_box3_button"
        self.btn_create_fangate = "btn_create_fangate"
        self.mail_xpath = "//input[@id='email_address']"
        self.newmail_xpath = "//input[@id='email_address']"

    def musictovideo(self, invalidfile, filepath, invalidimage, coverimage, mailid):
        self.driver.find_element(By.XPATH, self.musicvideo_maker_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.choosefile_id).send_keys(invalidfile)
        time.sleep(1)
        self.driver.find_element(By.ID, self.choosefile_id).send_keys(filepath)
        time.sleep(2)
        self.driver.find_element(By.ID, self.next_button_id).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.radio_button_xpath).click()
        self.driver.find_element(By.ID, self.next_button_id2).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.cover_art_id).send_keys(invalidimage)
        time.sleep(2)
        self.driver.find_element(By.ID, self.cover_art_id).send_keys(coverimage)
        time.sleep(8)
        self.driver.find_element(By.ID, self.video_effect_id).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_effect_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.save_effect_id).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.next_box2_button).click()
        try:
            self.driver.find_element(By.XPATH, "//div[@class='switch']").click()
        except NoSuchElementException:
            self.driver.find_element(By.XPATH, "//label[@for='show_icons']").click()

        self.driver.find_element(By.XPATH, self.select_social_icon_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_spotify_xpath).click()
        self.driver.find_element(By.XPATH, self.select_social_icon2_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_apple_xpath).click()
        self.driver.find_element(By.XPATH, self.select_social_icon3_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_soundcloud_xpath).click()
        self.driver.find_element(By.ID, self.next_box4_button).click()
        self.driver.find_element(By.XPATH, self.mail_xpath).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.newmail_xpath).send_keys(mailid)
        self.driver.find_element(By.ID, self.next_box3_button).click()
        self.driver.find_element(By.ID, self.btn_create_fangate).click()
        time.sleep(8)
        print("pass")
        self.driver.close()
        self.driver.quit()
