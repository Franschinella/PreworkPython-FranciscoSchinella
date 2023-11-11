print('EJERCICIOS PYTHON')

print('Variables y Operadores')

'''
1- Crea una variable llamada <nombre> y asígnale tu nombre como valor. Luego, imprime la variable
'''
nombre = "Francisco"
print("Francisco")

'''
2- Crea dos variables, <a> y <b> y asígnales los valores 5 y 10 respectivamente. Luego, imprime la suma de <a> y <b>
'''
a = 5
b = 10
print(a + b)

'''
3- Calcula el área de un triángulo con base 10 y altura 5
'''
a = 5
b = 10
area = (b * a) / 2
print(area)

'''
4- Calcula el resto de dividir 17 entre 3
'''
print(17/3)

print('Condicionales')

'''
1- Dado un número, imprime si es positivo o negativo
'''
x = 10
if x > 0:
  print(x, "es positivo")

'''
2- Dado un número, imprime si es par o impar
'''
n = 10
if n % 2 == 0:
  print(n, "es par")

'''
3- Dado tres números, encuentra y muestra el mayor de ellos
'''
lista = [5,14,13]
print(max(lista))

print('Bucles')

'''
1- Imprime los números del 1 al 10 usando un bucle FOR
'''
for i in range (1,11):
  print(i)

'''
2- Imprime los números pares del 1 al 20 usando un bucle WHILE
'''
x=1
while x<21:
  if x%2==0:
    print(x)
  x+=1

'''
3- Usa un bucle para calcular la suma de los números del 1 al 100
'''
numeros = range(1,101)
suma = sum(numeros)
print(suma)

print('Funciones')

'''
1- Define una función que tome dos números y retorne su suma
'''
def suma (a,b):
  return a + b
resultado = suma(5,3)
print(resultado)

'''
2- Define una función que tome un número y retome su factorial
'''
def factorial(n):
   if n==0 or n==1:
     resultado=1
   elif n>1:
     resultado=n*factorial(n-1)
   return resultado
resultado = factorial(5)
print(resultado)

'''
3- Define una función que tome un número y determine si es primo
'''
def n_primo(numero):
  if numero < 2:
    return "No es un número primo"
  for i in range(2, numero):
     if  (numero % i)== 0:
        return "No es un número primo"
  return "Es un número primo"
resultado = n_primo(5)
print(resultado)

'''
4- Define una función que reciba una lista de números y retorne la suma de ellos
'''
def suma_lista(numeros):
  suma = 0
  for numero in numeros:
    suma += numero
  return suma
mi_lista = [1, 2, 3, 4, 5]
print(suma_lista(mi_lista))

'''
5- Define una función que reciba una cadena de texto y retorne la cadena en reversa
'''
cadena = "Me irá bien en todo lo que me proponga"
cadena_inversa = cadena[::-1]
print(cadena_inversa)

print('Ejercicios Nivel Básico')

'''
1- Crear una función para verificar si un número es par o impar y devuelva "El número es par" o "El número es impar" según corresponda.
'''
def es_par(numero):
  return numero % 2 == 0
num = int(input("Ingresa un número: "))
if es_par(num):
  print("Es un número par")
else:
  print("Es un número impar")

'''
2- Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado
'''
def factorial(numero):
  resultado = 1
  for i in range(1, numero + 1):
    resultado *= i
  return resultado
num = int(input("Ingresa un número: "))
print("El factorial de", num, "es: ", factorial(num))

'''
3- Crea una funcipon a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de "La candidad de dígitos es: " y el resultado total de dígitos
'''
def contar_digitos(numero):
  return len(str(numero))
num = int(input("Ingresa un número: "))
print("La cantidad de dígitos es: ", contar_digitos(num))

'''
4- Dada una lista de números, crea una función que devuelva el número máximo de la lista
'''
def encontrar_maximo(lista):
  maximo = lista[0]
  for numero in lista:
    if numero > maximo:
      maximo = numero
  return maximo
numeros = [5, 12, 3, 8, 9]
print("El número máximo es: ", encontrar_maximo(numeros))

'''
5- Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado
'''
def sumar_digitos(numero):
  suma = 0
  while numero > 0:
    suma += numero % 10
    numero //= 10
  return suma
