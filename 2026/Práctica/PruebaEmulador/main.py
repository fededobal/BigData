import sys

from ejercicios import MODULOS, buscar


def listar():
    print("Puntos disponibles:\n")
    for m in MODULOS:
        print(f"  {m.CLAVE:<10} {m.DESCRIPCION}")


def ejecutar(modulo):
    print(f"\n=== {modulo.CLAVE}: {modulo.DESCRIPCION} ===")
    ok = modulo.run()
    print(f"resultado en data/output/{modulo.SALIDA}/output.txt  ->  {ok}")
    return ok


def main(args):
    if "--lista" in args or "-l" in args:
        listar()
        return 0

    if not args:
        elegidos = MODULOS
    else:
        elegidos = []
        for nombre in args:
            modulo = buscar(nombre)
            if modulo is None:
                print(f"No existe el punto '{nombre}'.\n")
                listar()
                return 1
            elegidos.append(modulo)

    for modulo in elegidos:
        ejecutar(modulo)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
