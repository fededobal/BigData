from ejercicios import (
    wordcount,
    top20,
    punto4,
    punto5A,
    punto5B,
    punto5C,
    punto5D,
    punto5E,
    punto5F,
    ejemploLogsTeoria,
)

MODULOS = [
    wordcount,
    top20,
    punto4,
    punto5A,
    punto5B,
    punto5C,
    punto5D,
    punto5E,
    punto5F,
    ejemploLogsTeoria,
]

REGISTRO = {m.CLAVE: m for m in MODULOS}


def buscar(nombre):
    n = nombre.strip().lower()
    for clave, modulo in REGISTRO.items():
        if clave.lower() == n or clave.lower() == "punto" + n:
            return modulo
    return None
