# Ejercicio 2: login con credenciales incorrectas (localizadores: Name y XPath con contains())
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
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    # Localizadores Name
    driver.find_element(By.NAME, "username").send_keys("usuario_falso")
    driver.find_element(By.NAME, "password").send_keys("clave_falsa")
    # Localizador XPath relativo con contains()
    driver.find_element(By.XPATH, "//button[contains(@class,'radius')]").click()

    # XPath con contains() para el mensaje de error
    mensaje = espera.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@id,'flash')]")))

    # Assert 1: el mensaje indica credenciales inválidas
    assert "invalid" in mensaje.text.lower()

    # Assert 2: la URL sigue en /login
    assert "/login" in driver.current_url

    driver.save_screenshot("capturas/ejercicio2.png")
    print("Ejercicio 2: PASS")
finally:
    driver.quit()
