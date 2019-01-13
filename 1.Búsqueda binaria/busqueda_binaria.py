#función de búsqueda binaria
def busqueda_binaria(array, target_value):

	#variables de "index" mínimo y máximo, máximo siendo la cantidad de valores de la lista -1 porque los "index" empiezan desde 0
	mini = 0
	maxi = int(len(array)) - 1

	#variables para saber si el numero fue encontrado o no y el número de intentos
	found = False
	tries = 1

	#ciclo donde ocurre la búsqueda, mientras no haya sido encontrado el número, seguira
	while mini <= maxi and not found :

		#se toma el promedio para el intento y se redondea hacia abajo
		guess = (mini + maxi) // 2

		#si se encuentra el valor "found" se vuelve verdadero y se acaba el ciclo
		if array[guess] == target_value :
			found = True

			#sino, se reduce o amuenta el máximo/mínimo respectivamente, se cuenta un intento y se repite el ciclo
		else:
			if target_value < array[guess] :
				maxi = guess - 1
				tries += 1
			else:
				mini = guess + 1
				tries += 1

				#se regresa si fue encontrado el número, el "index" de donde está y el número de intentos
	return found, guess, tries

#lista de números
primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#preguntamos por el número buscado
print( "Insert the number you are searching:" ) 

#se le asigna como entero al "target"
target_value = int(input())

#se realiza la función de la búsqueda binaria
busqueda_binaria(primes, target_value)

#Se imprimen los resultados
print("The target was found: found/index/#of attempts",busqueda_binaria(primes, target_value))