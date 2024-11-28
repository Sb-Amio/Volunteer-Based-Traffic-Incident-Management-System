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

@pytest.mark.parametrize("username, em, password1, password2", [
    ("NormalUser","21201201@uap-bd.edu", "abcdabcd", "abcdabcd"),
    ("NormalUser", "wrong", "abcdabcd", "abcdabcd"),
    ("Nrmal User", "21201201@uap-bd.edu", "abcdabcd", "abcdabcd"),
    ("NrmalUser", "21201201@uap-bd.edu", "abcdabc", "abcdabcd"),
    ("NrmalUser", "21201201@uap-bd.edu", "ww", "ww"),
    ("NrmalUser1", "21201201@uap-bd.edu", "abcdabcd", "abcdabcd"),
])
def test_login(driver, username,em, password1, password2):
    driver.get("http://127.0.0.1:8000/signup/Volunteer/")

    # Find form fields and button
    username_field = driver.find_element(By.ID, "id_username")
    email_field = driver.find_element(By.ID, "id_email")
    password_field1 = driver.find_element(By.ID, "id_password1")
    password_field2 = driver.find_element(By.ID, "id_password2")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button")

    username_field.send_keys(username)
    email_field.send_keys(em)
    password_field1.send_keys(password1)
    password_field2.send_keys(password2)
    submit_button.click()

    time.sleep(3)

    #print(driver.page_source)
    # Assert based on actual success criteria
    #assert "Dashboard" in driver.page_source  # Replace with the actual success indicator
