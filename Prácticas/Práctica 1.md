# Conceptos y aplicaciones en Big Data

## Práctica 1 – Paradigma MapReduce

---

### 1) Dado el siguiente dataset:

|Split 1||Split 2||Split 3||Split 4||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**Key**|**Value**|**Key**|**Value**|**Key**|**Value**|**Key**|**Value**|
|34|21|23|45|3|21|30|91|
|21|34|12|12|15|10|31|32|
|10|18|36|18|14|18|32|53|
|32|45|4|97|3|15|19|35|

Responda para cada job: ¿Cuántas veces (invocaciones) se ejecuta la función map? ¿Cuántas veces (invocaciones) se ejecuta la función reduce? ¿Cuántos _mappers_ se ejecutan? ¿Cuántos _reducers_ se ejecutan? ¿Qué datos recibe cada función reduce? ¿Cuál es la salida de cada job?

#### a) Job A

```python
def map(k1, v1, context):
    context.write(1, v1)

def reduce(k2, v2, context):
    n = 0
    for v in v2:
        n = n + 1
    context.write(k2, n)
```

>La función *map* se ejecuta 16 veces (cada fila de cada split).
>
>La función *reduce* se ejecuta una sola vez ya que se generó un solo grupo (clave 1).
>
>Se ejecuta un *mapper*  por cada split, osea 4 *mappers*.
>
>***preguntar lo de los reducers***
>
>Recibe la clave k2 '1' y la lista de 16 elementos v2 (21, 34, 18, 45, 45, 12, 18, 97, 21, 10, 18, 15, 91, 32, 53, 35).
>
>El job escribe (1,16).

#### b) Job B

```python
def map(k1, v1, context):
    context.write(1, v1)

def reduce(k2, v2, context):
    n = 0
    for v in v2:
        n = n + v
    context.write(k2, n)
```

>La función *map* se ejecuta 16 veces (cada fila de cada split).
>
>La función *reduce* se ejecuta una sola vez ya que se generó un solo grupo (clave 1).
>
>Se ejecuta un *mapper*  por cada split, osea 4 *mappers*.
>
>***preguntar lo de los reducers***
>
>Recibe la clave k2 '1' y la lista de 16 elementos v2 (21, 34, 18, 45, 45, 12, 18, 97, 21, 10, 18, 15, 91, 32, 53, 35).
>
>El job escribe (1,565).

#### c) Job C

```python
def map(k1, v1, context):
    if (v1 < 30):
        context.write(1, k1)
    else:
        context.write(2, k1)

def reduce(k2, v2, context):
    max = -1
    for v in v2:
        if(v > max):
            max = v
    context.write(k2, max)
```

>La función *map* se ejecuta 16 veces (cada fila de cada split).
>
>La función *reduce* se ejecuta 2 veces, ya que se generan dos grupos con clave 1 y 2.
>
>Se ejecuta un *mapper*  por cada split, osea 4 *mappers*.
>
>***preguntar lo de los reducers***
>
>Recibe la clave k2 ('1' o '2') y una lista de elementos v2 (los de la clave 1: 34, 10, 12, 36, 3, 15, 14, 3; y los de clave 2: 21, 32, 23, 4, 30, 31, 32, 19).
>
>El job escribe (1, 36) y (2, 32).

#### d) Job D

```python
def map(k1, v1, context):
    for v in range(v1):
        context.write(k1, v1)

def reduce(k2, v2, context):
    n = 0
    for v in v2:
        n = n + 1
    context.write(k2, n)
```

>La función *map* se ejecuta 16 veces (cada fila de cada split).
>
>La función *reduce* se ejecuta 14 veces, ya que genera un grupo por cada clave k1 no repetida de los 4 splits.
>
>Se ejecuta un *mapper*  por cada split, osea 4 *mappers*.
>
>***preguntar lo de los reducers***
>
>Recibe la clave y una lista con todos los valores emitidos para esa clave. Como el map escribe (k1, v1) repetido v1 veces, la lista de cada clave tiene tantos elementos como indica su propio valor, y todos los elementos son ese mismo valor. Por ejemplo, la clave 34 recibe [21, 21, 21, …] con 21 elementos.
>
>El job escribe:

