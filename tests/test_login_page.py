import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        time.sleep(2)

        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(1)

        # here we create a variable to locate the username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # here we create a variable to locate the password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # here we push the Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_url = text_locator.text

        # Verify button log out is displayed on the new page
        log_out_btn_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert log_out_btn_locator.is_displayed()