num = int(input("Ingresa un número: "))
print("La suma de los dígitos es: ", sumar_digitos(num))

'''
6- Dados dos números, crear una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM
'''
def mcm(a, b):
  if a == 0 or b == 0:
    return 0
  else:
    maximo = max(a, b)
    while True:
      if maximo % a == 0 and maximo % b == 0:
        return maximo
      maximo += 1
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print("El MCM es: ", mcm(num1, num2))

'''
7- Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo
'''
def calcular_area_triangulo(base, altura):
  return(base * altura) / 2
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
print("El área del triángulo es: ", calcular_area_triangulo(base, altura))

'''
8- Crea una función que, dado un número, verifique si es positivo, negativo o cero
'''
def verificar_signo(num):
  if num > 0:
    return "positivo"
  elif num < 0:
    return "negativo"
  else:
    return "cero"
num = float(input("Ingresa un número: "))
print("El número es: ", verificar_signo(num))

'''
9- Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra
'''
def contar_letras(palabra):
  contador = 0
  for letra in palabra:
    if letra.isalpha():
      contador += 1
  return contador
palabra = input("Ingresa una palabra: ")
print("La cantidad de letras es: ", contar_letras(palabra))

'''
10- Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto
'''
def valor_absoluto(lista):
  for i in range(len(lista)):
    lista[i] = abs(lista[i])
  return lista
numeros = [5, -12, 3, -8, 9]
print("Lista con valores absolutos:", valor_absoluto(lista))

'''
11- Crea una función que, dado un número, verifique si es primo
'''
def es_primo(numero):
  if numero <= 1:
    return False
  for i in range(2, numero):
    if numero % i == 0:
      return False
    return True
num = int(input("Ingresa un número: "))
if es_primo(num):
  print("Es un número primo")
else:
  print("No es un número primo")

'''
12- Dado dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números
'''
def mcd(a, b):
  while b:
    a, b = b, a % b
  return a
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número:"))
print("El MCD es: ", mcd(num1, num2))

print('Ejercicios Nivel Medio')

'''
1- Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.
'''
def fibonacci(n):
  fib_series = [0, 1]
  if n <= 0:
    print("Ingresa un número entero positivo.")
  elif n == 1:
    print(f"Los primeros {n} números de la serie de Fibonacci son: {fib_series[0]}")
  else:
    for _ in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)
        
    print(f"Los primeros {n} números de la serie de Fibonacci son: {fib_series}")
n = int(input("Ingresa la cantidad de números de la serie de Fibonacci a imprimir: "))
fibonacci(n)

'''
2- Define una función que tome un número y retorne una lista de sus divisores.
'''
def obtener_divisores(numero):
  divisores = []
  for i in range(1, numero + 1):
    if numero % i == 0:
      divisores.append(i)
  return divisores
num = int(input("Ingresa un número: "))
lista_divisores = obtener_divisores(num)
print(f"Los divisores de {num} son: {lista_divisores}")

'''
3- Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
'''
def elementos_unicos(lista):
  return list(set(lista))
lista_original = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = elementos_unicos(lista_original)
print(f"Lista original: {lista_original}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")

'''
4- Define una función que tome un número y retorne la suma de sus dígitos.
'''
def suma_digitos(numero):
  suma = 0
  for digito in str(numero):
    suma += int(digito)
  return suma
num = int(input("Ingresa un número: "))
resultado = suma_digitos(num)
print(f"La suma de los dígitos de {num} es: {resultado}")

'''
5- Define una función que tome una cadena y cuente el número de vocales en la cadena.
'''
def contar_vocales(cadena):
  cadena = cadena.lower()
  contador_vocales = 0
  for caracter in cadena:
    if caracter in "aeiou":
      contador_vocales += 1
  return contador_vocales
texto = input("Ingresa una cadena de texto: ")
numero_vocales = contar_vocales(texto)
print(f"El número de vocales en la cadena es: {numero_vocales}")

'''
6- Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
'''
def primeros_n_elementos(lista, n):
  return lista[:n]
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Ingresa el número de elementos que deseas obtener: "))
resultado = primeros_n_elementos(mi_lista, n)
print(f"Los primeros {n} elementos de la lista son: {resultado}")

