from ejercicios.comun import LIBROS, correr

CLAVE = "wordcount"
DESCRIPCION = "Cantidad de apariciones de cada palabra"
SALIDA = "wordcount"


def fmap(key, value, context):
    for palabra in value.split():
        context.write(palabra, 1)


def fred(key, values, context):
    c = 0
    for v in values:
        c = c + 1
    context.write(key, c)


def run():
    return correr(LIBROS, SALIDA, fmap, fred)
