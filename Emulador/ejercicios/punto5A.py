from MRE import Job

CLAVE = "punto5A"
DESCRIPCION = "Palabras distintas que aparecen en los libros"


def fmap(key, value, context):
    for palabra in value.split():
        context.write(palabra, 1)


def fred(key, values, context):
    context.write(key, "")


def run():
    return Job("data/input/libros", "data/output/punto5A", fmap, fred).waitForCompletion()
