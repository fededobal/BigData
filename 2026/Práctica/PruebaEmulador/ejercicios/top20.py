import bisect

from MRE import Job

CLAVE = "top20"
DESCRIPCION = "Las 20 palabras mas frecuentes (usa la salida de wordcount)"


def fmap(key, value, context):
    context.write(1, (key, int(value)))


def fred(key, values, context):
    lista = []
    for v in values:
        bisect.insort(lista, v, key=lambda x: x[1])
    top = lista[-20:][::-1]
    context.write("TOP 20:", "\n" + "".join(f"{p} {c}\n" for p, c in top))


def run():
    return Job("data/output/wordcount", "data/output/top20", fmap, fred).waitForCompletion()
