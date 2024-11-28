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

@pytest.mark.parametrize("title, description, location, service", [
    ("Test Title","Test Description", "Test, Location", "Fire"),
    ("Test Title","Test Description", "Test, Location", "Police"),

])
def test_login(driver, title, description, location, service):
    driver.get("http://127.0.0.1:8000/add_incident/")

    # Find form fields and button
    title_field = driver.find_element(By.ID, "id_title")
    description_field = driver.find_element(By.ID, "id_description")
    location_field = driver.find_element(By.ID, "id_location")
    service_field = driver.find_element(By.ID, "id_service_type")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button")

    title_field.send_keys(title)
    description_field.send_keys(description)
    location_field.send_keys(location)
    service_field.send_keys(service)
    submit_button.click()

    time.sleep(3)

    #print(driver.page_source)
    # Assert based on actual success criteria
    #assert "Dashboard" in driver.page_source  # Replace with the actual success indicator