'''
7- Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
'''
def contar_letras_mayus_minus(cadena):
  mayusculas = 0
  minusculas = 0
  for caracter in cadena:
    if caracter.isupper():
      mayusculas += 1
    elif caracter.islower():
      minusculas += 1
  return mayusculas, minusculas
texto = input("Ingresa una cadena de texto: ")
mayusculas, minusculas = contar_letras_mayus_minus(texto)
print(f"Cantidad de letras mayúsculas: {mayusculas}")
print(f"Cantidad de letras minúsculas: {minusculas}")

'''
8- Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
'''
def es_numero_perfecto(numero):
  if numero <= 0:
    return False
  suma_divisores = sum(divisor for divisor in range(1, numero) if numero % divisor == 0)
  return suma_divisores == numero
num = int(input("Ingresa un número para verificar si es perfecto: "))
resultado = es_numero_perfecto(num)
if resultado:
  print(f"{num} es un número perfecto.")
else:
  print(f"{num} no es un número perfecto.")

'''
9- Define una función que reciba un número y retorne su representación en binario.
'''
def representacion_binaria(numero):
  return bin(numero)
num = int(input("Ingresa un número para obtener su representación en binario: "))
resultado_binario = representacion_binaria(num)
print(f"La representación en binario de {num} es: {resultado_binario}")

'''
10- Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
'''
def interseccion_listas(lista1, lista2):
  return list(set(lista1) & set(lista2))
lista_a = [1, 2, 3, 4, 5]
lista_b = [3, 4, 5, 6, 7]
resultado_interseccion = interseccion_listas(lista_a, lista_b)
print(f"Intersección de las listas: {resultado_interseccion}")

