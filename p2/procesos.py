
'''
David Fernández Reimúndez – david.fernandez.reimundez@udc.es
Hugo Varela Sánchez – hugo.varela.sanchez@udc.es
'''

import array_queue as arr

class Procesos:

    """Clase que simula un proceso.

    Esta clase crea el proceso que ejecutara una CPU o GPU, los cuales se usaran para 
    simular la ejecucion de estos.

    ----------
    Attributes
    ----------
    
    process_id: str
    Es el nombre del proceso.

    user_id: str
    Es el nombre del usuario que ejecuta el proceso.

    d_estimada: int
    Duracion estimada del procesa. (short / long)

    d_real: int
    Duracion real del proceso.

    interaccion: int
    Unidad de tiempo total

    tiempo_inicial: int
    Unidad en la que el proceso entra a ejecutarse

    -------
    Methods
    -------

    def __init__ (self, process_id, user_id, tipo, d_estimada, d_real,interaccion, tiempo_inicial)
        Crea los atributos.

    def __str__ (self):
        Muestra por pantalla el proceso.
    
    """ 

    def __init__(self,process_id : str, user_id : str, tipo : str, d_estimada : int, d_real : int,interaccion = None, tiempo_inicial = None, penalizado = 0, entrada_cola = None):

        """Asigna atributos al objeto.

        
        ----------
        Parameters
        ----------
        process_id: str
            Es el nombre del proceso.

        user_id: str
            Es el nombre del usuario que ejecuta el proceso.

        d_estimada: int
            Duracion estimada del procesa. (short / long)

        d_real: int
            Duracion real del proceso.

        interaccion: int
            Unidad de tiempo total

        tiempo_inicial: int
            Unidad en la que el proceso entra a ejecutarse
        
        penalizado: int
            Unidad que indica la penalización del proceso
            0 -> No ha sido penalizado
            1 -> Ha recibido penalización
            
        entrada_cola: int
            Unidad en la que el proceso entra a su respectiva cola de ejecución

        ------- 
        Returns
        -------

        None.

        """

        self._user_id = user_id
        self._process_id = process_id
        self._tipo = tipo
        self.d_estimada = d_estimada
        self._d_real = d_real
        self.interaccion = interaccion
        self.tiempo_inicial = tiempo_inicial
        self.penalizado = penalizado
        self.entrada_cola = entrada_cola
        
    def __str__(self) -> str:
        return f'Proceso: {self.process_id}, usuario: {self.user_id}, tipo: {self.tipo}, d_estimada: {self.d_estimada}, interaccion: {self.interaccion}, d_inicial: {self.tiempo_inicial}, d_real: {self.d_real}'


    @property
    def user_id(self):
        return self._user_id
    

    @property
    def process_id(self):
        return self._process_id
    

    @property
    def tipo(self):
        return self._tipo


    @property
    def d_estimada(self):
        return self._d_estimada
    @d_estimada.setter
    def d_estimada(self, d_estimada : str) -> str:
        self._d_estimada = d_estimada

        
    @property
    def d_real(self):
        return int(self._d_real)
    @d_real.setter
    def d_real(self, d_real : int) -> int:
        self._d_real = d_real
        

    @property
    def interaccion(self):
        return self._interaccion
    @interaccion.setter
    def interaccion(self, interaccion : int) -> int:
        self._interaccion = interaccion


    @property
    def tiempo_inicial(self):
        return self._tiempo_inicial
    @tiempo_inicial.setter
    def tiempo_inicial(self, tiempo_inicial : None) -> int:
        self._tiempo_inicial = tiempo_inicial
        
        
    @property
    def penalizado(self):
        return self._penalizado
    @penalizado.setter
    def penalizado(self, penalizado : int) -> int:
        self._penalizado = penalizado


    @property
    def entrada_cola(self):
        return self._entrada_cola
    @entrada_cola.setter
    def entrada_cola(self, entrada_cola: None) -> int:
        self._entrada_cola = entrada_cola
