from pathlib import Path

from MRE import Job

RAIZ = Path(__file__).resolve().parent.parent
LIBROS = RAIZ / "data" / "input" / "libros"
OUTPUT = RAIZ / "data" / "output"


def correr(entrada, nombre, fmap, fred):
    salida = OUTPUT / nombre
    salida.mkdir(parents=True, exist_ok=True)
    return Job(str(entrada), str(salida), fmap, fred).waitForCompletion()
