import array_ordered_positional_list as aop
import linked_ordered_positional_list as lop
import pandas as pd
import class_pelicula as peli
import curses, time, sys


'''
Cosas a destacar:
	Vale a ver, soy Hugo, y basicamente se me metio en la cabeza crear un menu para la practica y hasta aqui llegue.
	Decidi usar la libreria curses y crear una interfaz de terminal, bastante simple, pero utilizable.

	Yo no habia escuchado ni visto nada de curses ni ninguna interfaz hasta hace dos dias, por lo que seguramente el 
	codigo sea algo caotico (en el sentido de la implementacion de curses). 

	El codigo no va documentado ya que funciona igual que el principal (Acabo de conseguir terminar el codigo y son las 16:54 y tengo que arreglar esto un poco no me da tiempo
	y literalmente se basa en el anterior, principalmente lo que cambia es la recogida y salida de datos)

	Dejo unos comentarios de cosas que hacen las funciones mas recursivas de curses a lo largo del codigo. (lo que entendi yo):

	Por cierto, curses es una libreria estandar de python por lo tanto no tienes que instalarla, pero lo que si es que se necesita un subsistema 
	linux para utilizarla (yo uso linux y me deja ejecutarlo pero intentandolo ejecutar en el menu de la terminal de windows no me dejo)

	pantalla.addstr(n:y, m:x, str) -> lo que hace es escribir un mensaje (el str) en unas coordenadas de la pantalla (m:x, n:y)
	imagina que es un print
	

	pantalla.clear() -> es como que limpia la pantalla, la devuelve vacia de cualquier addstr

	pantalla.refresh() -> si 'limpias' la pantalla pero no la actualizas va a seguir mostrando lo mismo

	pantalla.getch() -> Es como que recoge el valor introducido por teclado, el siguiente, cualquiera
	de ahi se puede comparar, que se isa mucho, si es curses.KEY_UP si presionas flecha arriba o 
	si es 10 so presionas enter
	
	curses.initstr() -> inicializa la interfaz

	curses.curs_set(0)  -> oculta el cursor

	pantalla.nodelay(True)  -> configura el getch para que no se bloquee

	pantalla.keypad(True) -> activa el poder pasar valores por teclado

	curses.A_REVERSE -> es lo que hace que se resalte el fondo de la opcion seleccionada

	hay mas como curses.echo pero no los hemos usado

	
	pantalla.addstr('Pulse enter para continuar.')

		while True:
			pantalla.refresh()
			key = pantalla.getch()
			
			if key == 10:
				break

	Una funcion que se me ocurrio, hasta que no pulses enter no contiunua por lo tanto lo llevas
	controlado de cuando quieres seguir, no hay tiempos y solo te aparece por pantalla lo que quieras.
	
	
	pd, se podria usar pantalla.getstr() para recojer el nombre del archivo o que director
	quieres, pero, aparte de que quede mejor como lo implentamos.
	'''








#Menu para la eleccion de director para el apartado 3.2





def menu_director(pantalla, lista):
	
	pantalla.clear()
	opciones = []
	texto = 'Elija un director'

	#creamos una lista con las peliculas de lista
	for pelicula in (lista):
		opciones.append((pelicula.director_name))
	
	
	

	
	#En varios lugares de la practica se ve esto, esto se usa como 'cursor'
	#Por lo que entendi, toda la pantalla son -1, excepto la opcion en la
	#que estamos, que es 0, 0, y por eso conseguimos resalrtar y elegir.
		
	fila_actual = 0
	columna_actual = 0
	
	#
	max_filas = (len(opciones)) // 5  

	while True:

		pantalla.addstr(0, 0, texto)

		for i, año in enumerate(opciones):
			fila = i // 5  # Calcular la fila en función del índice
			columna = i % 5  # Calcular la columna en función del índice
			
			if fila == fila_actual and columna == columna_actual:
				pantalla.addstr(fila + 2, columna * 20, str(año), curses.A_REVERSE)

			else:
				pantalla.addstr(fila + 2, columna * 20, str(año))


		pantalla.refresh()
		key = pantalla.getch()

		# Manejar las teclas de flecha para cambiar la selección

		if key == curses.KEY_UP:
			fila_actual = (fila_actual - 1) % max_filas
		elif key == curses.KEY_DOWN:
			fila_actual = (fila_actual + 1) % max_filas
		elif key == curses.KEY_LEFT:
			columna_actual = (columna_actual - 1) % 5
		elif key == curses.KEY_RIGHT:
			columna_actual = (columna_actual + 1) % 5

		elif key == 10:  
			result = opciones[fila_actual * 5 + columna_actual]
			pantalla.clear()
			pantalla.refresh()
			
			return result








