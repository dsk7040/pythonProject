import time
from selenium.webdriver.common.by import By

class Fangate():

    def __init__(self, driver):
        self.driver = driver

        # self.Download_gate_xpath = "//li[@id='li-gates']//a[contains(text(),'Download Gates')]"
        # self.Create_gate_xpath = "//div[@class='table-row-item ud1']//img[@alt='green-plus-icon']"
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
        self.add_popup_xpath = "//button[contains(text(),'ADD MORE STEPS ANYWAY')]"
        self.select_radio_xpath = "(//div[@class='radio-option-box'])[50]"
        self.add_apple_track_xpath = "//input[@id='add_apple_artist']"
        self.next_box_button_gate_ID = "next_box_button_gate-steps"
        self.next_box_button_gate_ID2 = "next_box_button_gate-steps"
        self.next_box_button_linkurl_ID = "next_box_button_linkurl"
        self.next_box_button_newrelease_ID = "next_box_button_newrelease"
        self.next_box_button_email_ID = "next_box_button_email-promotion"
        self.next_box_button_pixel_ID = "next_box_button_pixel"
        self.next_box_button_confirmation_ID = "next_box_button_confirmation"
        self.Close_Popup_xpath = "//a[@class='button button-morelight']"
        self.dashboard_button_xpath = "//a[contains(text(),'DASHBOARD')]"

    def create_fangate(self, trackurl, uploadmp3, Arjitsingh, Apple_Track):
        self.driver.get("https://dev2.hypeddit.com/gate/create")
        self.driver.implicitly_wait(10)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.trackurl_click_xpath).send_keys(trackurl)
        time.sleep(3)
        self.driver.find_element(By.ID, self.next_button_id).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Select_genre_xpath).click()
        self.driver.find_element(By.XPATH, self.Select_Bass_xpath).click()
        self.driver.find_element(By.ID, self.genre_next_button_id).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.uploadMp3_id).send_keys(uploadmp3)
        time.sleep(3)
        self.driver.find_element(By.ID, self.next_upload_button_id).click()
        self.driver.find_element(By.ID, self.next_box_button_id).click()
        self.driver.find_element(By.XPATH, self.dark_theme_xpath).click()
        self.driver.find_element(By.ID, self.next_button_design_id).click()
        self.driver.find_element(By.ID, self.spotify_profile_add_id).click()
        self.driver.find_element(By.ID, self.add_spotify_artist_id).send_keys(Arjitsingh)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.spotify_artist_xpath).click()
        self.driver.find_element(By.XPATH, self.add_apple_button_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.add_popup_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_radio_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.add_apple_track_xpath).send_keys(Apple_Track)
        time.sleep(2)
        self.driver.find_element(By.ID, self.next_box_button_gate_ID).click()
        time.sleep(3)
        self.driver.find_element(By.ID, self.next_box_button_gate_ID2).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.next_box_button_linkurl_ID).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.next_box_button_newrelease_ID).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.next_box_button_email_ID).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.next_box_button_pixel_ID).click()
        time.sleep(1)
        self.driver.find_element(By.ID, self.next_box_button_confirmation_ID).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.Close_Popup_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.dashboard_button_xpath).click()
        time.sleep(2)

    # def waitForElement(self, locator, locatorType="id", timeout=10, poll_Frequency=0.5):
    #         element = None
    #         try:
    #             byType = self.getByType(locatorType)
    #             # self.log.info("Waiting for maximum :: " + str(timeout) +
    #             #               " :: seconds for element to be clickable")
    #             wait = WebDriverWait(self.driver, timeout, poll_Frequency,
    #                                  ignored_exceptions=[NoSuchElementException,
    #                                                      ElementNotVisibleException,
    #                                                      ElementNotSelectableException,
    #                                                      ElementClickInterceptedException])
    #             element = wait.until(EC.element_to_be_clickable((byType,
    #                                                              locator)))
    #             #
    #         except:
    #             # self.log.info("Element not appeared on the web page")
    #             print_stack()
    #         return element


