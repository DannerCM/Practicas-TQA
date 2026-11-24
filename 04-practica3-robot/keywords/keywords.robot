*** Settings ***
Library    SeleniumLibrary
Resource   ../variables/variables.robot

*** Keywords ***
Abrir Navegador En
    [Arguments]    ${url}
    Open Browser    ${url}    ${NAVEGADOR}    options=add_argument("--window-size=1280,900")
    Set Selenium Timeout    10s
    Set Selenium Implicit Wait    5s

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

Cerrar Anuncios
    Execute Javascript    document.querySelectorAll('button.fc-cta-consent').forEach(b => b.click());
    Execute Javascript    document.querySelectorAll('ins.adsbygoogle, iframe[id^=aswift], #ad_position_box, .google-auto-placed').forEach(e => e.remove());

Buscar Producto En AutomationExercise
    [Arguments]    ${termino}
    Cerrar Anuncios
    Wait Until Element Is Visible    id=search_product
    Input Text    id=search_product    ${termino}
    Click Button    id=submit_search
    Cerrar Anuncios

Capturar Pantalla
    [Arguments]    ${nombre}
    Capture Page Screenshot    ${CARPETA_CAPTURAS}${/}${nombre}.png
