# Historia
- El Framework Hadoop es creado en 2003 por Google para procesar grandes volúmenes de datos.
- En 2006, Yahoo continúa con el desarrollo del proyecto Hadoop. Aparece Hadoop Reduce.
- Hoy pertenece a Apache https://hadoop.apache.org/.
# Hadoop
- Framework que soporta procesamiento sobre grandes volúmenes de datos en un ambiente distribuido.
- Ejecuta aplicaciones para ese fin.
- Incluye un sistema de archivos distribuidos (HDFS).
- Tolerante a fallas.
- Diseñado para el procesamiento offline de datos (batch).
- Idea *escriba una sola vez y lea muchas*.
	- Cada lectura la hace de manera completa, de inicio a fin.
- No permite lectura aleatoria.
## Componentes![[Pasted image 20260825141814.png|631]]
## HDFS
- Todos los archivos se dividen en bloques del miEn Hadoop la administración de los procesos que
se ejecutan en el cluster la lleva a cabo un
framework llamado Yarn MapReducesmo tamaño (64MB por defecto).
- Físicamente, los bloques podrían estar en cualquier computadora.
- Permite la réplica de bloques para optimización y recuperación de fallas.
### Procesos
Son de tipo maestro-esclavo.
- Namenode (master):
	- Maneja el árbol del FS y los metadatos de archivos y carpetas.
	- Conoce, para cada bloque del FS, qué datanode lo maneja.
	- Vínculo con el FS del SO.
- Secondary namenode: realiza tareas auxiliares al namenode.
- Datanode (slave):
	- Son lo que llevan a cabo la lectura y escritura de los bloques en el filesystem del SO.
	- Lleva a cabo la creación, borrado y replicado de los bloques.

En Hadoop la administración de los procesos que se ejecutan en el cluster la lleva a cabo un framework llamado Yarn MapReduce.
Básicamente Yarn realiza los trabajos usando dos procesos diferentes:
- Job tracker: maneja todos los trabajos a ser procesados. Tiene en cuenta el mapa del cluster al momento de crear los procesos Task.
- Task tracker: son los encargados de realizar el procesamiento de los datos.