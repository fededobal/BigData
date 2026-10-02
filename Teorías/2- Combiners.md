# Función combiner
Objetivo: disminuir la cantidad de datos que se van a transmitir entre nodos.
- Se ejecuta con la salida de los mappers.
- Se ejecuta en el mismo nodo dónde se ejecutó el map.
- Hadoop no garantiza cuantas veces es invocada esta función, ya que internamente es solo una "tarea de optimización".
![[Pasted image 20260901142501.png]]Solo cuando el planificador estima que la tarea de combiner no liberará espacio en RAM, comienza con la escritura de las tuplas intermedias en el HDFS para ser pasadas al reducer de otro nodo.
![[mapreduce_interfaces.png|700]]![[Pasted image 20260901144706.png|700]]