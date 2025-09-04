from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

def test_search_python(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Python programming")
    search_box.submit()
    assert "Python" in driver.title or "python" in driver.page_source

def test_search_selenium(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Selenium WebDriver")
    search_box.submit()
    assert "Selenium" in driver.title or "selenium" in driver.page_source
