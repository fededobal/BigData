from MRE import Job

CLAVE = "punto4"
DESCRIPCION = "Cantidad de vocales, consonantes, numeros, espacios y otros"

VOCALES = "aeiouáéíóúAEIOUÁÉÍÓÚ"


def fmap(key, value, context):
    for caracter in value:
        if caracter in VOCALES:
            context.write("VOCALES", 1)
        elif caracter.isalpha() and caracter.lower() != caracter.upper():
            context.write("CONSONANTES", 1)
        elif caracter.isdigit():
            context.write("NUMEROS", 1)
        elif caracter.isspace():
            context.write("ESPACIOS", 1)
        else:
            context.write("OTROS", 1)


def fred(key, values, context):
    cont = 0
    for v in values:
        cont = cont + v
    context.write(key, cont)


def run():
    return Job("data/input/libros", "data/output/punto4", fmap, fred).waitForCompletion()