#Lo mismo que antes pero con años, hay que tener en cuenta que año es un int
def menu_años(pantalla, lista):
	
	pantalla.clear()
	opciones = []
	texto = 'Elija un año:'
	
	for posicion, año in enumerate(lista):
		opciones.append(int(año.estreno))
	opciones.sort()

	for i in opciones:
		i = str(i)
	opciones = list(set(opciones))
	
	#Esto es bastante raro de explicar, pero lo probe y funciona.
	#Lo que hago es crear una estructura de datos que es un conjunto, que es set
	#Como es un conjunto, no hay repetidos, por lo que los elimina, y despues
	#lo que hago es colver a convertirlo en lista. 

	
	fila_actual = 0
	columna_actual = 0

	max_filas = (len(opciones)) // 5  


	while True:

		pantalla.addstr(0, 0, texto)


		for i, año in enumerate(opciones):
			fila = i // 5  
			columna = i % 5  
			
			if fila == fila_actual and columna == columna_actual:
				pantalla.addstr(fila + 2, columna * 10, str(año), curses.A_REVERSE)

			else:
				pantalla.addstr(fila + 2, columna * 10, str(año))

		pantalla.refresh()
		key = pantalla.getch()

		if key == curses.KEY_UP:
			fila_actual = (fila_actual - 1) % max_filas
		elif key == curses.KEY_DOWN:
			fila_actual = (fila_actual + 1) % max_filas
		elif key == curses.KEY_LEFT:
			columna_actual = (columna_actual - 1) % 5
		elif key == curses.KEY_RIGHT:
			columna_actual = (columna_actual + 1) % 5

		elif key == 10:  
			result = opciones[fila_actual * 5 + columna_actual]

			pantalla.clear()
			pantalla.refresh()
			return result
		




#Funcion tambien utilizada en la


def menus(pantalla, menu, seleccion=int, lista_rep=list, lista_norep=list, data=pd.DataFrame, data_norep=pd.DataFrame):
	
	pantalla.clear()
	seleccion_menu_0 = 0

	if menu == 1:
		texto = '¿Que quieres hacer?'
		opciones = ['Lista peliculas ordenadas', 'Lista peliculas sin duplicados (puede generar archivo)', 'Visualizacion listados tabulados', 'Metricas', 'Exit']
		bomboclat = {'Lista peliculas ordenadas': 1,'Lista peliculas sin duplicados (puede generar archivo)': 2,'Visualizacion listados tabulados': 3,'Metricas': 4,'Exit': 5}
	elif menu == 2:
		texto = 'Que quieres hacer'
		opciones = ['Ver todos los archivos', 'Filtrar por director', 'Filtrar por año', 'Cancelar']
		bomboclat = {'Ver todos los archivos':1, 'Filtrar por director':2, 'Filtrar por año':3, 'Cancelar':4}
	elif menu == 3:
		texto = '¿Quiere generar un archivo nuevo?'
		opciones = ['Si', 'No']
		bomboclat = {'Si':1, 'No':2}
	elif menu == 4:
		texto = '¿Quiere usar repetidos o no?'
		opciones = ['Repetidos', 'Sin repetidos']
		bomboclat = {'Repetidos':1, 'Sin repetidos':2}
	elif menu == 5:
		texto = '¿Quiere representar un dataframe o lista tabulada?'
		opciones = ['Usar DataFrame', 'Usar tabulacion']
		bomboclat = {'Usar DataFrame':1, 'Usar tabulacion':2}
	
	elif menu == 6:
		sys.exit()

	
	while True:

		pantalla.addstr(0, 0, texto)  
		for i, opcion in enumerate(opciones):

			if i == seleccion_menu_0:
				pantalla.addstr(i+1, 0, opcion, curses.A_REVERSE)

			else:
				pantalla.addstr(i+1, 0, opcion)
		
		pantalla.refresh()
		key = pantalla.getch()

		# Manejar las teclas de flecha para cambiar la selección del segundo menú
		if key == curses.KEY_UP:
			seleccion_menu_0 = (seleccion_menu_0 - 1) % len(opciones)

		elif key == curses.KEY_DOWN:
			seleccion_menu_0 = (seleccion_menu_0 + 1) % len(opciones)

		elif key == 10:  
			saras = opciones[seleccion_menu_0]
			result = bomboclat[saras]
			

			break

	return result


