import time
import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [("incorrectUser", "Password123", "Your username is invalid!"), ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(3)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error msg is not displayed but it should"

        # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == expected_error_message, "Error msg is not expected"

    def test_negative_username(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("Student")

        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("incorrectPassword")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(3)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error msg is not displayed but it should"

        # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error msg is not expected"

    def test_negative_password(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username = driver.find_element(By.ID, "username")
        username.send_keys("student")

        # Type password incorrectPassword into Password field
        password = driver.find_element(By.ID, "password")
        password.send_keys("incorrectPassword")

        # Push Submit button
        submit_btn = driver.find_element(By.ID, "submit")
        submit_btn.click()

        # Verify error message is displayed
        error_msg = driver.find_element(By.ID, "error")
        assert error_msg.is_displayed(), "Error message is not displayed but it should be"

        # Verify error message text is Your password is invalid!
        error_msg_text = error_msg.text
        assert error_msg_text == "Your password is invalid!", "Error message is not expected"
