#Hugo Varela Sanchez; hugo.varela.sanchez@udc.es
#David Fernandez Reimundez; david.fernandez.reimundez@udc.es

#Hay que filtrar el apartado 2-3 por listas en vez del dataframe
#En una clase un profesor dice que el apartado 3 no se puede hacer de x manera y manda un correo y en otra dice  que si que vale, y en una dicen que el apartado 4 es de una y en otra que es de otra, lo hacemos con tantas opciones para que digan lo que digan este la opcion

#Importamos la libreris sys, y los archivos para implementar el TAD Lista Posicional Ordenada
import sys
import array_ordered_positional_list as aop
import linked_ordered_positional_list as lop
import pandas as pd
import class_pelicula as peli


#---------------------------------------------------------------------------------------------------------------

def menus(menu,  eleccion = int):
    
    '''
    Funcion de ayuda muy extensa. 
    Esta funcion lo que hace gestionar los 'menus' de la practica:

        El menu == 0 

            Es el primero que aparece, y aparece siempre. 
            Elige si quieres usar una lop o una aop

        El menu == 1 Menu: Principal

            Es el menu principal.
            Te da a cual de los 4 puntos principales de la practica quieres usar, aun asi, tiene
            5 opciones, ya que se le añade la opcion de cerrar el programa

        El menu == 2 Menu: Submenu

            Submenu para elegir cual de las 3 opciones del apartado 3 quieres realizar.
            Aun asi metimos la opcion de volver a atras. 
            Todas estas opciones llevan a distintos submenus para elegir si
            se quiere repetidos y la forma de impresion, salvo que el 3.2, y 3.3
            piden un input() para recojer por que lo quieres filtrar

        El menu == 3 Menu: Guardar

            Te la la opcion de si quires guardar en un archivo generado en el menu 1.2
            Antes de este menu te imprime la nueva lista sin repetidos y luego se te plantea la idea de guardarlo
            Si lo guarda te pide un input donde tienes que poner el nombre del fichero
            Si no lo quieres guardar te retorna al menu principal
        
        El menu == 4 Menu: Repetidos 
        
            Te deja elegir si quieres imprimir la tabla con o sin repetidos. 
        
        El menu == 5 Menu: Impresion

            A la hora de hacer la practica, vimos que como la impresion era con tabulados, se
            podria hacer con pandas. Sin embargo, nos llego un correo del decano en donde
            se entendia que no se podia hacer. Por tanto, para no perder la opcion de imprimir el DataFrame y dar variedad, 
            decidimos dejarlo, pero implementar una opcion de imprimir a base de tabulaciones, que 
            a nuestro gusto, quedo muy bien.
            Tambien filtra de distintas maneras en cada uno, ya que se 'corresponde' mas al tipo de impresion, y 
            asi se muestra que se entiende que se sabe hacer de ambas maneras.

        El menu == 6 Exit
            No es un menu, simplemente sale del programa

    ---------
    Parameters
    ----------

    menu: int
        Menu al que pretendes acceder.

    eleccion: int
        No es obligatorio ponerlo, pero se usa para cuando se enrta en el menu 3. 
        Si entras al menu 3 te permite acceder a que opcion quieres
   

        
    -------
    Returns
    -------
    opcion: int
    tipo_lista : int.
    quehacer : int
    eleccion : int
    
    Devuelven numeros de entre 1-5, 1-4, 1-2

    Devuelve una unica variable, llamemos variable x, solo que hay varios nombres porque en las primeras
    etapas del menu habia nombres distintos, y se acabaron manteniendo con el tiempo.
    Eso es debido a que el menu antiguo era funcional pero muy lioso, y decidimos reescribirlo para optimizarlo.
    '''

    #Si menu es alguno de esos numeros (0, 3, 4, 5), como en todos solo puedes elegir entre 1 y 2, ya te da el texto 
    #que va a imprimir y se encarga de gestionar conjunto de que no puedas poner nada que no sea una opcion.
    if menu in (0, 3, 4, 5):
        

        
        if menu == 0:
            salida = 'Tipo de lista a usar: \n  (1)Array_ordered_positional_list\n  (2)Linked_ordered_positional_list\n\n  Eleccion: '

        elif menu == 5:
            salida = '\nForma de visualizar listas: \n  (1)DataFrame\n  (2)Tabulacion\n\n  Eleccion: '

        elif menu == 4:
            salida = '\nQuieres usar repetidos, ¿si o no?: \n  (1)SI usar repetidos\n  (2)NO usar repetidos\n\n  Eleccion: '
        
        elif menu == 3:
            salida = '\n¿Quieres guardar la nueva lista?: \n    (1)SI\n    (2)NO\n\n\tEleccion: '


        #Compara si es un int y si esta entre las opciones, si no te da un error y te pide que pongas de nuevo la opcion y devuelve el la opcion
        while True:

            try:
                eleccion = int(input(salida))
                
                if (eleccion<1 or eleccion>2):
                    raise peli.NumberNotInMenu
                break

            except ValueError:
                print('\nDebes introducir un número\n')

            except peli.NumberNotInMenu:
                print('\nDebe de ser un número del 1 al 2\n')


        
        # if eleccion == 1:
        #     opcion  = 1

        # else:
        #     opcion = 0
        #return opcion.

        return eleccion
    

    #Si es igual a 6, llama a la libreria sys, en concreto al metodo sys.exit() que se encarga de cerrar el programa
    elif menu == 6:
        sys.exit()
        
    #Si el menu es igual a 1, compara si es un int y si esta entre las opciones, si no te da un error y te pide que pongas de nuevo la opcion, y devuelve la opcion
    elif menu ==1:
        while True:

            try:
                quehacer = int(input('\n---x---\n\nQue quieres ver:\n(1)Lista de peliculas ordenadas\n(2)Lista de películas ordenadas sin duplicados (devuelve un archivo txt con las peliculas)\n(3)Ver algunos listados tabulados\n(4)Mostrar métricas\n(5)Cerrar programa\n\nEleccion: '))
                if quehacer == 5:
                    sys.exit()
                
                
                if (quehacer<1 or quehacer>4):
                    raise peli.NumberNotInMenu
                break
                

            except ValueError:
                print('\nDebes introducir un número\n')

            except peli.NumberNotInMenu:
                print('\nDebe de ser un número del 1 al 4\n')


        return quehacer



    #Si el menu es igual a 2, compara si es un int y si esta entre las opciones, si no te da un error y te pide que pongas de nuevo la opcion, y devuelve la opcion
    elif menu == 2:

        while True:

            try:
                eleccion = int(input('Que quieres hacer: \n    (1)Ver todas las peliculas\n    (2)Peliculas rodadas por un director\n    (3)Peliculas estrenadas en un año \n    (4)Cancelar\n\n\tEleccion: '))
                
                if (eleccion<1 or eleccion>4):
                    raise peli.NumberNotInMenu
                break

            except ValueError:
                print('\nDebes introducir un número\n')

            except peli.NumberNotInMenu:
                print('\nDebe de ser un número del 1 al 4\n')

        return eleccion
     
   



