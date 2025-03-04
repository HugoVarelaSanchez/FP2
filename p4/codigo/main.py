#Hugo Varela Sanchez; hugo.varela.sanchez@udc.es
#David Fernandez Reimundez; david.fernandez.reimundez@udc.es
import avl_tree as a
import cursos as cursos
import pandas as pd
import sys


#AVISO: PARA LA IMPRESIÓN DE LOS ÁRBOLES TUVIMOS QUE SACAR DEL MAIN() DE AVL_TREE.PY LA FUNCIÓN "preorder_indent_BST", LA PUSIMOS FUERA DEL MAIN()


def menus(menu):
        
    '''
    Funcion de ayuda muy extensa. 
    Esta funcion lo que hace gestionar los 'menus' de la practica:

        El menu == 0, Principal

            Es el primero que aparece, y aparece siempre. 
            Elige que opcion de las 5 quieres usar.

        El menu == 1 Menu: Eleccion arbol

            Es un menu de eleccion auxiliar. Para algunas funciones como puede ser la eleccion de estadisticas
            puedes escoger que arbol quieres usar. 


        El menu == 2 Menu: Estadisticas

            Elige cual de los 3 tipos de estadisticas quieres ver

        El menu == 3 Menu: Apartado 1 submenu

            Es para elegir tan solo entre el arbol a y el arbol b.
            Con esto puedes elegir tan solo entre el arbol a y b



    ---------
    Parameters
    ----------

    menu: int
        Menu al que pretendes acceder.
        
    -------
    Returns
    -------
    
    quehacer : int
        Devuelven numeros de entre 1-5
    '''



    #La dinamica de eleccion es igual para todos, salvo que se cambia los valores mazximos y los prints

    # Si el menu es 0, es el menu principal.
    if menu == 0:

        #Entras en un bucle hasta que pones la opcion correcta
        while True:
            
            try:
                #Pides la opcion
                quehacer = int(input('\n---x---\n\nQue quieres hacer:\n(1)Imprimir arboles\n(2)Realizar operacion oferta agregada\n(3)Realizar operacion oferta comun\n(4)Estadisticas con pandas\n(5)Cerrar programa\n\nEleccion: '))
                #Si es 5 paras la ejecucion del programa (tan solo en este menu)
                if quehacer == 5:
                    sys.exit() #Para la ejecucion 
                
                #Tan solo puedes elegir un numero entre estos, si no da un error (excepcion) y itera de nuevo
                if (quehacer<1 or quehacer>5):
                    raise cursos.NumberNotInMenu
                break
                
            #Si el error se debe a que pusiste un tipo de variable distinta a int, te salta este mensaje de error
            except ValueError:
                print('\nDebes introducir un número\n')

            #Si poner un numero fuera de los que estan disponibles, te salta el siguiente mensje
            except cursos.NumberNotInMenu:
                print('\nDebe de ser un número del 1 al 5\n')

        #Si elijes una opcion posible, devuelve quehacer
        return quehacer





    #Repite el menu anterior pero elige cual de los 4 arboles
    elif menu == 1:
        while True:

            try:
                quehacer = int(input('\n---x---\n\nQue arbol quierez usar:\n(1)Empresa A\n(2)Empresa B\n(3)Curos comunes\n(4)Cursos totales\n\nEleccion: '))
                

                if (quehacer<1 or quehacer>4):
                    raise cursos.NumberNotInMenu
                break
                

            except ValueError:
                print('\nDebes introducir un número\n')

            except cursos.NumberNotInMenu:
                print('\nDebe de ser un número del 1 al 4\n')
        return quehacer


    #Repite el menu anterior pero elige que tipo de estadistica quieres
    elif menu == 2:
        while True:

            try:
                quehacer = int(input('\n---x---\n\nQue estadistica quieres mostrar:\n(1)Numero medio de estudiantes por idioma\n(2)Numero medio de estuaiantes por nivel\n(3)Ingresos totales posibles\n\nEleccion: '))
                
                
                if (quehacer<1 or quehacer>3):
                    raise cursos.NumberNotInMenu
                break
                

            except ValueError:
                print('\nDebes introducir un numero\n')

            except cursos.NumberNotInMenu:
                print('\nDebe de ser un numero del 1 al 3\n')
        return quehacer
    

        #Repite el menu anterior pero elige cual de las 2 empresas queires
    elif menu == 3:
        while True:

            try:
                quehacer = int(input('\n---x---\n\nQue arbol quierez imprimir:\n(1)Empresa A\n(2)Empresa B\n\nEleccion: \n'))
                

                if (quehacer<1 or quehacer>2):
                    raise cursos.NumberNotInMenu
                break
                

            except ValueError:
                print('\nDebes introducir un número\n')

            except cursos.NumberNotInMenu:
                print('\nDebe de ser un número del 1 al 2\n')
        return quehacer


























