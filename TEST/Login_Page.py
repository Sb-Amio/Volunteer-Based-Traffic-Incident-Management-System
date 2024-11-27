import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("NormalUser", "abcdabcd"),
    ("NormalUser", "wrong"),
    ("wrong", "abcdabcd"),
    ("wrong", "wrong"),
    ("VolunteerUser", "abcdabcd"),
])
def test_login(driver, username, password):
    driver.get("http://127.0.0.1:8000/login/")

    # Find form fields and button
    username_field = driver.find_element(By.ID, "id_username")
    password_field = driver.find_element(By.ID, "id_password")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button")

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()

    time.sleep(1)

    #print(driver.page_source)
    # Assert based on actual success criteria
    #assert "Dashboard" in driver.page_source  # Replace with the actual success indicator
