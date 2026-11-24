# Práctica 2: Selenium WebDriver con Python

Tres ejercicios con localizadores ID, Name y XPath. Cada uno tiene 2 asserts y una captura en `capturas/`.

## Requisitos

- Python 3.10 o superior
- Google Chrome (Selenium Manager descarga el driver)

## Instalación

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```
python ejercicio1_login_saucedemo.py
python ejercicio2_login_invalido.py
python ejercicio3_buscar_producto.py
```

Chrome corre sin ventana. Para verlo, cambiar `VER_NAVEGADOR = True` al inicio del script.