def accion(accion, arbol_a = a.AVL, arbol_b = a.AVL, arbol_diferencia = a.AVL, arbol_mezcla = a.AVL, df_a = pd.DataFrame, df_b = pd.DataFrame, df_u = pd.DataFrame, df_i = pd.DataFrame):
    
    
    '''
    Funcion que gestiona las acciones que se toman despues de la eleccion en los menus
    Esta muy ligada con la funcion menus

    La accion == 1 
        Imprime uno de los dos arboles principales
    
    La accion == 2
        Imprime el arbol que tiene la oferta agregada

    La accion == 3
        Imprime el arbol que tiene la oferta comun

    La accion == 4
        Imprime las estadisticas con pandas
    
    ---------
    Parameters
    ----------
    accion: int
        Accion qeu quieres tomar
    
    arbol_a: a.AVL
        arbol a
    
    arbol_b: a.AVL
        arbol b

    arbol_diferencia: a.AVL
        arbol que tiene todos los cursos que conforman la union de las academia
    
    arbol_mezcla: a.AVL
        Arbol que tiene todos los cursos que conforman la interseccion
        
    df_a: pd.DataFrame
        Dataframe con las esatdisticas de arbol a

    df_b: pd.DataFrame 
        Dataframe con las esatdisticas de arbol b

    df_u: pd.DataFrame
        Dataframe con las esatdisticas de arbol diferencia

    df_i: pd.DataFrame
        Dataframe con las esatdisticas de arbol mezcla


    -------
    Returns
    -------
    prints -> print()
    '''
    
    
    
    #Creamos dos diccionarios para saber que cojer con cada llamada a menus
    dic_aux_arbol = {1: df_a, 2: df_b, 3: df_i, 4 : df_u}
    aux_arbol = {1: arbol_a, 2: arbol_b, 3: arbol_diferencia, 4: arbol_mezcla}

    
    if accion == 1:
        #LLamamos al diccionario para saber que arbol es y lo mostramos por pantalla 
        arbol = aux_arbol[menus(3)]
        a.preorder_indent_BST(arbol, arbol.root(), 0)
        

    elif accion == 2:
        #Imprimimos el arbol de diferencia
        print('\nArbol oferta agregada: \n')
        a.preorder_indent_BST(aux_arbol[3], aux_arbol[3].root(), 0)

    
    elif accion == 3:
        #Imprimimos el arbol de oferta comun 
        print('\nArbol oferta comun: \n')
        a.preorder_indent_BST(aux_arbol[4], aux_arbol[4].root(), 0)

    elif accion == 4: 
        
        #Elegimos el tipo de estadisticas y el dataframe que quermos
        tipo_estadisticas = menus(2)
        data = dic_aux_arbol[menus(1)]

         #Para cada tipo de estadisticas filtramos

        if tipo_estadisticas == 1: 
            

            group_col = 'Idioma'
            target_col = 'Participantes'
            idioma_por_per_participantes = data.groupby(group_col).agg({target_col :["mean"]})
            print(idioma_por_per_participantes, '\n') 
        
        elif tipo_estadisticas == 2: 
            
            group_col = 'Nivel'
            target_col = 'Participantes'
            participantes_por_per_nivel = data.groupby(group_col).agg({target_col :["mean"]})
            print(participantes_por_per_nivel, '\n')
        
        elif tipo_estadisticas == 3: 
            ingresos_totales = data['Ingresos'].sum()
            print('Los ingresos totales son: ', round(ingresos_totales, 2), '€\n')
        













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



    #Creamos los arboles
    arbol_A = a.AVL()
    arbol_B = a.AVL()
    arbol_mezcla = a.AVL()
    arbol_diferencias = a.AVL()

    #Extracción de datos

    with open('ejA.txt','r',encoding='utf-8') as contenido1:
        datos_cursos_a = contenido1.read()

    with open('ejB.txt','r',encoding='utf-8') as contenido2:
        datos_cursos_b = contenido2.read()



    #Separamos los datos por líneas
    datos_cursos_a = datos_cursos_a.split('\n') 
    datos_cursos_b = datos_cursos_b.split('\n')

    #Listas para las estadisticas con pandas de cada arbol
    info_a =  []
    info_b = []   
    info_comun = []
    info_agregada = []



    #Extraemos la información y vamos creando los obejetos de la clase curso
    for line in datos_cursos_a:
        
        if len(line)>0:

            line = line.split(',')
            if len(line) == 6:

                name, dur, participantes, level, lang, precio = line
                curso = cursos.Curso(name, lang, dur, participantes, level, precio)
                

                #Creamos un identificafdor para filtrar dentro del arbol y lo insertamos
                identificador = f'{curso.curso_name}_{curso.level}_{curso.lang}'
                arbol_A[identificador] = curso
                info_a.append(arbol_A[identificador].info_curso())


    for line in datos_cursos_b:
        if len(line)>0:
            line = line.split(',')
            if len(line) == 6:
                name, dur, participantes, level, lang, precio = line
                curso = cursos.Curso(name, lang, dur, participantes, level, precio)
                
                #Creamos un identificafdor para filtrar dentro del arbol y lo insertamos
                identificador = f'{curso.curso_name}_{curso.level}_{curso.lang}'
                arbol_B[identificador] = curso
                info_b.append(arbol_B[identificador].info_curso())



   


    #Ahora para la oferta agregada y la común
                
    for i in arbol_A:

        curso_actual = arbol_A[i]

        if i in arbol_B:

            curso_actual2 = arbol_B[i]

            #Si el beneficio es mayor en el arbol b, como tenemos definido en el metodo magico que compara beneficios
            #Guardara en el nuevo arbol con los cursos iguales
            if curso_actual2 > curso_actual:

                curso = cursos.Curso(curso_actual.curso_name, curso_actual.lang, curso_actual2.durac, curso_actual.participantes + curso_actual2.participantes, curso_actual.level, curso_actual2.precio)
                #print(curso)
                identificador = f"{curso_actual.curso_name}_{curso_actual.level}_{curso_actual.lang + '__B'}"
                arbol_mezcla[i] = curso
                arbol_diferencias[identificador] = curso
                info_agregada.append(arbol_diferencias[identificador].info_curso())
                info_comun.append(arbol_mezcla[i].info_curso())
            #Lo msimo de antes pero guarda el del arbol a no el del b
            else:

                curso = cursos.Curso(curso_actual.curso_name +'__A', curso_actual.lang, curso_actual.durac, curso_actual.participantes + curso_actual2.participantes, curso_actual.level, curso_actual.precio)
                #print(curso.curso_name)
                identificador = f"{curso_actual.curso_name}_{curso_actual.level}_{curso_actual.lang + '__A'}"
                arbol_mezcla[i] = curso
                arbol_diferencias[identificador] = curso
                info_agregada.append(arbol_diferencias[identificador].info_curso())
                info_comun.append(arbol_mezcla[i].info_curso())

        #Si los cursos no son iguales va a guardar el curso en el arbol con los cursos diferentes
        else:
            #identificador1 = f"{curso_actual.curso_name}_{curso_actual.level}_{curso_actual.lang + '_A'}"
            arbol_diferencias[i] = curso_actual
            info_agregada.append(arbol_diferencias[i].info_curso())
        

        #Como hay cosas que hay en b y no en a, hay que recorrer b para cojer todas las cosas que estan en b y no en a.
        #y guardarlas en el nuevo arbol para asi completarlo
            
        for j in arbol_B:
            curso_actual2 = arbol_B[j]
            if j not in arbol_A:
                identificador2 = f"{curso_actual2.curso_name}_{curso_actual2.level}_{curso_actual2.lang + '_B'}"
                arbol_diferencias[j] = curso_actual2
                info_agregada.append(arbol_diferencias[j].info_curso())


    #Creamos las columnas que va a tener el dataframe
    columnas = ['Nombre', 'Idioma', 'Nivel', 'Duracion', 'Participantes', 'Precio','Beneficio', 'Ingresos']


    #Creamos los dataframes y los rellenamos
    df_a = pd.DataFrame(info_a, columns = columnas)
    df_b = pd.DataFrame(info_b, columns = columnas)
    df_u = pd.DataFrame(info_comun, columns = columnas)
    df_i = pd.DataFrame(info_agregada, columns = columnas)


    #Ciclo principal de ejecucion
    while True:

        #Imprimimos el primer menu
        quehacer = menus(0)

        if quehacer == 1:
            accion(1, arbol_A, arbol_B, arbol_diferencias, arbol_mezcla)

        if quehacer == 2: 
            accion(2, arbol_A, arbol_B, arbol_diferencias, arbol_mezcla)

        if quehacer == 3: 
            accion(3, arbol_A, arbol_B, arbol_diferencias, arbol_mezcla)
    
        if quehacer == 4: 
            accion(4, arbol_A, arbol_B, arbol_diferencias, arbol_mezcla, df_a, df_b, df_u, df_i)

        #Una vez ejecutado, volvemos a iterar




if __name__ == "__main__":

    main()




