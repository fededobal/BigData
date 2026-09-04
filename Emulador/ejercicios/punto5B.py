from MRE import Job

CLAVE = "punto5B"
DESCRIPCION = "Promedio de palabras por parrafo"


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
    return Job("data/input/libros", "data/output/punto5B", fmap, fred).waitForCompletion()
