from MRE import Job

CLAVE = "punto5E"
DESCRIPCION = "Cantidad de parrafos con dialogo"


def fmap(key, value, context):
    if value[:2] == "--":
        context.write(".", 1)


def fred(key, values, context):
    cant = 0
    for v in values:
        cant += v
    context.write("CANTIDAD de párrafos con diálogos: ", cant)


def run():
    return Job("data/input/libros", "data/output/punto5E", fmap, fred).waitForCompletion()
