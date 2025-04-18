import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--allow-file-access-from-files")
    chrome_options.add_argument("--disable-web-security")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_homepage(setup):
    driver = setup
    try:
        driver.get("file:///C:/Users/yendr/OneDrive/Desktop/tarea4/index.html")
        assert "Tienda de Computadoras" in driver.title, "El título de la página no coincide"
    except Exception as e:
        driver.save_screenshot("error_homepage.png")
        raise e
    driver.save_screenshot("homepage.png")

def test_login(setup):
    driver = setup
    try:
        driver.get("file:///C:/Users/yendr/OneDrive/Desktop/tarea4/index.html")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "loginButton").click()


        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            print("No hay alerta presente")

        time.sleep(1)
        driver.save_screenshot("login_success.png")
    except Exception as e:
        driver.save_screenshot("error_login.png")
        raise e

def test_logout(setup):
    driver = setup
    try:
        driver.get("file:///C:/Users/yendr/OneDrive/Desktop/tarea4/index.html")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "loginButton").click()

   
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            print("No hay alerta presente")

        logout_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "logoutButton")))
        logout_button.click()

    
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            print("No hay alerta presente")

        time.sleep(1)
        driver.save_screenshot("logout_success.png")
    except Exception as e:
        driver.save_screenshot("error_logout.png")
        raise e

def test_products_visible_after_login(setup):
    driver = setup
    try:
        driver.get("file:///C:/Users/yendr/OneDrive/Desktop/tarea4/index.html")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "loginButton").click()

     
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            print("No hay alerta presente")

        products = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "products")))
        assert products.is_displayed(), "Los productos no son visibles después de iniciar sesión"
        driver.save_screenshot("products_visible.png")
    except Exception as e:
        driver.save_screenshot("error_products.png")
        raise e