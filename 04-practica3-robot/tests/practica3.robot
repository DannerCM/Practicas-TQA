*** Settings ***
Documentation     Practica 3: tres ejercicios con Robot Framework y SeleniumLibrary.
Resource          ../keywords/keywords.robot
Test Teardown     Close All Browsers

*** Test Cases ***
Ejercicio 1 Login Correcto En SauceDemo
    Abrir Navegador En    ${URL_SAUCEDEMO}
    Iniciar Sesion En SauceDemo    ${USUARIO_SAUCE}    ${CLAVE_SAUCE}
    Location Should Be    ${URL_INVENTARIO}
    Element Text Should Be    class=title    Products
    Capturar Pantalla    ejercicio1-login-correcto

Ejercicio 2 Login Incorrecto En The Internet
    Abrir Navegador En    ${URL_HEROKU_LOGIN}
    Iniciar Sesion En Heroku    ${USUARIO_INVALIDO}    ${CLAVE_INVALIDA}
    Element Should Contain    id=flash    Your username is invalid!
    Location Should Contain    /login
    Capturar Pantalla    ejercicio2-login-incorrecto

Ejercicio 3 Busqueda De Productos En AutomationExercise
    Abrir Navegador En    ${URL_AUTOMATION}
    Buscar Producto En AutomationExercise    ${TERMINO_BUSQUEDA}
    Page Should Contain    ${TITULO_BUSQUEDA}
    Page Should Contain Element    xpath=//div[@class='productinfo text-center']/p
    Capturar Pantalla    ejercicio3-busqueda
