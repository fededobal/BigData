from ejercicios.comun import LIBROS, correr

CLAVE = "punto5C"
DESCRIPCION = "Promedio de parrafos por libro"
SALIDA = "punto5C"


def fmap(key, value, context):
    if value.strip():
        context.write(".", 1)


def fred(key, values, context):
    cant_libros = sum(1 for f in LIBROS.iterdir() if f.is_file())
    cant = 0
    for v in values:
        cant += v
    context.write("PROMEDIO de párrafos entre todos los libros: ", cant / cant_libros)


def run():
    return correr(LIBROS, SALIDA, fmap, fred)
