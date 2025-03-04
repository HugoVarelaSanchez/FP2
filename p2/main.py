
'''
David Fernández Reimúndez – david.fernandez.reimundez@udc.es
Hugo Varela Sánchez – hugo.varela.sanchez@udc.es
'''

#Importamos los archivos y librerias necesarias

import array_queue as aq
from procesos import *
import sys
import pandas as pd



#'------------------------------------------------Gestor de colas-------------------------------------------'

class Gestor_Colas:
    
    """Un gestor de colas.

    Para realizar la simulacion, vamos a necesitar usar una
    estructura llamada 'Cola'.
    Como utilizaremos varias necesitaremos una clase que
    las gestione.

    ----------
    Attributes
    ----------

    proceso: Procesos (class)
        Proceso a ejecutarse.

    -------
    Methods
    -------

    def __init__ (self, proceso):
        Crea los atributos.

    def __str__ (self):
        Muestra por pantalla el proceso.

    def is_penalitated (self, proceso, usuarios, timepo):
        Añade a usuarios que cumplan ciertos requisitos 
        en un proceso a una lista para penalizarlos en un futuro.
    
    def tipo_cola(self,colas): 
        Añade el proceso a la cola que se ocupara de gestionar 
        la ejecucion del proceso

    def penalizar(usuarios_penalizados, cola, colas):
        Si el nombre de usuarios esta en penalizados, lo elimina
        de la cola short en la que esta para añadirla a la
        cola long del mismo tipo.
        Tambien elimina al usuario de la lista de penalizados
    """





    def __init__(self, proceso : Procesos):

        """Asigna atributos al objeto.

        
        ----------
        Parameters
        ----------
        proceso: Procesos (class)
        Es el proceso que se debe gestionar

        ------- 
        Returns
        -------

        None.

        """
        
        self._proceso = proceso


    def __str__ (self):
        return f'{self.proceso}'
        

    @property
    def proceso(self):
        return self._proceso
    


#'----------------------------------------------------Is Penalitated------------------------------------------------------'



    def is_penalitated(self, proceso : Procesos, usuarios_penalizados : list, ciclo : int) -> None:
        """Almacena las personas que deben ser penalizadas.

        ----------
        Parameters
        ----------

        proceso : Procesos (class)
            El proceso que se esta gestionando.

        usuarios_penalizados : list
            Usuarios penalizados.

        --------
        Returns
        --------
        
        None
        
        """ 

        #Comprobamos si para un proceso short, el tiempo de ejecucion es mayor a 5.
        #Si es asi, y no esta en la lista de penalizados, guarda a ese usuario en la listra de penalizados

        tiempo_ejec = (proceso.interaccion - proceso.tiempo_inicial) + 1
        if (tiempo_ejec > 5) and (proceso.user_id not in usuarios_penalizados):
            
            usuarios_penalizados.append(proceso.user_id)
            print(f'Penalización activa: ciclo = {ciclo}, {proceso.user_id} \n')
        
#'----------------------------------------------------Tipo cola------------------------------------------------------'


    def tipo_cola(self, colas_ejecucion:list, ciclo : int) -> None: 

        """Almacena el proceso en la cole correspondiente.

        ----------
        Parameters
        ----------

        colas_ejecucion : list
            Lista con las colas de ejecucion
        --------
        Returns
        --------
        
        None
        """ 

        #Asignamos a i el tipo de proceso (CPU / GPU) y comprobamos.
        #Una vez comprobado comprueba si es (Short / Long) y lo añade a la cola de ejecucion correspondiente
        #colas[] es esa cola

        i = self.proceso

        if i.tipo == 'cpu':
            
            if i.d_estimada == 'short':
                colas_ejecucion[3].enqueue(i)
                print(f'\nProceso {i.process_id} añadido a la cola de ejecucion: \n{ciclo} {i.process_id} {i.user_id}\n{i.tipo} {i.d_estimada}\n')
                
            else:
                colas_ejecucion[2].enqueue(i)
                print(f'\nProceso {i.process_id} añadido a la cola de ejecucion: \n{ciclo} {i.process_id} {i.user_id}\n{i.tipo} {i.d_estimada}\n')

        else:

            if i.d_estimada == 'short':
                colas_ejecucion[1].enqueue(i)
                print(f'\nProceso {i.process_id} añadido a la cola de ejecucion: \n{ciclo} {i.process_id} {i.user_id}\n{i.tipo} {i.d_estimada}\n')

            else:
                colas_ejecucion[0].enqueue(i)
                print(f'\nProceso {i.process_id} añadido a la cola de ejecucion: \n{ciclo} {i.process_id} {i.user_id}\n{i.tipo} {i.d_estimada}\n')



