# Práctica 3: Robot Framework

## Objetivo

Automatizar tres pruebas web con Robot Framework y SeleniumLibrary. Cada caso usa variables, keywords propias, dos validaciones y una captura de pantalla.

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
robot --outputdir resultados tests/
```

Genera `report.html`, `log.html` y `output.xml` en `resultados/`. Las capturas quedan en `capturas/`.

## Estructura

```
tests/practica3.robot        tres casos de prueba
resources/keywords.robot     keywords propias
resources/variables.robot    URLs, usuarios y navegador
capturas/                    una captura por caso
resultados/                  report.html, log.html, output.xml
requirements.txt             versiones fijadas
```
