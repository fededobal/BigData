# Proceso iterativo
BBDD -> Job -> Resultados parciales -> Job (N veces) -> Resultados final
# Ejemplo - Método de Jacobi
Resolver sistemas de ecuaciones lineales cuadrados (igual cantidad de ecuaciones que de incógnitas).
$$
X - 3Y - (1/2)Z = 1
$$
$$
(-1/10)X + Y - (1/10)Z = -4
$$
$$
(-1/2)X – (1/2)Y + Z = 1
$$

Se inicia con un valor arbitrario para cada incógnita. Ejemplo: (X0 = 1; Y0 = 2; Z0 = 3). Con los valores de la iteración i se calculan las variables de la iteración i+1:
- Xi+1 = 8,5; Yi+1 = -3,6; Zi+1 = 2,5
- Xi+2 = -8,55; Yi+2 = -2,9; Zi+2 = 3,45

![[Pasted image 20260908141915.png]]

```python
error = 0.01
dif = 1
incog = {"X": 1, "Y": 2, "Z": 3}
while (dif >= error):
	calcular (incogi, incogi+1) # llamada al Job
	dif = (Xi+1- Xi)^2 + (Yi+1- Yi)^2 + (Zi+1- Zi)^2 
```
## Dataset
```
<var_1, t_i, c_1, c_2, . . ., c_N>
<var_2, t_i, c_1, c_2, . . ., c_N>
<var_3, t_i, c_1, c_2, . . ., c_N>
. . .
<var_N, t_i, c_1, c_2, . . ., c_N>
```
## Map
| Incog. | Indep | Z    | Y   | X      |
| ------ | ----- | ---- | --- | ------ |
| < X    | 1     | 0    | 3   | 1/2 >  |
| < Y    | -4    | 1/10 | 0   | 1/10 > |
| < Z    | 1     | 1/2  | 1/2 | 0 >    |
```python
def map(key, value, context):
	vars = (1, 1, 2, 3)
	coefs = value.split("\t")
	res = 0
	for v in range(4):
		res = res + vars[i] * coefs[i]
	context.write(key, res)
```
## Reduce
| Incog. | Valor  |
| ------ | ------ |
| < X    | 8.5 >  |
| < Y    | -3.6 > |
| < Z    | 2.5 >  |
```python
def reduce(key, values, context):
	res = 0
	for v in values:
		res = v
	context.write(key, res)
```
# Parametrización
A veces, en algunos problemas, resulta útil pasar parámetros a los diferentes jobs para que estos realicen su tarea.
Los valores se setean el driver y estos son pasados a los TaskTracker que ejecutan los mappers y los reducers.
## Método de Jacobi
Inicialmente el driver envía un valor arbitrario para cada incógnita.
Esos valores son enviados a todos los TaskTracker
Finalizado el job, lee los datos que resultaron del job y los utiliza para:
- Calcular el error para chequear la condición de fin
- Enviarlos nuevamente a los TaskTracker en una nueva iteración, si se debe continuar
```python
def map(key, value, context):
	vars = context["incognitas"]
	coefs = value.split("\t")
	res = 0
	for v in range(4):
		res = res + vars[i] * coefs[i]
	context.write(key, res)
```

Driver:
```python
job = Job(inputDir, outputDir, fmap, fred)
coefs = {"incognitas": [1, 1, 2 , 3]}
job.setParams(coefs)
success = job.waitForCompletion()
```