| k3  | v3  |
| --- | --- |
| 3   | 36  |
| 4   | 97  |
| 10  | 18  |
| 12  | 12  |
| 14  | 18  |
| 15  | 10  |
| 19  | 35  |
| 21  | 34  |
| 23  | 45  |
| 30  | 91  |
| 31  | 32  |
| 32  | 98  |
| 34  | 21  |
| 36  | 18  |
#### e) Job E

```python
def map(k1, v1, context):
    context.write(v1, k1)

def reduce(k2, v2, context):
    n = 0
    for v in v2:
        n = n + 1
        context.write(v, n)
```

>

---
### 2)

El dataset **Libros** provisto por la cátedra almacena libros cada uno en un archivo separado. Dentro de cada archivo, la primera línea tiene el título del libro y luego en las líneas siguientes un párrafo por línea. Ejecute el proyecto WordCount dado por la cátedra para saber cuántas veces es utilizada cada palabra.
### 3)

En el ejercicio anterior ¿Cómo haría para obtener el top 20 de las palabras más usadas?
```python
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
```
### 4)
Modifique el proyecto WordCount para contar cuántas vocales, consonantes, dígitos, espacios y otros caracteres posee el data set **Libros**.
```python
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
```
### 5)
Indique si utilizando el dataset **Libros** es posible resolver los siguientes problemas:
a. Obtener los títulos de todos los libros 
```python
def fmap(key, value, context):
	for palabra in value.split():
		context.write(palabra,1)

def fred(key, values, context):
	context.write(key, "")
```

b. Obtener la cantidad de palabras promedio por párrafo
```python
def fmap(key, value, context):
	context.write(".", len(value.split()))

def fred(key, values, context):
	cant = 0
	sum = 0
	for v in values:
		sum += v
		cant += 1
	context.write("PROMEDIO de palabras por párrafo: ", sum / cant)
```

c. Obtener la cantidad de párrafos promedio por libro
```python
inputPath = Path(inputDir)
cantLibros = sum(1 for item in inputPath.iterdir() if item.is_file())

def fmap(key, value, context):
	if not (value.strip()).isspace():
		context.write(".", 1)

def fred(key, values, context):
	cant = 0
	for v in values:
		cant += v
	context.write("PROMEDIO de párrafos entre todos los libros: ", cant / cantLibros)
```

d. Obtener la cantidad de caracteres del párrafo más extenso
```python
def fmap(key, value, context):
	cant = 0
	for c in value.strip():
		cant += 1
	context.write(".", cant)

def fred(key, values, context):
	max = -sys.maxsize - 1
	for v in values:
		if v > max:
			max = v
	context.write("CANTIDAD de caracteres del párrafo más largo: ", max)
```

e. Cantidad total de párrafos con diálogos (se entiende por párrafo con diálogo aquel que empieza con un guión) 
```python
def fmap(key, value, context):
	if value[:2] == "--":
		context.write(".", 1)

def fred(key, values, context):
	cant = 0
	for v in values:
		cant += v
	context.write("CANTIDAD de párrafos con diálogos: ", cant)
```

f. El diálogo más largo (se entiende por diálogo a una secuencia de párrafos con diálogo que aparecen de manera consecutiva)
```python

```

g. El top 20 de las palabras más usadas por cada libro
### 6)
Una empresa proveedora de internet realizó una encuesta para conocer el grado de satisfacción de sus clientes, en un formulario web los clientes debían completar un campo con los textos "Muy satisfecho", "Algo satisfecho", "Poco satisfecho", "Disconforme" o "Muy disconforme". Utilice el dataset **Encuesta** para saber cuántos clientes están en cada una de las cinco categorías.

### 7)

El dataset **Inversionistas** posee los nombres, dni, fecha de nacimiento (día, mes y año como campos separados) e importe invertido por diferentes personas en la apertura de un nuevo negocio en la ciudad. Se desea saber:

a. El nombre del inversionista más joven b. El total del importe invertido por todos los inversionistas c. El promedio de edad

Implemente una solución en MapReduce. ¿Se puede resolver los tres problemas en un único job?

### 8)

Si contáramos con un cluster donde podemos configurar 100 nodos para la tarea de reduce ¿De qué manera se podrían usar esos 100 nodos en el ejemplo de los eventos POSITIVO, NEGATIVO y NEUTRO visto en la teoría?