#Funcion mas extensa por la cantidad de addstr
def accion(pantalla, accion, lista_rep=list, lista_norep=list, data=pd.DataFrame, data_norep=pd.DataFrame):

	if accion == 5:
		sys.exit()



	elif accion == 1:

		pantalla.clear()
		pantalla.addstr(0, 0, 'Lista de todas las peliculas:')
		
		#Se usan bastantes list comprehension
		for i, pelis in enumerate(lista_rep): 
			pantalla.addstr(i+1, 0, f'Director: {pelis.director_name}, Pelicula: {pelis.film_name} Estreno: {pelis.estreno}, Puntuation: {pelis.puntuation}')

			if i == len(lista_rep)-1:
				pantalla.addstr(i+2, 0, 'Pulse enter para continuar.')

		pantalla.addstr('Pulse enter para continuar.')

		while True:
			pantalla.refresh()
			key = pantalla.getch()
			
			if key == 10:
				break




	if accion == 2:

		pantalla.clear()
		pantalla.refresh()

		pantalla.addstr(0, 0, 'Lista de todas las peliculas sin repetidos:')

		for i, pelis in enumerate(lista_norep): 
			pantalla.addstr(i+1, 0, f'Director: {pelis.director_name}, Pelicula: {pelis.film_name} Estreno: {pelis.estreno}, Puntuation: {pelis.puntuation}')
			ultimo = i
		
		pantalla.addstr(i+2, 0, 'Pulse enter para continuar.')
		pantalla.refresh()

		while True:
			pantalla.refresh()
			key = pantalla.getch()

			if key == 10:
				break

		pantalla.refresh()
		guardar = menus(pantalla, 3)
		

		if guardar == 1:

			nombre_archivo = 'Peliculas_sin_repetir.txt'

			with open(f'{nombre_archivo}', 'w', encoding='utf-8') as archivo:

				for pelii in lista_norep:
					archivo.write(f'{pelii.director_name}; {pelii.film_name}; {pelii.estreno}; {pelii.puntuation}\n')

			pantalla.clear()
			pantalla.addstr(0, 0, 'Lista guardada')
			pantalla.addstr(1, 0, 'Presione enter para continuar')
			pantalla.refresh()

			while True:
				pantalla.refresh()
				key = pantalla.getch()
				
				if key == 10:
					break






	if accion == 3:

		siguiente = menus(pantalla, 2)
		
		if siguiente in (1, 2, 3):

			rep = menus(pantalla, 4)
			pri = menus(pantalla, 5)


			if rep == 1:
					conclusion = lista_rep
					conclusion_data = data
					tx = 'con'
			else:
					conclusion = lista_norep
					conclusion_data = data_norep
					tx = 'sin'



			if siguiente == 1:
				if pri == 1:
					pantalla.clear()

					pantalla.addstr(0, 0, f'Todas las peliculas tabuladas y ordenadas en formato DataFrame {tx} repetidos')
					pantalla.addstr(1, 0, conclusion_data.to_string())

					long = (len(conclusion_data))
					pantalla.addstr(long+6, 0, 'Pulse enter para continuar')

					pantalla.refresh()

					while True:
						pantalla.refresh()
						key = pantalla.getch()

						if key == 10:
							pantalla.clear()
							break


				else:
					pantalla.clear()
					pantalla.addstr(0, 0, f'Todas las peliculas tabuladas y ordenadas en formato lista tabulada {tx} repetidos')

					new_aux_list = ['Título', 'Director', 'Año','Puntuación']
					cadena_sup = ''

					for i in new_aux_list:
						columna =  f"{i: ^37}"
						cadena_sup = cadena_sup + f'\t{columna}'
					
					pantalla.addstr(2, 0, cadena_sup)


					separador = '-'*37
					lineas = f'\t{separador}'*4

					pantalla.addstr(3, 0, lineas)
					
					for lo, i in enumerate(conclusion):
						film_name = f"{i.film_name: ^37}" 
						director_name = f"{i.director_name: ^37}" 
						estreno =  f"{i.estreno: ^37}" 
						puntuation = f"{i.puntuation: ^37}"
						pantalla.addstr(lo+4, 0, f"\t{film_name}\t{director_name}\t{estreno}\t{puntuation}")

					separador = '-'*37
					lineas = f'\t{separador}'*4
					pantalla.addstr(int(lo+6), 0, lineas)
					pantalla.refresh()

					while True:
						pantalla.refresh()
						key = pantalla.getch()

						if key == 10:
							pantalla.clear()
							break








			elif siguiente == 2:
				
					
					
				if pri == 1:
					pantalla.clear()

					#------------------------------
					director = menu_director(pantalla, conclusion)
					#------------------------------


					data_director = conclusion_data[conclusion_data['Director'] == director]
					pantalla.addstr(0, 0, f'Todas las peliculas de {director} tabuladas y ordenadas en formato DataFrame {tx} repetidos')

					pantalla.addstr(2, 0, data_director.to_string())
					pantalla.refresh

					while True:
						pantalla.refresh()
						key = pantalla.getch()

						if key == 10:
							pantalla.clear()
							break


				else:
					

					director = menu_director(pantalla, conclusion)
					pantalla.clear()
					pantalla.addstr(0, 0, f'Todas las peliculas de {director} tabuladas y ordenadas en formato lista tabulada {tx} repetidos')

					new_aux_list = ['Título', 'Director', 'Año','Puntuación']
					cadena_sup = ''

					for i in new_aux_list:
						columna =  f"{i: ^37}"
						cadena_sup = cadena_sup + f'\t{columna}'

					
					pantalla.addstr(2, 0, cadena_sup)

					separador = '-'*37
					lineas = f'\t{separador}'*4

					pantalla.addstr(3, 0, lineas)

					aux = []
					for y in conclusion:
						if director == y.director_name:
							aux.append(y)

					for lo, i in enumerate(aux):
						
						film_name = f"{i.film_name: ^37}" 
						director_name = f"{i.director_name: ^37}" 
						estreno =  f"{i.estreno: ^37}" 
						puntuation = f"{i.puntuation: ^37}"
						pantalla.addstr(lo+4, 0, f"\t{film_name}\t{director_name}\t{estreno}\t{puntuation}")

					separador = '-'*37
					lineas = f'\t{separador}'*4
					pantalla.addstr(int(lo+6), 0, lineas)
					pantalla.refresh()

					while True:
						pantalla.refresh()
						key = pantalla.getch()

						if key == 10:
							pantalla.clear()
							break




				






			elif siguiente == 3:


				if pri == 1:


					pantalla.clear()

					#------------------------------
					año = menu_años(pantalla, conclusion)
					#------------------------------
					pantalla.addstr(0, 0, f'Todas las peliculas de {año} tabuladas y ordenadas en formato DataFrame {tx} repetidos')

					data_año = conclusion_data[conclusion_data['Año'] == int(año)]
					pantalla.addstr(2, 0, data_año.to_string())
					pantalla.refresh

					while True:
						pantalla.refresh()
						key = pantalla.getch()

						if key == 10:
							pantalla.clear()
							break



				else:
					

					año = menu_años(pantalla, conclusion)

					pantalla.clear()
					pantalla.addstr(0, 0, f'Todas las peliculas de {año} tabuladas y ordenadas en formato lista tabulada {tx} repetidos')

					new_aux_list = ['Título', 'Director', 'Año','Puntuación']
					cadena_sup = ''

					for i in new_aux_list:
						columna =  f"{i: ^37}"
						cadena_sup = cadena_sup + f'\t{columna}'

					
					pantalla.addstr(2, 0, cadena_sup)

					separador = '-'*37
					lineas = f'\t{separador}'*4

					pantalla.addstr(3, 0, lineas)

					aux = []
					for y in conclusion:
						if año == y.estreno:
							aux.append(y)

					for lo, i in enumerate(aux):
						
						film_name = f"{i.film_name: ^37}" 
						director_name = f"{i.director_name: ^37}" 
						estreno =  f"{i.estreno: ^37}" 
						puntuation = f"{i.puntuation: ^37}"
						pantalla.addstr(lo+4, 0, f"\t{film_name}\t{director_name}\t{estreno}\t{puntuation}")

					separador = '-'*37
					lineas = f'\t{separador}'*4
					pantalla.addstr(int(lo+6), 0, lineas)
					pantalla.refresh()

					while True:
						pantalla.refresh()
						key = pantalla.getch()

						if key == 10:
							pantalla.clear()
							break






	






	if accion == 4:

		rep = menus(pantalla, 4)

		if rep == 1:
					conclusion = lista_rep
					conclusion_data = data
					tx = 'con'
		else:
					conclusion = lista_norep
					conclusion_data = data_norep
					tx = 'sin'

	#--------------------------------------------------------------

		pantalla.clear()
		
		pantalla.addstr(0, 0, f'Peliculas creadas por director {tx} repetidos: ')
		
		group_col = 'Director'
		num_peliculas_por_director = conclusion_data.groupby(group_col).size()
		pantalla.addstr(2, 0, num_peliculas_por_director.to_string())
		long = len(num_peliculas_por_director)
		
    
		pantalla.refresh()

		pantalla.addstr(long+4, 0, 'Pulse enter para continuar')

		while True:
				pantalla.refresh()
				key = pantalla.getch()
			
				if key == 10:
					pantalla.clear()
					break
		