#'----------------------------------------------------Penalizar------------------------------------------------------'


    def penalizar(self, usuarios_penalizados : list, cola : aq.ArrayQueue, colas_ejecucion : list, ciclo : int):
        
        """Penaliza a los usuarios que deberian ser penalizados.
    
            ----------
            Parameters
            ----------
    
            usuarios_penalizados : list
                Usuarios penalizados
    
            cola: aq.ArrayQueue
                Una cola que almacena procesos
    
            colas_ejecucion : list
                Lista con las colas de ejecucion
    
    
            --------
            Returns
            --------
            
            None
            """ 
        
        #Definimos aux como el proceso que se esta ejecutando o se va a ejecutar, y guardamos el nombre del usuario de ese proceso
    
        aux = cola.first()
        nombre = aux.user_id
        
        #Si el usuario esta en la lista de penalizados, para cada tipo, le cambia la duracion estimada a Long, y lo 
        #añade a la cola correspondiente inicializando su tiempo inicial.
    
        if nombre in usuarios_penalizados:
            print(f'\tPenalización aplicada: ciclo = {ciclo}, {aux.process_id} {aux.user_id} \n')
    
            if aux.tipo == 'gpu':
    
                aux.tiempo_inicial = None
    
                colas_ejecucion[0].enqueue(cola.dequeue())
                usuarios_penalizados.pop(usuarios_penalizados.index(aux.user_id))
                
                aux.penalizado = 1
                
                aux.d_estimada = 'long*'
                
                aux.entrada_cola = ciclo
            
            elif aux.tipo == 'cpu':
                
                aux.tiempo_inicial = None
    
                
                colas_ejecucion[2].enqueue(cola.dequeue())
                usuarios_penalizados.pop(usuarios_penalizados.index(aux.user_id))
                
                aux.penalizado = 1

                aux.d_estimada = 'long*'
                
                aux.entrada_cola = ciclo


#'----------------------------------------------------Ejecucion------------------------------------------------------'


#Funcion para la ejecucion de los procesos

def ejecucion (cola : aq.ArrayQueue, usuarios_penalizados : list, ciclo : int, colas_ejecucion : list, nombre_proceso : str, values_tablas: list) -> None:

    """Ejecuta los procesos por unidad de tiempo.

        ----------
        Parameters
        ----------

        cola: aq.ArrayQueue
            Una cola de ejecucion.

        usuarios_penalizados:list
            Lista con los usuarios penalizados
        
        contador : int
            Variable que lleva la unidad de tiempo

        colas_ejecucion : list
            Lista que almacena las colas de ejecucion

        nombre_proceso : str
            Cadena de texto con el nombre de la cola de ejecucion que se usa en esa llamada

        --------
        Returns
        --------
        
        None
        """ 

    #Definimos aux como el proceso que se va a ejecutar
    #Definimos proceso como el gestor de colas de aux

    aux = cola.first()
    proceso = Gestor_Colas(aux)
    

    #Si el tiempo inicial es None, es que va a ser la primera vez que se ejecute, por lo tanto
    #su tiempo inicial sera la unidad de tiempo del momento, igual que la interaccion.
    #Ademas, si es short comprobara si el usuario esta penalizado para aplicarle o no sancion.

    #Si no es none es que no es su primera vez. Si la duracion real es el tiempo en ese mometno 
    #menos el tiempo con el que inicio, es que acaba de terminar, por lo tanto comprobamos di si 
    #hay que penalizar al usuario y eliminamos el proceso

    #Si no es igual simplemente interaccion sera igual al la unidad de tiempo actual

    if aux.tiempo_inicial == None:

        aux.tiempo_inicial = ciclo
        aux.interaccion = ciclo
        print(f'{nombre_proceso}: {aux.process_id} \n\tPreparado para empezar a ejecutarse')
        if aux.d_estimada == 'short':
             proceso.penalizar(usuarios_penalizados, cola, colas_ejecucion, ciclo)
    
    else:

        if aux.d_real == (ciclo - aux.tiempo_inicial):

            print(f'\n{nombre_proceso}: {aux.process_id} terminado:\n\t{ciclo} {aux.process_id} {aux.tipo}\n\tDu_estimada: {aux.d_estimada}, Ciclo: {aux.interaccion}, Ciclo_inicial: {aux.tiempo_inicial}, Duracion: {aux.d_real}\n')
                
            if aux.d_estimada == 'short' :

                proceso.is_penalitated(aux, usuarios_penalizados, ciclo)
                
            info_proceso = [aux.user_id, aux.process_id, nombre_proceso, (aux.tiempo_inicial - aux.entrada_cola), aux.penalizado, aux.entrada_cola, aux.tiempo_inicial]
            values_tablas.append(info_proceso)   
            
            cola.dequeue()
            
            
            
        elif 1 == (ciclo - aux.tiempo_inicial):
            print(f'{nombre_proceso}: proceso {aux.process_id} \n\tPrimera ejecucion')
            aux.interaccion = ciclo

        else:
            aux.interaccion = ciclo
            print(f'{nombre_proceso}: {aux.process_id}')
    


