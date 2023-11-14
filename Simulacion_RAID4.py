"""
Debido a que todos los servidores no tendrían la misma longitud, se va a proceder a añadir espacios en las últimas
posiciones de los servidores 2, 3 y 4. Esto se podía haber solucionado de forma trivial añadiendo espacios en el texto original.
Otra forma que se implementó pero se consideró menos eficiente y más compleja sería utilizar "if" para q no recorra
posiciones vacías en los arrays.

"""
#Texto original
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

array = []
for bloque in range(0, len(texto), 4):  
    # Obtener el bloque de 4 caracteres
    bloque_4_caracteres = texto[bloque:bloque+4]
    # Si el bloque tiene menos de 4 caracteres, añadir espacios en blanco al final. 
    bloque_4_caracteres = bloque_4_caracteres.ljust(4)
    # Dividir el bloque de 4 caracteres por caracteres
    bloque_dividido = [c for c in bloque_4_caracteres]
    array.append(bloque_dividido)

servidor5 = []  # Crear el array para el servidor 5

#Cálculo de la paridad
for sub_array in array:
    paridad = 0  # Inicializar el contador de paridad en 0
    for c in sub_array:
        paridad ^= ord(c)  # Aplicar operación XOR con el código ASCII de cada caracter
    servidor5.append(paridad)

print("Servidor 5:", servidor5)

# Suponiendo que tenemos 4 servidores de datos y se quiere enviar los caracteres a variables correspondientes a cada servidor
servidor1 = []
servidor2 = []
servidor3 = []
servidor4 = []

for sub_array in array:
    for i in range(len(sub_array)):
        if i == 0:
            servidor1 += sub_array[i]
        elif i == 1:
            servidor2 += sub_array[i]
        elif i == 2:
            servidor3 += sub_array[i]
        elif i == 3:
            servidor4 += sub_array[i]

print("Servidor 1:", servidor1)
print("Servidor 2:", servidor2)
print("Servidor 3:", servidor3)
print("Servidor 4:", servidor4)

# Se procede ahora a realizar la lectura del texto original

# Crear subarrays vacíos para cada servidor
subarrays = [[] for i in range(len(servidor1))]

# Agregar elementos de cada servidor a los subarrays
for i in range(len(servidor1)):
    subarrays[i].append(servidor1[i])
    subarrays[i].append(servidor2[i])
    subarrays[i].append(servidor3[i])
    subarrays[i].append(servidor4[i])

print(subarrays)

# Verificar la paridad de los datos 
paridad_recu = []
for bloque in subarrays:
    paridad_total = 0
    for c in bloque:
        paridad_total ^= ord(c)
    paridad_recu.append(paridad_total)

if paridad_recu != servidor5:
    print("Error: los datos recibidos no son correctos.")
else:
    print("Los datos recibidos son correctos:")

# Concatenar caracteres de los subarrays
datos_completos = []
for subarray in subarrays:
    datos_completos.append(''.join(subarray))

texto_completo = ''.join(datos_completos)
print(texto_completo)

#Se realiza la parte 3 donde simulamos la caída de un servidor y necesitamos recuperar dicho información

# Simular caída del servidor 3
servidor3_recu = []

for i in range(len(servidor1)):
    # Aplicar operación XOR para recuperar el caracter
    caracter_recuperado = chr(ord(servidor1[i]) ^ ord(servidor2[i]) ^ ord(servidor4[i]) ^ servidor5[i])
    servidor3_recu.append(caracter_recuperado)

print("Servidor 3 (recuperado):", servidor3_recu)

# LECTURA A PARTIR DE LOS SERVIDORES Y EL SERVIDOR RECUPERADO

# Crear subarrays vacíos para cada servidor
subarrays = [[] for i in range(len(servidor1))]

# Agregar elementos de cada servidor a los subarrays
for i in range(len(servidor1)):
    subarrays[i].append(servidor1[i])
    subarrays[i].append(servidor2[i])
    subarrays[i].append(servidor3_recu[i])
    subarrays[i].append(servidor4[i])

# Verificar la paridad de los datos totales
paridad_recu = []
for bloque in subarrays:
    paridad_total = 0
    for c in bloque:
        paridad_total ^= ord(c)
    paridad_recu.append(paridad_total)

if paridad_recu != servidor5:
    print("Error: los datos recibidos no son correctos.")
else:
    print("Los datos recibidos son correctos:")

# Concatenar caracteres de los subarrays
datos_completos = []
for subarray in subarrays:
    datos_completos.append(''.join(subarray))
#Recuperamos el texto original.
texto_completo = ''.join(datos_completos)
print(texto_completo)
