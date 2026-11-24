# Ejercicio 1: login en SauceDemo (localizadores: ID)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

VER_NAVEGADOR = False  # True para ver Chrome en pantalla

opciones = webdriver.ChromeOptions()
if not VER_NAVEGADOR:
    opciones.add_argument("--headless=new")
    opciones.add_argument("--window-size=1366,768")
driver = webdriver.Chrome(options=opciones)
espera = WebDriverWait(driver, 10)

try:
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()

    # Localizadores ID
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Assert 1: URL de inventario
    espera.until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url

    # Assert 2: título de la página
    titulo = espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert titulo.text == "Products"

    driver.save_screenshot("capturas/ejercicio1.png")
    print("Ejercicio 1: PASS")
finally:
    driver.quit()
