from ejercicios.comun import LIBROS, correr

CLAVE = "punto5E"
DESCRIPCION = "Cantidad de parrafos con dialogo"
SALIDA = "punto5E"


def fmap(key, value, context):
    if value[:2] == "--":
        context.write(".", 1)


def fred(key, values, context):
    cant = 0
    for v in values:
        cant += v
    context.write("CANTIDAD de párrafos con diálogos: ", cant)


def run():
    return correr(LIBROS, SALIDA, fmap, fred)
