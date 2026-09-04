import os

from MRE import Job

CLAVE = "punto5C"
DESCRIPCION = "Promedio de parrafos por libro"


def fmap(key, value, context):
    if value.strip():
        context.write(".", 1)


def fred(key, values, context):
    cant_libros = len(os.listdir("data/input/libros"))
    cant = 0
    for v in values:
        cant += v
    context.write("PROMEDIO de párrafos entre todos los libros: ", cant / cant_libros)


def run():
    return Job("data/input/libros", "data/output/punto5C", fmap, fred).waitForCompletion()
