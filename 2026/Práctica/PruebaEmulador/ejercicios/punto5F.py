from MRE import Job

CLAVE = "punto5F"
DESCRIPCION = "El dialogo mas largo (parrafos con dialogo consecutivos)"


def fmap(key, value, context):
    parrafo = value.strip()
    if parrafo != "":
        context.write(".", (key, parrafo))


def fred(key, values, context):
    parrafos = []
    for v in values:
        parrafos.append(v)
    parrafos.sort()

    mejor = []
    actual = []
    for (offset, p) in parrafos:
        if p.startswith("--"):
            actual.append(p)
            if len(actual) > len(mejor):
                mejor = list(actual)
        else:
            actual = []

    context.write("DIÁLOGO mas largo (" + str(len(mejor)) + " parrafos)",
                  "\n" + "\n".join(mejor) + "\n")


def run():
    return Job("data/input/libros", "data/output/punto5F", fmap, fred).waitForCompletion()
