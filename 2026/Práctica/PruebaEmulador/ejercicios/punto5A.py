from ejercicios.comun import LIBROS, correr

CLAVE = "punto5A"
DESCRIPCION = "Palabras distintas que aparecen en los libros"
SALIDA = "punto5A"


def fmap(key, value, context):
    for palabra in value.split():
        context.write(palabra, 1)


def fred(key, values, context):
    context.write(key, "")


def run():
    return correr(LIBROS, SALIDA, fmap, fred)
