class Curso:
    """Clase que almacena los datos de un curso."""


    def __init__(self, curso_name: str, lang: str, durac: str, participantes: int, level: int, precio: float):
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
    @participantes.setter
    def participantes(self, participantes):
        self.participantes = participantes

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        self.precio = precio
        
    @property
    def lang(self):
        return self._lang
    
    @property 
    def beneficio(self):
        return round((self.precio/self.durac * self.participantes), 2)
    
    @property
    def ingresos(self):
        return self.precio * self.participantes

    @property
    def info_curso(self):
        return [self.curso_name, self.lang, self.level, self.durac, self._participantes, self.precio, self.beneficio, self.ingresos]

    def __str__ (self):
        return f' Precio:{self.precio}, Participantes:{self._participantes}'
    
    def __eq__(self, other) -> bool:
        '''__eq__(self):
            Compara si un objeto es igual que otro
        
        Parameters
        ----------
        self

        other(Pelicula):
            Es otro objeto del mismo tipo
        -------
        Bool.
        '''
        return self.beneficio == other.beneficio

    #Mayor o igual
    def __ge__(self, other) -> bool:
        '''__ge__(self):
            Compara si un objeto es mayor o igual que otro
        
        Parameters
        ----------
        self

        other(Pelicula):
            Es otro objeto del mismo tipo
        -------
        Bool.
        '''
        return self.beneficio >= other.beneficio

    #Mayor
    def __gt__(self, other):
        '''__gt__(self):
            Compara si un objeto es mayor que otro
        
        Parameters
        ----------
        self

        other(Pelicula):
            Es otro objeto del mismo tipo
        -------
        Bool.
        '''

        return self.beneficio > other.beneficio
        