- Es un framework para distribuir tareas en múltiples nodos.
- *Escriba una vez y lea muchas veces*.
- Ventajas:
	- Paralelización y distribución de tareas automática.
	- Escalable.
	- Tolerante a fallos.
	- Monitoreo y capacidad de seguridad.
	- Flexibilidad de programación (Java, Python, C#, Ruby, C++).
	- Abstracción al programador.
- Es un paradigma de programación porque establece una forma de pensar los problemas sin tener acceso a todos los datos.
# Ejemplo para cálculo de promedio
```python
acum = 0
for d in datos:
	acum = acum + d
prom = suma / len(datos)
```
Esto es secuencial. Se debe repensar de forma paralela: *pedirle a cada nodo que sume y cuente sus datos*...
```python
acum = 0; n = 0
for nodo in cluster:
	acum = acum + nodo.acum
	n = n + nodo.n
promedio = acum / n
```
# Conceptos
- Toda tarea MapReduce se divide en dos fases:
	- Fase map: en la que los datos de entrada son procesados, uno a uno, y transformados en un conjunto intermedio de datos.
	- Fase reduce: se reúnen los resultados intermedios y se reducen a un conjunto de datos resumidos, que es el resultado final de la tarea.
## Job
- La unidad de trabajo de MapReduce es un **Job**.
	- Un Job se divide en una tarea map y una tarea reduce.
	- Los Jobs de MapReduce son controlados por un daemon conocido como JobTracker, el cual reside en el "nodo master".
	- Los clientes envían Jobs MapReduce al JobTracker y este distribuye la tarea usando otros nodos del cluster.
	- Esos nodos se conocen como TaskTracker y son responsables de la ejecución de la tarea asignada y reportar el progreso al JobTracker.
- Los jobs se dividen en 4 fases:
	1. **Map**
	2. Shuffle
	3. Sort
	4. **Reduce**
- Map y Reduce son las fases que se deben programar.
- Shuffle y Sort son internas a la ejecución del job.
# Tareas Map y Reduce
Las tareas de map y reduce trabajan con el concepto de <clave, valor>.
![[Pasted image 20260825145926.png]]
## Entrada de datos
MapReduce se alimenta de uno o más archivos.
- Texto plano: cada línea del archivo es un dato a procesar.
- La clave de los archivos de texto plano es el offset de la línea dentro del archivo.
El o los archivos de entrada son divididos en "**splits**" y cada TaskTracker trabaja sobre un "split".
## Tarea Map
Se ejecutan múltiples instancias de la tarea map sobre diferentes porciones del dataset.
Se intenta que cada map se ejecute sobre una copia local del dataset para minimizar el tráfico de datos. Una tarea map solo ve una porción del dataset de entrada.

La tarea map lee los datos en forma de pares <k1, v1> y produce una lista de cero, uno o más pares <k2, v2>.
- <k1, v1> --> list(<k2, v2>)
```python
def map(k1, v1):
	values = v1.split()
	acum = 0
	for v in values:
		acum = acum + float(v)
	return ( 1 , (acum, len(values)))
```
## Tarea Reduce
Finalizadas las tareas intermedias shuffle y sort se ejecuta la tarea reduce.
La tarea reduce tiene todos los elementos para poder realizar cualquier operación de "resumen".

Reduce lee los datos en forma de pares <k2, list(v2)> y produce una lista de cero o más pares <k3, v3>.
- <k2, list(v2)> --> list(<k3, v3>)
```python
def reduce(k2, v2):
	acum = 0; n = 0
	for v in v2:
		acum = acum + v[0]
		n = n + v[1]
	return ( k2 , acum / n)
```
# Ejemplo: conteo de eventos por resultado

## Enunciado

Se posee un dataset con resultados de eventos. De cada evento se conoce su resultado (`"POSITIVO"`, `"NEUTRO"`, `"NEGATIVO"`).
Se desea saber cuántos eventos positivos, neutrales y negativos hay en todo el dataset.
## El dataset
El dataset es uno o más archivos de texto donde en cada línea está el resultado del evento.
```
…
POSITIVO
POSITIVO
NEGATIVO
NEUTRO
POSITIVO
NEUTRO
NEGATIVO
NEGATIVO
NEUTRO
POSITIVO
NEGATIVO
…
```
## Tarea map
La intención es contar la ocurrencia de cada tipo de evento. `v1` es el tipo de evento (`"POSITIVO"`, `"NEUTRO"`, `"NEGATIVO"`).

Primer intento — ¿qué pasa si usamos una única clave intermedia?
```python
def map(k1, v1):
    return (1, v1)
```

Versión correcta: el valor se usa como clave intermedia. El valor intermedio
`v2` no se usa, por eso se le pone un valor arbitrario.
```python
def map(k1, v1):
    return (v1, 1)
```
### Tarea map — Ejemplo

| TaskTracker | Input            | Output          |
| ----------- | ---------------- | --------------- |
| TT1         | `<1, POSITIVO>`  | `<POSITIVO, 1>` |
| TT1         | `<2, POSITIVO>`  | `<POSITIVO, 1>` |
| TT1         | `<3, NEGATIVO>`  | `<NEGATIVO, 1>` |
| TT2         | `<4, NEUTRO>`    | `<NEUTRO, 1>`   |
| TT2         | `<5, POSITIVO>`  | `<POSITIVO, 1>` |
| TT2         | `<6, NEUTRO>`    | `<NEUTRO, 1>`   |
| TT2         | `<7, NEGATIVO>`  | `<NEGATIVO, 1>` |
| TT3         | `<8, NEGATIVO>`  | `<NEGATIVO, 1>` |
| TT3         | `<9, NEUTRO>`    | `<NEUTRO, 1>`   |
| TT3         | `<10, POSITIVO>` | `<POSITIVO, 1>` |
| TT3         | `<11, NEGATIVO>` | `<NEGATIVO, 1>` |
## Tarea reduce
Cada TaskTracker que ejecuta la tarea reduce recibe todas las tuplas del tipo `"POSITIVO"`, `"NEUTRO"` o `"NEGATIVO"`. Solo hay que contar cuántas ocurrencias existen. Tendremos una salida por cada tipo de evento.

```python
def reduce(k2, v2):
    n = 0
    for v in v2:
        n = n + 1
    return (k2, n)
```
En este ejemplo se ejecutan **tres reducers**, uno por cada una de las tres claves intermedias.
### Ejemplo "POSITIVO"

| TaskTracker | Input                                           | Output           |
| ----------- | ----------------------------------------------- | ---------------- |
| TT4         | `<POSITIVO, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]>` | `<POSITIVO, 11>` |
