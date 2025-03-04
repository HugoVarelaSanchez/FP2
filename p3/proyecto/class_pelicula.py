#Hugo Varela Sanchez; hugo.varela.sanchez@udc.es
#David Fernandez Reimundez; david.fernandez.reimundez@udc.es
class Pelicula:
    """Clase que almacena los datos de una pelicula.

    Esta clase crea una pelicula la cual contiene los datos de esta.

    ----------
    Attributes
    ----------
    
    film_name: str
        Es el nombre del proceso.

    director_name: str
        Es el nombre del usuario que ejecuta el proceso.

    estreno : int
        año de estreno

    puntuacion : float
        nota de la pelicula


    -------
    Methods
    -------

    def __init__ (self, film_name, director_name, estreno, puntuation)
        Crea los atributos.

    def __str__ (self):
        Muestra por pantalla el proceso.

    def __eq__(self, other):
        metodo magico que compara si un objeto es igual que otro
    
    def __ge__(self, other):
        metodo magico que compara si un objeto es mayor o igual que otro

     def __gt__(self, other):
        metodo magico que compara si un objeto es mayor que otro

    def data_values(self):
        metodo de ayuda que devuelve una lista con los datos de la peli
    """ 

    def __init__(self,director_name : str, film_name  : str, estreno : str, puntuation : float):

        """Asigna atributos al objeto.

        
        ----------
        Parameters
        ----------
        film_name: str
            Es el nombre del proceso.

        director_name: str
            Es el nombre del usuario que ejecuta el proceso.

        puntuation: int
            Duracion estimada del procesa. (short / long)

        d_real: int
            Duracion real del proceso.

        ------- 
        Returns
        -------

        None.

        """

        self._director_name = director_name
        self._film_name = film_name
        self._estreno = int(estreno)
        self._puntuation = float(puntuation)

    #Atributos

    @property
    def director_name(self):
        return self._director_name

    @property
    def film_name(self):
        return self._film_name
    
    @property
    def estreno(self):
        return self._estreno

    @property
    def puntuation(self):
        return self._puntuation
    

    #Metodos magicos:
    def __str__(self) -> str:
        '''__str__(self):
            Devuelve la peli por pantalla
        
        Parameters
        ----------
        self 
        -------
        None.
        '''

        #return f'Película: {self.film_name}, Director: {self.director_name}, Estreno: {self.estreno}, Puntuation: {self.puntuation}'
        return f'Director: {self.director_name}, Pelicula: {self.film_name} Estreno: {self.estreno}, Puntuation: {self.puntuation}'


    #Metodos magicos comparativos

    #Comparamos si es igual
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

        if self.director_name == other.director_name:

            if self.estreno == other.estreno:

                if self.film_name == other.film_name:
                    return self.film_name == other.film_name
                
            else:
                return False
        else:
            return False

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
        
        if self.director_name == other.director_name:

            if self.estreno == other.estreno:
                return self.film_name >= other.film_name
            
            else:
                return self.estreno >= other.estreno
            
        else:
            return self.director_name >= other.director_name

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

        if self.director_name == other.director_name:

            if self.estreno == other.estreno:
                return self.film_name > other.film_name
            
            else:
                return self.estreno > other.estreno
            
        else:
            return self.director_name > other.director_name
        

    #Metodos de ayuda

    def data_values(self) -> list:
        '''data_values(self):
            Devuelve una lista con datos que seran claves para la creacion de los dataframes
        
        Parameters
        ----------
        self
o
        -------
        list.
        '''
        lista = [self.film_name, self.director_name, self.estreno, self.puntuation]
        return lista
    


class NumberNotInMenu(Exception):
    """Exceocion
    Error por si no se selecciona una opcion del menu
    Attributes
    ----------
    NONE
    -------
    NONE
 """ 
    pass