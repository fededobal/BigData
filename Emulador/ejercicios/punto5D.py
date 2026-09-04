from MRE import Job

CLAVE = "punto5D"
DESCRIPCION = "Cantidad de caracteres del parrafo mas largo"


def fmap(key, value, context):
    context.write(".", len(value.strip()))


def fred(key, values, context):
    maximo = 0
    for v in values:
        if v > maximo:
            maximo = v
    context.write("CANTIDAD de caracteres del párrafo más largo: ", maximo)


def run():
    return Job("data/input/libros", "data/output/punto5D", fmap, fred).waitForCompletion()
