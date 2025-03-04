#Hugo Varela Sanchez; hugo.varela.sanchez@udc.es
#David Fernandez Reimundez; david.fernandez.reimundez@udc.es
class Curso:
    """
    Clase que almacena los datos de un curso.


    ----------
    Attributes
    ----------
    
    curso_name: str
        Nombre del curso

    lang: str
        Lenguaje
    
    durac: int
        Duracion 

    participantes: int
        Numero de participantes
    
    precio: float
        Precio del curso

    benefico: float
        Precio que gana cada curso por hora y por estudiante
    
    ingresos: int
        Cantidad de dinero que obtiene el curso, es el número de estudiantes por el precio

    -------
    Methods
    -------

    def __init__ (self, curso_name: str, lang: str, durac: str, participantes: int, level: int, precio: float)
        Crea los atributos.

    def __str__ (self):
        Muestra por pantalla el precio y los participantes.

    def __eq__(self, other):
        Metodo magico que compara si un objeto es igual que otro
    
    def __ge__(self, other):
        Metodo magico que compara si un objeto es mayor o igual que otro

     def __gt__(self, other):
        Metodo magico que compara si un objeto es mayor que otro

    def info_curso(self):
        Metodo de ayuda que devuelve una lista con los datos del curso para crear los dataframes
    """ 



    def __init__(self, curso_name: str, lang: str, durac: str, participantes: int, level: int, precio: float, beneficio = None, ingresos = None):
        """Inicializa los atributos del curso."""
        self._curso_name = curso_name
        self._lang = lang
        self._durac = int(durac)
        self._participantes = int(participantes)
        self._level = level
        self._precio = float(precio)



    @property
    def curso_name(self):
        return self._curso_name

    @property
    def level(self):
        return self._level
        
    @property
    def durac(self):
        return self._durac

    @property
    def participantes(self):
        return self._participantes

    @property
    def precio(self):
        return self._precio

    @property
    def lang(self):
        return self._lang
    
    @property 
    def beneficio(self):
        return round((self.precio/self.durac * self.participantes), 2)
    
    @property
    def ingresos(self):
        return self.precio * self.participantes


    def info_curso(self):
        return [self.curso_name, self.lang, self.level, self.durac, self._participantes, self.precio, self.beneficio, self.ingresos]



    def __str__ (self):
        '''Permite imprimir por pantalla'''

        return f' Precio:{self.precio}, Participantes:{self._participantes}'
    



    def __eq__(self, other) -> bool:
        '''__eq__(self, other):
            Compara si un objeto es igual que otro
        
        Parameters
        ----------
        self

        other(curso):
            Es otro objeto del mismo tipo
        -------
        Bool.
        '''
        return self.beneficio == other.beneficio

    #Mayor o igual
    def __ge__(self, other) -> bool:
        '''__ge__(self, other):
            Compara si un objeto es mayor o igual que otro
        
        Parameters
        ----------
        self

        other(curso):
            Es otro objeto del mismo tipo
        -------
        Bool.
        '''
        return self.beneficio >= other.beneficio

    #Mayor
    def __gt__(self, other):
        '''__gt__(self, other):
            Compara si un objeto es mayor que otro
        
        Parameters
        ----------
        self

        other(curso):
            Es otro objeto del mismo tipo
        -------
        Bool.
        '''

        return self.beneficio > other.beneficio
    
class NumberNotInMenu(Exception):
        'Clase creada solo para ser una excepcion por si en un menu eliges un numero que no esta'
        
        pass