'----------------------------------------------------Main------------------------------------------------------'











def main():

    """Funcion encargada de ejecutar el codigo.

    ----------
    Parameters
    ----------

    None

    -------
    Returns
    -------

    None.
    """ 


    #Pasamos los procesos a la variable archivo

    archivo = sys.argv[1]
    #archivo = 'processes0.txt'

    #Creamos las colas y las metemos en una tupla

    cola_reg= aq.ArrayQueue()
    gpu_short = aq.ArrayQueue()
    gpu_long = aq.ArrayQueue()
    cpu_short = aq.ArrayQueue()
    cpu_long = aq.ArrayQueue()
    colas_ejecucion = (gpu_long, gpu_short, cpu_long, cpu_short)

    #Creamos un par mas de variables
    values_tablas = []
    usuarios_penalizados = []
    contador = 0
    #Se puede pensar que el contador deberia empezar en uno, para nosotros no. A nuestra interpretacion, cuando ponemos un cronometro, el tiempo empieza en cero
    

    bucle_aux =(len(cpu_long) + len(cpu_short) + len(gpu_long) + len(gpu_short))
    
    #~Leemos el archivo y los guardamos en info procesos

    with open(archivo, 'r') as contenido:
        info_procesos = contenido.read()


    #Creamos un for, dondem metemos cada linea de codigo de longitud distinta de 0 en la cola

    for line in info_procesos.split('\n'):
        
        if len(line) != 0:

            datos_proceso = line.split()
            proces_id, user_id, tipo1, dur_estimada, dur_real = datos_proceso
            proceso1 = Procesos(proces_id, user_id, tipo1, dur_estimada, dur_real)

            cola_reg.enqueue(proceso1)


    #Creamos un bucle en el que simulamos todo
    #Cada ciclo de este bucle es el equivalente a una unidad de tiempo
    #El tiempo se guarda en la variable contador

    # si existe algun elemento en la cola de registros o en las colas de ejecucion, el bucle seguira
    while (len(cola_reg) + bucle_aux) != 0:    

        #Si la lontud de la cola de procesos no es 0, introduce el siguiente proceso a la cola correspondiente
        print(f'\n-------- \nCiclo: {contador}\n-------- \n')
        print(f'Personas con penalizacion: {usuarios_penalizados}\n')

        if not(len(cola_reg) == 0):

            proceso_actual = cola_reg.dequeue()
            
            proceso = Gestor_Colas(proceso_actual)
            proceso_actual.entrada_cola = contador
            proceso.tipo_cola(colas_ejecucion, contador)
        
        #Ejecutamos los procesos (sumamos una unidad de tiempo, añadimos penalizaciones, sacamos...)


        if len(cpu_short) > 0:
            ejecucion(cpu_short, usuarios_penalizados, contador,colas_ejecucion, 'CPU Short', values_tablas)
        else:
            print('CPU Short: None')
            
        if len(gpu_short) > 0:
            ejecucion(gpu_short, usuarios_penalizados, contador,colas_ejecucion, 'GPU Short', values_tablas)
        else:
            print('GPU Short: None')

        if len(cpu_long) > 0:
            ejecucion(cpu_long, usuarios_penalizados, contador,colas_ejecucion, 'CPU Long',values_tablas)
        else:
            print('CPU Long: None')
            
        if len(gpu_long) > 0:
            ejecucion(gpu_long, usuarios_penalizados, contador, colas_ejecucion, 'GPU Long', values_tablas)
        else:
            print('GPU Long: None')
            


        

        #Incrementamos contador en 1 y actualizamos bucle_aux

        contador += 1
        bucle_aux =(len(cpu_long) + len(cpu_short) + len(gpu_long) + len(gpu_short))

        
    print('\nSe han terminado de ejecutar todos los procesos')
    
    data = pd.DataFrame(values_tablas, columns = ['Usuario', 'Proceso', 'Tipo_cola', 'Perm_gestor', 'Penalizacion','Entrada','Inicio'])
    print(data)
    
    print('\n\n\n')
    
    group_col = 'Usuario'
    target_col = 'Penalizacion'
    penals = data.groupby(group_col).agg({target_col :["mean"]})
    print(penals)
    
    print('\n\n\n')
    
    group_col = 'Tipo_cola'
    target_col = 'Perm_gestor'
    permanencia = data.groupby(group_col).agg({target_col :["mean"]})
    print(permanencia)

if __name__ == '__main__':
    
    main()

    

    