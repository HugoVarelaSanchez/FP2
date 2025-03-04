#Importamos la clase pokemon creada anteriormente

from pokemon import *

class Trainer:
    ''' Representa un entrenador pokemon

        Creamos una clase que crea un entrenador pokemon.
        Este tendra una serie de pokemons.

        Atributos:
        ----------
            name: str
                Nombre del entrenadir
            
            pokemon: list
                Lista de pokemons a utilizar

        -------

        Metodos 


        pokemons_names (self) -> str        
            Devuelve el nombre de los pokemons
        
        all_debilitated(self) -> bool
            Comprueba si todos los pokemons estan debilitados. Si estan debiiltados devolvera True

        select_first_pokemon (self) -> Pokemon or None
            Elige el primer pokemon que no esta debilitado

        select_next_pokemon (self, p:Pokemon) ->Pokemon:
            Elige el siguiente pokemon en funcion a la efectividad frente 
            a su oponente y al nivel siempre que no este debilitado
        '''
    
    def __init__(self, name:str, pokemon:list):
        """ Asigna atributos al objeto.
            Establece el nombre, y la lista de pokemons del entrenador

        Atributos:
            ----------
            name:  str
                Nombre del entrenador

            pokemon:  list
              lista con todos los pokemons que conforman el equipo del entrenador
            -------
        Returns:
            None.
        """ 
        self.name = name
        self.pokemon = pokemon
    

#'''---------------------------------------------------Atributos----------------------------------------'''


    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, name:str):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")


    @property
    def pokemon(self) -> list:
        return self._pokemon
    @pokemon.setter
    def pokemon(self, pokemon:list):
        if isinstance(pokemon, list) and len(pokemon) > 0:
            self._pokemon = pokemon
        else:
            raise ValueError("Pokemon must be a non-empty list")



#'''---------------------------------------------------Metodos----------------------------------------'''



    def select_first_pokemon(self):
        """Escoge el primer pokemon que se elige para la batalla.
            
            Atributos:
            ----------
            self 

            --------
            Returns:
                Pokemon or None
                    El primer pokemon no debilitado, o None
            """ 

        for item in self.pokemon:
                if not item.is_debilitated():
                    return item
        return None
            
        



    def all_debilitated(self) -> bool:
        """Devuelve si todos los pokemons estan debilitados o no.

            Atributos:
            ----------
            self 

            --------

            Devuelve: 
                bool
                    bool, True si todos estan debilitados y False si hay alguno vivo
            """ 

        for item in self.pokemon:
                if item.hp>0:
                    return False
        return True





    def select_next_pokemon(self, p:Pokemon) -> Pokemon:
        """ Selecciona el siguiente pokemon en salir a combatir, teniendo 
            en cuenta la efectividad y el nivel.

            Atributos:
            ----------
            self

            p: Pokemon
                El pokemon del rival para que pokemon nos es mejor
            --------

            Devuelve: 
                elegido: Pokemon
                    Nos devuelve el pokemon que mejor se adapte a la situacion
            """
        assert self.all_debilitated()==False, 'Todos los pokemon de {self.name} estan debilitados'

        
        efe, lvl, indice = -2, int, int     #Variables que nos ayudaran a guardar valores

        for i in self._pokemon:

                if i.is_debilitated() == False:

                    if i.effectiveness(p) > efe:
                        efe = i.effectiveness(p)
                        lvl = i.level
                        elegido = i

                    elif i.effectiveness(p) == efe:
                        if i.level > lvl:
                            lvl = i.level
                            elegido = i
        return elegido

    def pokemon_names(self) -> list:
        ''
        """Devuelve los nombres de los pokemons
            Atributos:
            ----------
            self 
            --------

            Devuelve: 
                list
                    Una lista con el nombre de los pokemons de cada entrenador
            """ 
        return [pokemon.names for pokemon in self._pokemon]

