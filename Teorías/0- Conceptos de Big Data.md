Big Data como:
- Concepto de marketing: usado al principio por Google para indexar muchas páginas web
	- Redes sociales
	- Sitios de archivos multimediales
	- Sitios de e-commerce
- Consecuencia del avance tecnológico que permitió generar y capturar datos de sensores de tiempo real, lo que involucró un crecimiento exponencial del volumen de datos
# Puesto en números
- En 2015 el universo digital estaba compuesto por 16 ZB de datos.
- En 2025 se prevee un volumen de 181 ZB.
- 1 Zettabyte =1000 Hexabyte
- 1 Hexabyte = 1000 Petabyte
- 1 Petabyte = 1000 Terabyte
- 181 ZB en discos de 10TB ➔ +18.000.000.000 discos
	- Peso: +13.500.000 toneladas (≈135 portaaviones)
	- Altura: +450.000 Km (≈35.5 planetas Tierra; ≈3.2 planetas Júpiter)

![[Pasted image 20260818143444.png]]

# Cómo determinar qué es Big Data y qué no
- No es fácil determinar el límite entre un problema de Big Data del que no lo es.
- Depende de los datos, fuentes, tipo, recolección, etc.
- Depende del procesamiento, almacenamiento, consultas.
- Depende del costo.
# Costos
## Cloud
En AWS, un cluster de 4 instancias con
- 2 vCPU con 4 GB de RAM
- 1 TB de almacenamiento
![[Pasted image 20260818144451.png]]

478.51 x 12 meses = U$D 5742.12
## No cloud
- 4 CPU
- 4GB de RAM
- 1 TB
![[Pasted image 20260818144602.png]]

(501.11+45.99) * 4 = U$D 2188.4

Conviene más el Cloud porque quien lo alquila se despreocupa de problemas como:
- variaciones de tensión
- inseguridad
- limitaciones propias
# Definición
> [!NOTE] Según el IDC:
> Big data representa una nueva generación de tecnologías y arquitecturas, diseñadas para extraer valor económicamente de volúmenes muy grandes de una amplia variedad de datos, al permitir la captura, el descubrimiento y/o análisis de alta velocidad.
## Las tres V
- Volumen: el universo digital sigue expandiendo sus fronteras.
- Velocidad: la velocidad a la que generamos datos es muy elevada, y la proliferación de sensores es un buen ejemplo de ello. Además, los datos en tráfico –datos de vida efímera, pero con un alto valor para el negocio crecen más deprisa que el resto del universo digital.
- Variedad: los datos no solo crecen sino que también cambian su patrón de crecimiento, a la vez que aumenta el contenido desestructurado.
## La cuarta V
Valor: extraer valor de toda esta información marcará el futuro del manejo de información.
Se puede encontrar de diferentes formas:
- mejoras en el rendimiento del negocio
- segmentación de clientes
- tomas de decisiones
- automatización de decisiones tácticas
- etc
# Datos
## Datos estructurados
Representan aprox. el 20% del universo digital.
Ejemplo de alojamiento:
- BBDD relacionales
Generados por humanos mediante:
- Ingreso de datos
- Actividad web
- Datos generados por juegos
- Informes, reportes
- Redes sociales
Generados por computadoras mediante:
- Sensores
- Logs
- Códigos de barra
- Operaciones bancarias
- Imágenes satelitales
- Monitoreo geológico
- Fotografía
- Video
- Radares
## Datos semiestructurados
- Texto plano
- Planillas de cálculo
## Datos no estructurados
Representan aprox. el 80% del universo digital.
- Texto escrito en lenguaje natural
- Multimedia
## DBMS
### Relacionales
- MySQL
- PostgreSQL
- Derby
### No relacionales
#### Clave/valor
No requieren un esquema, no son tipadas (usualmente todo se almacena en string).
Ej.: Riak.
#### Documentos
Formato JSON. Útil cuando se generan muchos reportes.
Ej.:
- MongoDB
- CouchDB
#### Orientadas a columnas
Permite el agregado simple de columnas, llenándose fila a fila. Usando BigTable de Google.
Ej.: Hbase.
#### Orientadas a grafos
Elemento básico: nodo-relación. Se navega nodo a nodo siguiendo las relaciones. Ej.: Neo4J.
# Tiempo real
## Problemas de tiempo real
- Detección de fraudes
- Detección de fallas
- Determinar eventos en redes sociales para detectar alertas tempranas
- Publicidad web
## Problemas de no tiempo real (batch)
- Segmentación de clientes
- Tomas de decisiones (semanales, mensuales, anuales, etc.)
# Tecnologías
Big Data no es una sino varias tecnologías útiles para hacer más fácil el tratamiento de los datos.
Se necesita hardware y software específico.
- Clusters, sistemas distribuidos, etc.
- Cloud computing
![[Pasted image 20260818151652.png]]