#-----------------------------------------------------------------

		pantalla.addstr(0, 0, f'Peliculas creadas por director {tx} repetidos: ')
		
		group_col = 'Director'
		target_col = 'Puntuacion'
		puntuation_per_director = conclusion_data.groupby(group_col).agg({target_col :["mean"]})
		pantalla.addstr(2, 0, puntuation_per_director.to_string())
		long = len(puntuation_per_director)
		
    
		pantalla.refresh()

		pantalla.addstr(long+6, 0, 'Pulse enter para continuar')

		while True:
				pantalla.refresh()
				key = pantalla.getch()
			
				if key == 10:
					pantalla.clear()
					break
		pantalla.clear()

			#----------------------------------------------------------

		pantalla.addstr(0, 0, f'Puntuacion media por director {tx} repetidos: ')
		
		group_col = 'Año'
		target_col = 'Puntuacion'
		puntuation_per_year = conclusion_data.groupby(group_col).agg({target_col :["mean"]})
		pantalla.addstr(2, 0, puntuation_per_year.to_string())
		long = len(puntuation_per_year)
		
    
		pantalla.refresh()

		pantalla.addstr(long+6, 0, 'Pulse enter para continuar')

		while True:
				pantalla.refresh()
				key = pantalla.getch()
			
				if key == 10:
					pantalla.clear()
					break
		

	#----------------------------------------------------

		





