from ejercicios.comun import LIBROS, correr

CLAVE = "punto5B"
DESCRIPCION = "Promedio de palabras por parrafo"
SALIDA = "punto5B"


def fmap(key, value, context):
    context.write(".", len(value.split()))


def fred(key, values, context):
    cant = 0
    total = 0
    for v in values:
        total += v
        cant += 1
    context.write("PROMEDIO de palabras por párrafo: ", total / cant)


def run():
    return correr(LIBROS, SALIDA, fmap, fred)