def accion(accion, lista_rep=list, lista_norep=list, data=pd.DataFrame, data_norep=pd.DataFrame):

    '''
    Funcion que gestiona las acciones que se toman despues de la eleccion en los menus
    Esta muy ligada con la funcion menus

    La accion == 5 Accion: Finalizar
        Termina de ejecutar el programa, lo cierra

    La accion == 1 Accion: Peliculas_dupe
        Imprime todas las peliculas ordenadas por director

    La accion == 2 Accion: Peliculas_no_dupe
        Imprime todas las peliculas ordenadas por director sin repetir.
        Tambien hace una llamada a menus(3) para preguntar si se guarda.
        En caso afirmativo guarda la lista en un fichero

    La accion == 3 Accion: Submenu
        Hace una llamada a menus(2) y elige que tiene  que hacer. De ahi, 
        Depues sigue linealmente hasta imprimir lo que debe. (explicacion a detalle traves de comentarios)
    
    La accion == 4 Accion: Metricas
        Hace llamada a menus(4)
        De ahi eligue que lista y dataframe usar y imprime las estadisticas con pandas.


    ---------
    Parameters
    ----------
    accion: int
        Es la opcion elegida en el menu
    
    -- No es obligartorio poner los siguientes parametros --

    lista_rep: list
        Lista posicional ordenada (TAD) con las peliculas incluyendo las repetidas
    
    lista_norep: list
        Lista posicional ordenada (TAD) con las peliculas sin incluir repetidos
    
    data: pandas.DataFrame
        Dataframe creado a partir de la lista con repetidos
    
    data_norep: pandas.DataFrame
        DataFrame creado a partir de la lista sin repetidos
   
    -------
    Returns
    -------
    prints -> print()
    '''


    #Si accion es 5, cierra el programa
    if accion == 5:
        sys.exit()


    #Si eleccion es 1, imprime un mensaje de lo que va a imprimir, y con un bucle for, cada iteracion imprime una peli distinta
    elif accion == 1:
        print('\nLista de todas las peliculas:\n')
        
        for pelis in lista_rep: 
            print(f'Director: {pelis.director_name}, Pelicula: {pelis.film_name} Estreno: {pelis.estreno}, Puntuation: {pelis.puntuation}')





    #Si eleccion es 2, imprime un mensaje de lo que va a imprimir, y con un bucle for, cada iteracion imprime una peli distinta
    if accion == 2:

        
        print(f'\nLista de todas las peliculas sin repetidos:\n')

        for pelis in lista_norep: 
            print(f'Director: {pelis.director_name}, Pelicula: {pelis.film_name} Estreno: {pelis.estreno}, Puntuation: {pelis.puntuation}')

        #LLama a Menus:Guardar y si devuelve un 1, hace un input pidiendo un nombre para el archivo, y guardandolo.
        guardar = menus(3)

        if guardar == 1:
            nombre_archivo = input('\nDame el nombre que le quieres poner al archivo: ')
        
            with open(f'{nombre_archivo}', 'w', encoding='utf-8') as archivo:
                for pelii in lista_norep:
                    archivo.write(f'{pelii.director_name}; {pelii.film_name}; {pelii.estreno}; {pelii.puntuation}\n')


    #Si accion es 3, llama a menus(2) menu:Submenu, si el numero que devuelve es dieferente a 4 (cancelar), llama 
    # a menus(4) y menus(5) para recojer si se quieren usar repetidos o no

    if accion == 3:

        siguiente = menus(2)
        
        if siguiente in (1, 2, 3):
            rep = menus(4)
            pri = menus(5)


            #Si es 1, es que se quieren usar repetidos. si es 2, es no repetidos, por tanto guarda la lista y el dataframe en dos variables conclusion con las que 
            #se vayan a usar
            if rep == 1:
                    conclusion = lista_rep
                    conclusion_data = data
                    tx = 'con'
            else:
                    conclusion = lista_norep
                    conclusion_data = data_norep
                    tx = 'sin'


            #Depende de lo que de Menu(2) (Menu:Submenu). entra en siguiente 1, 2, 3

            if siguiente == 1:

                #Si pri es 1, es que se quiere imprimir como DataFrame, por tanto imprime un menasje de lo que va a imprimir y imprime conclusion_data
                if pri == 1:
                    
                    print(f'\nTodas las peliculas tabuladas y ordenadas en formato DataFrame {tx} repetidos')
                    print(f'\n{conclusion_data}')

                # Si no imprime  con TAD
                else:

                    #Crea una nueva variable con los nombres de cada columna y con un bucle y strings (lo aprendimos en el primer cuatrimestre), imprime de forma ordenada.

                    new_aux_list = ['Título', 'Director', 'Año','Puntuación']
                    cadena_sup = ''
                    for i in new_aux_list:
                        columna =  f"{i: ^37}"
                        cadena_sup = cadena_sup + f'\t{columna}'

                    
                    #Imprime colocados los nomrbes de las columnas
                    print('\n',cadena_sup)

                    #Crea un str que se llama separados que no es mas que una cadena de ---- y lo imprime
                    separador = '-'*37
                    lineas = f'\t{separador}'*4
                    print(lineas)
                    
                    #Para conclusion, va ordenando como hizo con cadena superior pero para cada atributo de pelicula y lo imprime en su posicion
                    for i in conclusion:
                        film_name = f"{i.film_name: ^37}" 
                        director_name = f"{i.director_name: ^37}" 
                        estreno =  f"{i.estreno: ^37}" 
                        puntuation = f"{i.puntuation: ^37}"
                        print(f"\t{film_name}\t{director_name}\t{estreno}\t{puntuation}")

                    #Vuelve a imprimir un separador
                    print(lineas)








            elif siguiente == 2:
                
                #Si pri es 1 (dataframe) pide introducir nombre de director, y si no es un director que este en el el dataframe vuelve a pedir. Despues 
                #Filtra y imprime

            
                if pri == 1:
                    director = input('\nDeme un nombre del director: ')

                    while (director not in data['Director'].values):

                        print('\nNo hay peliculas de este director.Si no es asi, asegurese de escribir el nombre como en la tabla')
                        director = input('\nDeme un nombre del director: ')
                
                    data_director = conclusion_data[conclusion_data['Director'] == director]
                    print(f'\nPeliculas de {director}:\n\n', data_director)


                else:
                    #Creamos una variable auxiliar
                    aux2 = []

                    #Guardamos todos los nombres de directores
                    for i in conclusion:
                        aux2.append(i.director_name)

                    while True:
                        #Si el nombre no esta en la nueva lista, vuelve a pedir y suelta un mensaje de error
                        try:
                            director = input('\nDeme un nombre del director: ')
                            
                            if (director not in aux2):
                                raise peli.NumberNotInMenu
                            break

                        except ValueError:
                            print('\nDebes introducir un nombre de director\n')

                        except peli.NumberNotInMenu:
                            print('\nNo se encuentra ninguna peli con ese director, busque otro\n')
                    

                    #Imprime un mensaje de lo que se va a imprimir
                    print(f'Todas las peliculas de {director} tabuladas y ordenadas en formato lista tabulada {tx} repetidos')

                    new_aux_list = ['Título', 'Director', 'Año','Puntuación']
                    cadena_sup = ''
                    for i in new_aux_list:
                        columna =  f"{i: ^37}"
                        cadena_sup = cadena_sup + f'\t{columna}'

                    #Volver a linea 320

                    print('\n',cadena_sup)

                    separador = '-'*37
                    lineas = f'\t{separador}'*4
                    print(lineas)
                    
                    aux = []
                    for y in conclusion:
                        if director == y.director_name:
                            aux.append(y)

                    for i in aux:
                        
                        film_name = f"{i.film_name: ^37}" 
                        director_name = f"{i.director_name: ^37}" 
                        estreno =  f"{i.estreno: ^37}" 
                        puntuation = f"{i.puntuation: ^37}"
                        print(f"\t{film_name}\t{director_name}\t{estreno}\t{puntuation}")

                    separador = '-'*37
                    lineas = f'\t{separador}'*4
                    print(lineas)


				






            elif siguiente == 3:

                aux2 = []

                    #Guardamos todos los nombres de directores
                for i in conclusion:
                    aux2.append(int(i.estreno))

                
                while True:
                        #Si el año no esta en la nueva lista, vuelve a pedir y suelta un mensaje de error
                        try:
                            año = int(input('\nDeme un año: '))
                            
                            if (año not in aux2):
                                raise peli.NumberNotInMenu
                            break

                        except ValueError:
                            print('\nDebes introducir un año\n')

                        except peli.NumberNotInMenu:
                            print('\nNo se encuentra ninguna peli con ese año, busque otro\n')


                


                if pri == 1:

                    #Filtra las filas donde la columna Año sea igual al año

                    data_año = conclusion_data[conclusion_data['Año'] == año]
                    print(f'\nPeliculas de {año}:\n\n', data_año)


                else:

                    #Crea una lista auxiliar, y recorre conclusion guardando las peliculas donde y.estreno sea igual a año
                    aux = []

                    for y in conclusion:
                        if año == y.estreno:
                            aux.append(y)

                    #Volver a linea 320

                    new_aux_list = ['Título', 'Director', 'Año','Puntuación']
                    cadena_sup = ''

                    for i in new_aux_list:
                        columna =  f"{i: ^37}"
                        cadena_sup = cadena_sup + f'\t{columna}'

                    print('\n',cadena_sup)

                    separador = '-'*37
                    lineas = f'\t{separador}'*4
                    print(lineas)
                    
                   

                    for i in aux:
                        
                        film_name = f"{i.film_name: ^37}" 
                        director_name = f"{i.director_name: ^37}" 
                        estreno =  f"{i.estreno: ^37}" 
                        puntuation = f"{i.puntuation: ^37}"
                        print(f"\t{film_name}\t{director_name}\t{estreno}\t{puntuation}")

                    separador = '-'*37
                    lineas = f'\t{separador}'*4
                    print(lineas)






	





    #Si la accion es 4 Accion:Metricas 
    if accion == 4:
        
        #Llama a menus(4) y asi decides si quieres usar o no repetidos y creas conclusion.
        rep = menus(4)

        if rep == 1:
                    conclusion = lista_rep
                    conclusion_data = data
        
        else:
                    conclusion = lista_norep
                    conclusion_data = data_norep

    #--------------------------------------------------------------

        #1, Imprime el dataframe que muestra el numero de peliculas por director
        print('\nPeliculas creadas por director: \n')
        group_col = 'Director'
        num_peliculas_por_director = conclusion_data.groupby(group_col).size()
        print(num_peliculas_por_director, '\n')

        #2, Imprime el dataframe que muestra la nota media por director
        print('\nPuntuacion media por director: \n')
        group_col = 'Director'
        target_col = 'Puntuacion'
        puntuation_per_director = conclusion_data.groupby(group_col).agg({target_col :["mean"]})
        print(puntuation_per_director, '\n')

        #3, Imprime el dataframe que muestra la nota media por año
        print('\nPuntuacion media por año: \n')
        group_col = 'Año'
        target_col = 'Puntuacion'
        puntuation_per_year = conclusion_data.groupby(group_col).agg({target_col :["mean"]})
        print(puntuation_per_year, '\n')



            
