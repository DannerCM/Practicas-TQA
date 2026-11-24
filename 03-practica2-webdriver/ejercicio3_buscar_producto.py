# Ejercicio 3: buscar "shirt" en Automation Exercise (localizadores: ID, Name y XPath)
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


def cerrar_anuncios():
    # Cierra el consentimiento de cookies si aparece
    for boton in driver.find_elements(By.CSS_SELECTOR, "button.fc-cta-consent"):
        if boton.is_displayed():
            boton.click()
    # Los anuncios (vignette) se ocultan al quitar su contenedor
    driver.execute_script(
        "document.querySelectorAll('ins.adsbygoogle, iframe[id^=aswift], "
        "#ad_position_box, .google-auto-placed').forEach(e => e.remove());")


try:
    driver.get("https://automationexercise.com")
    driver.maximize_window()
    cerrar_anuncios()

    # Localizador XPath relativo
    espera.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/products']"))).click()
    if "#google_vignette" in driver.current_url:
        driver.get("https://automationexercise.com/products")
    cerrar_anuncios()

    # Localizadores ID y Name
    espera.until(EC.visibility_of_element_located((By.ID, "search_product")))
    driver.find_element(By.NAME, "search").send_keys("shirt")
    driver.find_element(By.ID, "submit_search").click()
    cerrar_anuncios()

    # Assert 1: aparece el título "Searched Products"
    titulo = espera.until(EC.visibility_of_element_located(
        (By.XPATH, "//h2[contains(@class,'title') and contains(.,'Searched Products')]")))
    assert "Searched Products" in titulo.get_attribute("textContent")  # el CSS lo muestra en mayúsculas

    # Assert 2: al menos un resultado contiene "shirt"
    nombres = driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']/p")
    assert len(nombres) >= 1
    assert any("shirt" in n.text.lower() for n in nombres)

    driver.execute_script("arguments[0].scrollIntoView();", titulo)
    driver.save_screenshot("capturas/ejercicio3.png")
    print("Ejercicio 3: PASS")
finally:
    driver.quit()
