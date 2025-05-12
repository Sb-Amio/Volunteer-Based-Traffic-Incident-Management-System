import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
@pytest.mark.parametrize("title, description, location, service, image", [
    ("Test Title", "Test Description", "Test, Location", "Fire", r"D:\Github\Volunteer Based Traffic & Incident Management System\static\images\Less.jpg"),
    ("Test Title", "Test Description", "Test, Location", "Police", r"D:\Github\Volunteer Based Traffic & Incident Management System\static\images\Large.png"),
])
def test_login(driver, title, description, location, service, image):
    driver.get("http://127.0.0.1:8000/add_incident/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_title")))
    image = os.path.abspath(image)
    title_field = driver.find_element(By.ID, "id_title")
    description_field = driver.find_element(By.ID, "id_description")
    location_field = driver.find_element(By.ID, "id_location")
    service_dropdown = Select(driver.find_element(By.ID, "id_service_type"))
    image_field = driver.find_element(By.ID, "id_image")
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    title_field.send_keys(title)
    description_field.send_keys(description)
    location_field.send_keys(location)
    service_dropdown.select_by_visible_text(service)
    image_field.send_keys(image)
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(submit_button).click().perform()
    time.sleep(3)