#-----------------------------------------------------------------------------------------------------------------------------------



def main():
    '''
    Funcion de ejecucion. Al llamarla se ejecuta todo el programa

    ---------
    Parameters
    ----------
    None

    -------
    Returns
    -------
    
    '''

    #Guardamos archivo como el archivo que se le pasa junto al main al llamarlo por la terminal

    archivo = sys.argv[1]
    #archivo = 'peliculas.txt'



    #Elegimos con que tipo de listas queremos hacer la practica
    tipo_lista = menus(0)

    #Inicializamos las listas
    #Si es 1, la lista sera un ArrayOrderedPositionalList
    if tipo_lista == 1:
        lista_peliculas       = aop.ArrayOrderedPositionalList()
        lista_peliculas_norep = aop.ArrayOrderedPositionalList()
        lista_peliculas_copy  = aop.ArrayOrderedPositionalList()  
    #Si no sera un LinkedOrderedPositionalList
    else:
        lista_peliculas       = lop.LinkedOrderedPositionalList()
        lista_peliculas_norep = lop.LinkedOrderedPositionalList()
        lista_peliculas_copy  = lop.LinkedOrderedPositionalList()

    #Hacemos esto ya que en el pdf especfica que se tiene que poder usar para ambas implementaciones.
    #Al poder definir que lista creas, se ve que uses la que uses, al usar metodos comunes
    #puedes usar un tipo o otro indiferentemente.



    #Guardamos el contenido del archivo
    with open(archivo, 'r', encoding='utf-8') as contenido:
        info_procesos = contenido.read()

    #Rellenamos las listas
    #Vamos sacando linea a linea y guardandona como una pelicula definida por la clase pelicula. 
    #Despues, la añadimos a la lista posicional
    for line in info_procesos.split('\n'):   

        if len(line) != 0 and len(line.split(';')) == 4:

            datos_pelicula = line.split(';')
            director_name, film_name, estreno, puntuation = datos_pelicula 

            pelicula = peli.Pelicula(director_name, film_name, estreno, puntuation)
            
            lista_peliculas.add(pelicula)
            lista_peliculas_copy.add(pelicula)
    

    #Rellenamos lista_peliculas_norep

    
    while True:
        
        #Iniciamos primero, siguiente y ultimo como elementos de la lista de esa posicion
        primero   = lista_peliculas_copy.get_element(lista_peliculas_copy.first())
        siguiente = lista_peliculas_copy.get_element(lista_peliculas_copy.after(lista_peliculas_copy.first()))
        ultima    = lista_peliculas_copy.get_element(lista_peliculas_copy.last())

        #Si primero es igual al siguiente, es que es repetido y lo eliminamos.
        if (primero.director_name == siguiente.director_name) and (primero.film_name == siguiente.film_name):
                
                lista_peliculas_copy.delete(lista_peliculas_copy.first())

        else:
            
            #Comparamos si la siguiente es igual a la ultima, si es asi añadimos las dos ya que las dos sifuientes son distintas
            if siguiente == ultima:

                lista_peliculas_norep.add(lista_peliculas_copy.delete(lista_peliculas_copy.first()))
                lista_peliculas_norep.add(lista_peliculas_copy.delete(lista_peliculas_copy.last()))
                break
            
            #Si no añadimos a lista peliculas y lo eliminamos de copy
            lista_peliculas_norep.add(lista_peliculas_copy.delete(lista_peliculas_copy.first()))

    #Creamos dos listas auxiliares para crear el dataframe
    aux_data_repeat = []
    aux_data_no_repeat = []

    #Rellenamos las listas 
    for u in lista_peliculas:
        aux_data_repeat.append(u.data_values())

    for u in lista_peliculas_norep:
        aux_data_no_repeat.append(u.data_values())

    #Creamos los DataFrames.
    data_repeat = pd.DataFrame(aux_data_repeat, columns = ['Titulo', 'Director', 'Año', 'Puntuacion'])

    data_no_repeat = pd.DataFrame(aux_data_no_repeat, columns = ['Titulo', 'Director', 'Año', 'Puntuacion'])



    #Entramos en la ejecucion del programa despues de recabar todos los datos.
    #LLamamos a menus(1) Menu: Principal, y dependiendo de lo que devuelva, llama a accion() con lo siguiente a realizar.

    #Cuando llega al final de la accion, sale, y vuelve a ejecutarse hasta que se selecciona 
    #Exit en el menu principal
    while True:
        siguiente = menus(1)

		
		

        if siguiente == 5:
            accion(5)
            
        elif siguiente == 1:
            accion(1, lista_peliculas, lista_peliculas_norep, data_repeat, data_no_repeat)

        elif siguiente == 2:
            accion(2, lista_peliculas, lista_peliculas_norep, data_repeat, data_no_repeat)
        
        elif siguiente == 3:
            accion(3, lista_peliculas, lista_peliculas_norep, data_repeat, data_no_repeat)
        
        elif siguiente == 4:
            accion(4, lista_peliculas, lista_peliculas_norep, data_repeat, data_no_repeat)
		
		
        

if __name__ == "__main__":
    #LLamamos a main()
    main()
