import bisect

from ejercicios.comun import OUTPUT, correr
from ejercicios import wordcount

CLAVE = "top20"
DESCRIPCION = "Las 20 palabras mas frecuentes (usa la salida de wordcount)"
SALIDA = "top20"


def fmap(key, value, context):
    context.write(1, (key, int(value)))


def fred(key, values, context):
    lista = []
    for v in values:
        bisect.insort(lista, v, key=lambda x: x[1])
    top = lista[-20:][::-1]
    context.write("TOP 20:", "\n" + "".join(f"{p} {c}\n" for p, c in top))


def run():
    return correr(OUTPUT / wordcount.SALIDA, SALIDA, fmap, fred)