'''
11- Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
def es_palindromo(cadena):
  cadena = cadena.replace(" ", "").lower()
  return cadena == cadena[::-1]
texto = input("Ingresa una cadena para verificar si es un palíndromo: ")
resultado = es_palindromo(texto)
if resultado:
  print(f"{texto} es un palíndromo.")
else:
  print(f"{texto} no es un palíndromo.")

'''
12- Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
'''
for num in range(1, 51):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)

'''
13- Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
'''
def ordenar_ascendente(lista):
  return sorted(lista)
mi_lista = [5, 2, 8, 1, 3]
lista_ordenada = ordenar_ascendente(mi_lista)
print(f"Lista original: {mi_lista}")
print(f"Lista ordenada en orden ascendente: {lista_ordenada}")

'''
14- Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
'''
def palabras_mas_largas_que_n(lista_palabras, n):
  return [palabra for palabra in lista_palabras if len(palabra) > n]
lista_palabras = ["python", "programacion", "lista", "palabras", "corta"]
longitud_minima = 6
palabras_mas_largas = palabras_mas_largas_que_n(lista_palabras, longitud_minima)
print(f"Lista original de palabras: {lista_palabras}")
print(f"Palabras más largas que {longitud_minima}: {palabras_mas_largas}")

'''
15- Define una función que tome un número y calcule su serie de Fibonacci.
'''
def fibonacci(n):
  fib_series = [0, 1]
  if n <= 0:
    return "Ingresa un número entero positivo."
  elif n == 1:
    return [fib_series[0]]
  else:
    for _ in range(2, n):
      next_number = fib_series[-1] + fib_series[-2]
      fib_series.append(next_number)
    return fib_series
numero = int(input("Ingresa un número para calcular su serie de Fibonacci: "))
serie_fibonacci = fibonacci(numero)
print(f"Serie de Fibonacci para el número {numero}: {serie_fibonacci}")

'''
16- Define una función que tome una lista de números y retorne el número más grande de la lista.
'''
def numero_mas_grande(lista_numeros):
  if not lista_numeros:
    return "La lista está vacía, no hay número más grande."
  maximo = lista_numeros[0]
  for numero in lista_numeros:
    if numero > maximo:
      maximo = numero
  return maximo
lista_numeros = [10, 5, 8, 20, 15]
maximo_numero = numero_mas_grande(lista_numeros)
print(f"Lista de números: {lista_numeros}")
print(f"Número más grande: {maximo_numero}")

'''
17- Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
'''
def suma_cubos_digitos(numero):
  suma_cubos = 0
  for digito in str(abs(numero)):
    suma_cubos += int(digito) ** 3
  return suma_cubos
num = int(input("Ingresa un número: "))
resultado = suma_cubos_digitos(num)
print(f"La suma de los cubos de los dígitos de {num} es: {resultado}")

'''
18- Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
'''
def segundo_mas_grande(lista_numeros):
  if len(lista_numeros) < 2:
    return "La lista debe tener al menos dos números."
  maximo = max(lista_numeros)
  lista_sin_maximo = [numero for numero in lista_numeros if numero != maximo]
  segundo_maximo = max(lista_sin_maximo)
  return segundo_maximo
lista_numeros = [10, 5, 8, 20, 15]
segundo_maximo_numero = segundo_mas_grande(lista_numeros)
print(f"Lista de números: {lista_numeros}")
print(f"Segundo número más grande: {segundo_maximo_numero}")

'''
19- Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
'''
def tienen_miembro_comun(lista1, lista2):
  return bool(set(lista1) & set(lista2))
lista_a = [1, 2, 3, 4, 5]
lista_b = [5, 6, 7, 8, 9]
resultado = tienen_miembro_comun(lista_a, lista_b)
print(f"Lista 1: {lista_a}")
print(f"Lista 2: {lista_b}")
print(f"Tienen al menos un miembro en común: {resultado}")

'''
20- Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
'''
def invertir_lista(lista):
  return lista[::-1]
mi_lista = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(mi_lista)
print(f"Lista original: {mi_lista}")
print(f"Lista invertida: {lista_invertida}")

'''
21- Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
'''
def contar_digitos_letras(cadena):
  digitos = 0
  letras = 0
  for caracter in cadena:
    if caracter.isdigit():
      digitos += 1
    elif caracter.isalpha():
      letras += 1
  return digitos, letras
texto = input("Ingresa una cadena de texto: ")
num_digitos, num_letras = contar_digitos_letras(texto)
print(f"Número de dígitos en la cadena: {num_digitos}")
print(f"Número de letras en la cadena: {num_letras}")

'''
22- Define una función que reciba una lista de números y retorne la suma acumulada de los números
'''
def suma_acumulada(lista_numeros):
  suma = 0
  suma_acumulada_lista = []
  for numero in lista_numeros:
    suma += numero
    suma_acumulada_lista.append(suma)
  return suma_acumulada_lista
numeros = [1, 2, 3, 4, 5]
resultado = suma_acumulada(numeros)
print(f"Lista original de números: {numeros}")
print(f"Suma acumulada de los números: {resultado}")

'''
23- Define una función que encuentre el elemento más común en una lista.
'''
def elemento_mas_comun(lista):
  if not lista:
    return "La lista está vacía."
  elemento_mas_frecuente = max(set(lista), key=lista.count)
  frecuencia = lista.count(elemento_mas_frecuente)
  return f"El elemento más común es '{elemento_mas_frecuente}' con {frecuencia} ocurrencias."
mi_lista = [1, 2, 3, 2, 4, 2, 5, 2]
resultado = elemento_mas_comun(mi_lista)
print(f"Lista original: {mi_lista}")
print(resultado)

'''
24- Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
'''
def tabla_de_multiplicar(numero):
  if not isinstance(numero, (int, float)):
    return "Ingresa un número válido."
  tabla = {}
  for i in range(1, 11):
    tabla[i] = numero * i
  return tabla
num = float(input("Ingresa un número para obtener su tabla de multiplicar: "))
resultado_tabla = tabla_de_multiplicar(num)
print(f"Tabla de multiplicar de {num}:")
for clave, valor in resultado_tabla.items():
  print(f"{num} x {clave} = {valor}")

'''
25- Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
'''
def contar_apariciones_caracteres(cadena):
  diccionario_apariciones = {}
  for caracter in cadena:
    if caracter in diccionario_apariciones:
      diccionario_apariciones[caracter] += 1
    else:
      diccionario_apariciones[caracter] = 1
  return diccionario_apariciones
texto = input("Ingresa una cadena de texto: ")
resultado_apariciones = contar_apariciones_caracteres(texto)
print(f"Apariciones de caracteres en la cadena:")
for caracter, cantidad in resultado_apariciones.items():
  print(f"'{caracter}': {cantidad}")

'''
26- Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
'''
def elementos_no_comunes(lista1, lista2):
  return list(set(lista1) ^ set(lista2))
lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]
resultado_no_comunes = elementos_no_comunes(lista_a, lista_b)
print(f"Lista original A: {lista_a}")
print(f"Lista original B: {lista_b}")
print(f"Elementos no comunes: {resultado_no_comunes}")

'''
27- Define una función que tome una lista y retorne la lista sin duplicados.
'''
def eliminar_duplicados(lista):
  return list(set(lista))
mi_lista = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = eliminar_duplicados(mi_lista)
print(f"Lista original: {mi_lista}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")

'''
28- Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
'''
def suma_cuadrados_pares(n):
  if n <= 0 or not isinstance(n, int):
    return "Ingresa un número entero positivo."
  suma = sum(i**2 for i in range(2, n+1, 2))
  return suma
numero = int(input("Ingresa un número entero positivo: "))
resultado = suma_cuadrados_pares(numero)
print(f"La suma de los cuadrados de los números pares hasta {numero} es: {resultado}")

'''
29- Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
'''
def calcular_promedio(lista):
  if not lista:
    return "La lista está vacía, no se puede calcular el promedio."
  suma = sum(lista)
  promedio = suma / len(lista)
  return promedio
lista_numeros = [1, 2, 3, 4, 5]
promedio_resultado = calcular_promedio(lista_numeros)
print(f"Lista de números: {lista_numeros}")
print(f"Promedio de los números: {promedio_resultado}")

'''
30- Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
'''
def cadena_mas_larga(lista_cadenas):
  if not lista_cadenas:
    return "La lista está vacía, no hay cadena más larga."
  cadena_mas_larga = max(lista_cadenas, key=len)
  return cadena_mas_larga
lista_cadenas = ["manzana", "banana", "kiwi", "fresa", "uva"]
resultado = cadena_mas_larga(lista_cadenas)
print(f"Lista de cadenas: {lista_cadenas}")
print(f"Cadena más larga: {resultado}")

'''
31- Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
'''
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def n_primeros_primos(n):
  if n <= 0:
    return "Ingresa un valor válido para n."
  primos = []
  i = 2
  while len(primos) < n:
    if es_primo(i):
      primos.append(i)
    i += 1
  return primos
cantidad_primos = int(input("Ingresa la cantidad de números primos que deseas obtener: "))
resultado_primos = n_primeros_primos(cantidad_primos)
print(f"Los primeros {cantidad_primos} números primos son: {resultado_primos}")

'''
32- Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
'''
def invertir_palabras(cadena):
  palabras = cadena.split()
  palabras_invertidas = palabras[::-1]
  resultado = ' '.join(palabras_invertidas)
  return resultado
texto = input("Ingresa una cadena de texto: ")
texto_invertido = invertir_palabras(texto)
print(f"Texto original: {texto}")
print(f"Texto con palabras invertidas: {texto_invertido}")

'''
33- Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
'''
def ordenar_por_ultimo_elemento(lista_tuplas):
  return sorted(lista_tuplas, key=lambda x: x[-1])
lista_tuplas = [(1, 3, 5), (2, 4, 1), (5, 2, 7), (3, 1, 9)]
resultado_ordenado = ordenar_por_ultimo_elemento(lista_tuplas)
print(f"Lista original de tuplas: {lista_tuplas}")
print(f"Lista ordenada por el último elemento: {resultado_ordenado}")

'''
34- Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
'''
def contar_vocales(cadena):
  vocales = "aeiouAEIOU"
  cantidad_vocales = sum(1 for letra in cadena if letra in vocales)
  return cantidad_vocales
texto = input("Ingresa una cadena de texto: ")
num_vocales = contar_vocales(texto)
print(f"La cantidad de vocales en la cadena es: {num_vocales}")

'''
35- Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
'''
def es_primo(numero):
  if numero < 2:
    return False
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False
  return True
num = int(input("Ingresa un número para verificar si es primo: "))
resultado = es_primo(num)
if resultado:
  print(f"{num} es un número primo.")
else:
  print(f"{num} no es un número primo.")