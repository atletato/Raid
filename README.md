# Simulación de un RAID

# Descripción
El proyecto consiste en una aplicación que simula la utilización de un sistema de almacenamiento basado en RAID.
Un RAID, también conocido como "Redundant Array of Independent Disks", consiste en una tecnología de sistemas de almacenamiento cuyo objetivo se basa en proteger los datos
y mejorar el rendimiento de las operaciones de lectura/escritura.
Hay distintos niveles de Raid y combinación de estos niveles para formar otro nuevos. Cada uno de estos niveles tiene una función concreta y proporciona tanto ventajas como desventajas frente a otros.
Un RAID se basa en tres conceptos: striping (separación de los datos), mirroring (copia de los datos) y parity (paridad de los datos).

En este ejemplo, se procede a simular el funcionamiento de un RAID 4. Este sistema de almacenamiento hace uso del striping, cuyo método divide la información en pequeños bloques almacenados de forma distribuida.
Pretende mejorar la velocidad de acceso, realizando operaciones E/S más pequeñas a las originales pero de forma parelela. Además, hace uso de un disco para almacenar la paridad, proporcionando tolerancia a fallos en un disco.

# Tarea
En el script creado se proporciona un string que procederá a almacenarse en 4 "servidores" de datos distintos (en nuestro caso *listas*) mediante striping y otro servidor que almacene la paridad.
Primeramente se pedirá una simulación en escritura de este archivo, para su posterior lectura utilizando el conjunto de los servidores.
Finalmente, para mostrar la utilidad de este tipo de RAID, simularemos la caída de uno de los servidores de datos y se procederá a la lectura a partir de 3 servidores de datos y la paridad,
consiguiendo que se muestre la lectura completa del archivo.

# Uso
Será necesario únicamente tener instalado python3 para correr el archivo y que se muestre por pantalla de la terminal el resultado final de la simulación.

# Autor
Desarrollado por: Jose Carrascal.

La tarea fue propuesta por Jesús F. Rodríguez-Aragón en el máster de BigData UVA.


