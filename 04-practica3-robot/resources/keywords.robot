*** Settings ***
Library    SeleniumLibrary
Resource   variables.robot

*** Keywords ***
Abrir Navegador En
    [Arguments]    ${url}
    Open Browser    ${url}    ${NAVEGADOR}    options=add_argument("--window-size=1280,900")
    Set Selenium Timeout    10s

Iniciar Sesion En SauceDemo
    [Arguments]    ${usuario}    ${clave}
    Input Text    id=user-name    ${usuario}
    Input Text    id=password    ${clave}
    Click Button    id=login-button

Iniciar Sesion En Heroku
    [Arguments]    ${usuario}    ${clave}
    Input Text    id=username    ${usuario}
    Input Text    id=password    ${clave}
    Click Button    xpath=//button[@type="submit"]

Agregar Producto Al Carrito
    Click Button    id=add-to-cart-sauce-labs-backpack

Abrir Carrito
    Click Element    class=shopping_cart_link

Capturar Pantalla
    [Arguments]    ${nombre}
    Capture Page Screenshot    ${CARPETA_CAPTURAS}${/}${nombre}.png
