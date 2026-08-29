# PruebaEmulador

Práctica de Big Data sobre el emulador MapReduce de la cátedra (`MRE.py`).

## Cómo correr

```bash
./.venv/bin/python main.py            # todos los puntos, en orden
./.venv/bin/python main.py 5b 5c      # solo algunos (acepta 5b, punto5B, PUNTO5B)
./.venv/bin/python main.py --lista    # qué puntos hay
```

Cada punto deja su resultado en `data/output/<punto>/output.txt`.

## Estructura

```
main.py            CLI: elige qué puntos correr
MRE.py             emulador de la cátedra (no se toca)
ejercicios/
  __init__.py      registro de puntos (MODULOS)
  comun.py         rutas + helper correr() que arma el Job
  wordcount.py     un módulo por punto: fmap, fred y run()
  top20.py
  punto4.py
  punto5A.py ... punto5F.py
data/
  input/           libros/, encuesta/, inversionistas/
  output/          una carpeta por punto
```

## Agregar un punto nuevo

1. Copiar cualquier módulo de `ejercicios/` (por ejemplo `punto5B.py`).
2. Cambiar `CLAVE`, `DESCRIPCION`, `SALIDA` y escribir `fmap` / `fred`.
3. Importarlo en `ejercicios/__init__.py` y agregarlo a `MODULOS`.

El `main.py` no hay que tocarlo: levanta los puntos del registro.
