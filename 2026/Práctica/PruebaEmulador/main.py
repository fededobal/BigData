import bisect

from MRE import Job
from os.path import dirname, abspath

root_path = dirname(abspath(__file__)) + "/"

def wordCount():
    inputDir = root_path + "WordCount/input/"
    outputDir = root_path + "WordCount/output/"

    def fmap(key, value, context):
        words = value.split()
        for w in words:
            context.write(w, 1)

    def fred(key, values, context):
        c = 0
        for v in values:
            c = c + 1
        context.write(key, c)

    job = Job(inputDir, outputDir, fmap, fred)
    success = job.waitForCompletion()
    print(success)

def top20():
    inputDir = root_path + "WordCount/output/"
    outputDir = root_path + "WordCount/outputTop20/"

    def fmap(key, value, context):
        context.write(1, (key, int(value)))

    def fred(key, values, context):
        lista = []
        for v in values:
            bisect.insort(lista, v, key=lambda x: x[1])
        top = lista[-20:][::-1]
        context.write("TOP 20:", "\n" + "".join(f"{p} {c}\n" for p, c in top))

    job = Job(inputDir, outputDir, fmap, fred)
    success = job.waitForCompletion()
    print(success)

def punto4():
    inputDir = root_path + "WordCount/input/"
    outputDir = root_path + "WordCount/outputPunto4/"
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

    job = Job(inputDir, outputDir, fmap, fred)
    success = job.waitForCompletion()
    print(success)

if __name__ == '__main__':
    wordCount()
    top20()
    punto4()