def main():
	#Creamos la variable archivo y la rellenamos con el txt que le pasamos
	
	archivo = sys.argv[1]

	#Definimos pantalla inicializando la interfaz
	pantalla = curses.initscr()

	

	




	def imprimir_menu(opciones_menu, seleccion_menu, texto):

		pantalla.addstr(0, 0, texto)  

		for i, opcion in enumerate(opciones_menu):

			if i == seleccion_menu:
				pantalla.addstr(i+1, 0, opcion, curses.A_REVERSE)
			else:
				pantalla.addstr(i+1, 0, opcion)


	curses.curs_set(0)  
	pantalla.nodelay(True)  
	pantalla.keypad(True) 
	curses.noecho()

	opciones_menu_0 = ["(1)Array_ordered_positional_list", '(2)Linked_ordered_positional_list']
	seleccion_menu_0 = 0
	texto_menu_0 = 'Tipo de lista a usar: '

	
	while True:
		pantalla.addstr(0, 0, texto_menu_0)  
		imprimir_menu(opciones_menu_0, seleccion_menu_0, texto_menu_0)
		pantalla.refresh()
		key = pantalla.getch()

		if key == curses.KEY_UP:
			seleccion_menu_0 = (seleccion_menu_0 - 1) % len(opciones_menu_0)
		elif key == curses.KEY_DOWN:
			seleccion_menu_0 = (seleccion_menu_0 + 1) % len(opciones_menu_0)
		
		elif key == 10:  
			tipo_lista = opciones_menu_0[seleccion_menu_0]
			pantalla.clear()
			
			break  
				
		






	#Elegimos con que tipo de listas queremos hacer la practica
	if tipo_lista == "(1)Array_ordered_positional_list":
		lista_peliculas       = aop.ArrayOrderedPositionalList()
		lista_peliculas_norep = aop.ArrayOrderedPositionalList()
		lista_peliculas_copy  = aop.ArrayOrderedPositionalList()  
		

	else:
		lista_peliculas       = lop.LinkedOrderedPositionalList()
		lista_peliculas_norep = lop.LinkedOrderedPositionalList()
		lista_peliculas_copy  = lop.LinkedOrderedPositionalList()
		
	#Hacemos esto ya que en el pdf especfica que se pueden usar ambas implementaciones.
	#Al poder definir que lista creas, se ve que uses la que uses, al usar metodos comunes
	#Puedes usar un tipo o otro indiferentemente



	#Guardamos el contenido del archivo
	with open(archivo, 'r', encoding='utf-8') as contenido:
		info_procesos = contenido.read()

	#Rellenamos las listas

	for line in info_procesos.split('\n'):   

		if len(line) != 0 and len(line.split(';')) == 4:

			datos_pelicula = line.split(';')
			director_name, film_name, estreno, puntuation = datos_pelicula 

			pelicula = peli.Pelicula(director_name, film_name, estreno, puntuation)
			
			lista_peliculas.add(pelicula)
			lista_peliculas_copy.add(pelicula)
	

	#Rellenamos lista_peliculas_norep

	
	while True:
		
		primero   = lista_peliculas_copy.get_element(lista_peliculas_copy.first())
		siguiente = lista_peliculas_copy.get_element(lista_peliculas_copy.after(lista_peliculas_copy.first()))
		ultima    = lista_peliculas_copy.get_element(lista_peliculas_copy.last())

		if (primero.director_name == siguiente.director_name) and (primero.film_name == siguiente.film_name):
				
				lista_peliculas_copy.delete(lista_peliculas_copy.first())

		else:
			

			if siguiente == ultima:

				lista_peliculas_norep.add(lista_peliculas_copy.delete(lista_peliculas_copy.first()))
				lista_peliculas_norep.add(lista_peliculas_copy.delete(lista_peliculas_copy.last()))
				break

			lista_peliculas_norep.add(lista_peliculas_copy.delete(lista_peliculas_copy.first()))

	#Creamos los dataframes con peliculas repetidas y no repetidas
	aux_data_repeat = []
	aux_data_no_repeat = []

	for u in lista_peliculas:
		aux_data_repeat.append(u.data_values())

	for u in lista_peliculas_norep:
		aux_data_no_repeat.append(u.data_values())

	data_repeat = pd.DataFrame(aux_data_repeat, columns = ['Titulo', 'Director', 'Año', 'Puntuacion'])

	data_no_repeat = pd.DataFrame(aux_data_no_repeat, columns = ['Titulo', 'Director', 'Año', 'Puntuacion'])





	while True:
		siguiente = menus(pantalla, 1, lista_rep=lista_peliculas, lista_norep=lista_peliculas_norep, data=data_repeat, data_norep=data_no_repeat )

		pantalla.clear()
		pantalla.refresh()
		pantalla.clear()
		pantalla.refresh()
		
		

		if siguiente == 5:
			accion(pantalla, 5)

		elif siguiente == 1:
			
			accion(pantalla, 1, lista_peliculas, lista_peliculas_norep, data_repeat, data_no_repeat)

		elif siguiente == 2:
			accion(pantalla, 2, lista_peliculas, lista_peliculas_norep, data_repeat, data_no_repeat)
		
		elif siguiente == 3:
			accion(pantalla, 3, lista_peliculas, lista_peliculas_norep, data_repeat, data_no_repeat)
		
		elif siguiente == 4:
			accion(pantalla, 4, lista_peliculas, lista_peliculas_norep, data_repeat, data_no_repeat)
		
		




if __name__ == "__main__":
	main()




