from MRE import Job

CLAVE = "ejemploLogsTeoria"
DESCRIPCION = "Para cada usuario, la página en la que más tiempo permaneció"


def fmapTiempos(key, value, context):
    id_user, id_page, tiempo = value.split(",")
    context.write((id_user, id_page), int(tiempo))


def fredTiempos(key, values, context):
    total = 0
    for v in values:
        total += v
    context.write(key, total)


def fmapMaximo(key, value, context):
    id_page, total = value.split("\t")
    context.write(key, (id_page, int(total)))


def fredMaximo(key, values, context):
    mejor = None
    for (id_page, total) in values:
        if mejor is None or total > mejor[1]:
            mejor = (id_page, total)
    context.write(key, mejor)


def run():
    Job("data/input/logs_paginas", "data/output/ejemploLogsTeoria_tiempos",
        fmapTiempos, fredTiempos).waitForCompletion()
    return Job("data/output/ejemploLogsTeoria_tiempos", "data/output/ejemploLogsTeoria",
               fmapMaximo, fredMaximo).waitForCompletion()
