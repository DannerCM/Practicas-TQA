# Práctica 3: Robot Framework

## Objetivo

Automatizar tres pruebas web (SauceDemo, The Internet y búsqueda de productos en Automation Exercise) con Robot Framework y SeleniumLibrary. Cada caso usa variables, keywords propias, dos validaciones y una captura de pantalla.

## Requisitos

- Python 3.10 o superior
- Google Chrome

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```bash
robot --outputdir reports tests/
```

Genera `report.html`, `log.html` y `output.xml` en `reports/`. Las capturas quedan en `screenshots/`.

## Estructura

```
tests/practica3.robot          tres casos de prueba
keywords/keywords.robot        keywords propias
variables/variables.robot      URLs, usuarios y navegador
screenshots/                   una captura por caso
reports/                       report.html, log.html, output.xml
requirements.txt               versiones fijadas
```
