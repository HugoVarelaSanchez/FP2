#Importamos ABC para poder definir clases abstractas

from abc import ABC, abstractmethod

#---------------------------------------------------Class Pokemon------------------------------------
class Pokemon (ABC):
    ''' Representa a un pokemon

        Creamos una clase que va a contener un pokemon, un personaje ficticio de un videojuego.
        Estos combatiran entre ellos.

        Atributos
        ----------
            name: str
                Nombre del pokemon

            level: int
                Nivel del pokemon

            strength: int
                Fuerza con al que ataca

            defense: int
                Defensa que tiene. La defensa reduce el danho recibido

            total_hp: int
                Vida total del pokemon

            hp: int
                Vida puntual del pokemon

            agility: int
                Velocidad. Si un pokemon tiene mas velocidad que otro atacara antes


        -------

        Metodos
        -------
        basic_attack (self, p:Pokemon) -> int        
            Realiza un ataque basico
        
        is_debilitated(self) -> bool
            Comprueba si el pokemon esta debilitado

        effectiveness (self)
            Define un metodo abstracto que se usara mas adelante con la subclase de los tipos

        factor (self, p:Pokemon) -> float:
            Devueve, si el tipo del pokemon al que se le 
            aplica este metodo es efectivo, no efectivo, 
            o poco efectivo contra el del rival, en forma 
            de un multiplicador del danho
        '''

    def __init__ (self, name:str, level:int, strength:int, defense:int, total_hp:int, hp:int, agility:int, ):   #hp:int = total_hp, esto es asi pq generalmente nos interesa que la vida sea la misma que la vida total, esto da fallo, buscar solucion
        """Asigna atributos al objeto.
        Atributos   
        ----------
            name: str
            Nombre del pokemon

            level: int
            Nivel del pokemon

            strength: int
            Fuerza con al que ataca

            defense: int
            Defensa que tiene. La defensa reduce el danho recibido

            total_hp: int
            Vida total del pokemon

            hp: int
            Vida puntual del pokemon

            agility: int
            Velocidad. Si un pokemon tiene mas velocidad que otro atacara antes
        -------
        Return: 
            None.
        """ 

        self._name = name
        self.level = level
        self.strength = strength
        self.defense = defense 
        self.hp = hp
        self._total_hp = total_hp
        self._agility = agility
        self._pokemon_type = None

        #'''-------------------------------------------------Preparar atributos----------------------------------------------'''

    @property
    def name(self)->str:
        return self._name
    

    @property
    def level(self)->int:
        return self._level
    @level.setter
    def level(self, level)->None:
        if isinstance(level, int) and level >= 0:
            self._level = level        
        else:
            raise ValueError("Level must be a non-negative integer")
        

    
    @property
    def strength (self)->int:
        return self._strength
    @strength.setter
    def strength(self, strength)->None:
        if isinstance(strength, int) and strength >= 0:
            self._strength = strength        
        else:
            raise ValueError("Strength must be a non-negative integer")
        


    @property
    def defense (self)->int:
        return self._defense
    @defense.setter
    def defense (self, defense)->None:
        if isinstance(defense, int) and defense >= 0:
            self._defense = defense        
        else:
            raise ValueError("Defense must be a non-negative integer")
        

    
    @property
    def hp (self)->int:
        return self._hp
    @hp.setter
    def hp (self, hp)->None:
        if isinstance(hp, int) and hp >= 0:
            self._hp =hp        
        else:
            raise ValueError("Hp must be a non-negative integer")
        


    @property
    def total_hp (self)->int:
        return self._total_hp
    
    
    @property
    def agility (self)->int:
        return self._agility
    @agility.setter
    def agility (self, agility)->None:
        if isinstance(agility, int) and agility >= 0:
            self._agility = agility       
        else:
            raise ValueError("Agility must be a non-negative integer")
        
    


    @property
    def pokemon_type(self)->None:
        return self._pokemon_type
    @pokemon_type.setter
    def pokemon_type(self, pokemon_type):
        self._pokemon_type = pokemon_type


    def __str__(self)->str:
        return f'{self.name}({self.pokemon_type}) Stats: Level:{self.level} ATT:{self.strength} DEF:{self.defense} AGI:{self.agility} HP:{self.hp}/{self.total_hp}'
    

    #'''-----------------------------------------------------Metodos------------------------------------------------------'''

    def basic_attack (self, p ) -> int: #Donde p es el pokemon rival
        """'En un combate, quita danho basico al contrincante y devuelve el danho quitado como un float'
        Atributos
        ----------
        self 

        p : Pokemon
            El pokemon contra el que peleas
        --------
        Returns: 
            damage : int
                Resultado de el ataque de nuestro pokemon menos la defensa del rival
        """ 

        
        damage = max((self.strength-p.defense), 1)
        if damage > p.hp:
            damage = p.hp
        p.hp = max(p.hp - damage, 0)
        return damage
    

    def is_debilitated(self)->bool: 
        """Devuelve si el pokemon esta vivo (hp > 0), o si esta muerto (hp == 0)
        Parameters
        ----------
        self 

        --------
        Returns: 
            bool
                Resultado de comprobar si el pokemon esta vivo o no
        """ 
        
        if self.hp == 0:
            return True
        else:
            return False
    


    @abstractmethod                                     
    def effectiveness (self, p): #Donde p es el pokemon rival
        """Define un metodo abstracto que se usara mas adelante con la subclase de los tipos

        Atributos
        ----------
        self 

        p: Pokemon
            el pokemon rival
        --------
        Returns:
            none
        """ 
        pass


    def factor (self, p) -> float:  #Donde p es el pokemon rival
        """'Devueve, si el tipo del pokemon al que se le aplica este metodo es efectivo, no efectivo, o poco efectivo contra el del rival, en forma de un multiplicador del danho'

        Parameters
        ----------
        self 

        p : Pokemon
            El pokemon contra el que peleas
        --------
        Returns:
            factor : float
                resultado de comprobar si el tipo es efectivo o no
        """ 
        
        
        tipo_s = self.pokemon_type
        tipo_r = p.pokemon_type

        if tipo_r == tipo_s:
            factor = 1
        elif (tipo_s == 'Fire' and tipo_r == 'Grass') or (tipo_s == 'Grass' and tipo_r == 'Water') or (tipo_s == 'Water' and tipo_r == 'Fire'):
            factor = 1.5
        else:
            factor = 0.5
        
        return factor

#'''---------------------------------------------------------------------Subclases(tipos)---------------------------------------------------'''


#'''-----------------------------------------------Water pokemon--------------------------------'''
class WaterPokemon(Pokemon):
    
    ''' Se define la clase que contiene a los pokemons de tipo agua.
    Esta es una subclase de pokemon por lo que tiene todos los atributos de esta

    Atributos
    ----------
            name: str
                Nombre del pokemon

            level: int
                Nivel del pokemon

            strength: int
                Fuerza con al que ataca

            defense: int
                Defensa que tiene. La defensa reduce el danho recibido

            total_hp: int
                Vida total del pokemon

            hp: int
                Vida puntual del pokemon

            agility: int
                Velocidad. Si un pokemon tiene mas velocidad que otro atacara antes

            pokemon_type: str
                Tipo que tiene: fuego, agua o planta

            surge_mode: bool
                Booster para pokemons de tipo agua con menos de la mitad de la vida

            
     -------

     Metodos
     -------
        check_surge_mode(self)->bool
            Comprueba si se activa el atributo surge mode
        
        water_attack(self, p:Pokemon)->int
            Realiza el ataque especial de tipo agua. Devuelve el danho

        def effectiveness(self, p:Pokemon) -> int
            Devuelve un 1 si es efectivo, un 0 si no es efectivo y un -1 si no le afecta
        '''
    

    def __init__ (self, name:str, level:int, strength:int, defense:int, total_hp:int, hp:int, agility:int, surge_mode:bool):
        

        """Asigna atributos al objeto, al ser una clase heredadam tiene los de la clase padre tambien.

        Atributos:
        ----------
            name: str
                Nombre del pokemon

            level: int
                Nivel del pokemon

            strength: int
                Fuerza con al que ataca

            defense: int
                Defensa que tiene. La defensa reduce el danho recibido

            total_hp: int
                Vida total del pokemon

            hp: int
                Vida puntual del pokemon

            agility: int
                Velocidad. Si un pokemon tiene mas velocidad que otro atacara antes

            pokemon_type: str
                Tipo que tiene: fuego, agua o planta

            surge_mode: bool
                Booster para pokemons de tipo agua con menos de la mitad de la vida
        -------
        Returns:
            None.
        """ 

        super().__init__(name, level, strength, defense, hp, total_hp, agility)
        self.pokemon_type = 'Water'
        self._surge_mode = False

    #'''---------------------------------------------Atributos (water)--------------------------------'''

    @property 
    def surge_mode(self)->bool:
        return self._surge_mode
    @surge_mode.setter
    def surge_mode(self, surge_mode:bool)->None:
        if isinstance(surge_mode, bool):
            self._surge_mode = surge_mode
        else:
            raise ValueError("Surge mode must be a bool")
    #'''--------------------------------------------Metodos-----------------------------------'''

    def check_surge_mode(self) -> bool:
        """Comprueba si se activa el atributo surge mode

        Atributos
        ----------
        self 
        
        --------
        Returns:
                bool
                    Si la vida esta a menos de la mitad devuelve True
        """ 
        if self.hp < (self.total_hp/2):
            self.surge_mode = True
            return True
        else:
            return False


    def water_attack(self, p:Pokemon) -> int:
        """Realiza el ataque especial de tipo agua. Devuelve el danho

        Atributos
        ----------
        self 

        p : Pokemon
            El pokemon contra el que peleas
        --------
        Returns
            damage : int
                El maximo entre 1 y el danho multiplicado por booster si esta activo de surge mode y por el factor
        """ 


        damage = max(1, int((self.factor(p) * self.strength) - p.defense))

        if self.check_surge_mode() == True:
            
            damage = max(1, int(((self.factor(p)+0.1) * self.strength) - p.defense))

        if damage > p.hp:
            damage = p.hp

        p.hp = p.hp - damage
        return damage


    def effectiveness(self, p:Pokemon) -> int:
        
        """Comprueba si es efectivo (1), si no es efectivo (0) o si no le afecta (-1)

        Atributos
        ----------
        self 

        p : Pokemon
            El pokemon contra el que peleas
        --------
            int
                Devuelve un 1 si es efectivo, un 0 si no es efectivo y un -1 si no le afecta
        """ 
        factor = self.factor(p)
        if factor == 1.5:
                return 1
        elif factor == 1:
                return 0
        else:
                return -1



#'''---------------------------------------Fire pokemon-----------------------------------------------'''




class FirePokemon(Pokemon):
    ''' Se define la clase que contiene a los pokemons de tipo fuego.
        Esta es una subclase de pokemon por lo que tiene todos los atributos de esta.

    Atributos
    ----------
            name: str
                Nombre del pokemon

            level: int
                Nivel del pokemon

            strength: int
                Fuerza con al que ataca

            defense: int
                Defensa que tiene. La defensa reduce el danho recibido

            total_hp: int
                Vida total del pokemon

            hp: int
                Vida puntual del pokemon

            agility: int
                Velocidad. Si un pokemon tiene mas velocidad que otro atacara antes

            pokemon_type: str
                Tipo que tiene: fuego, agua o planta

            temperature: float
                Booster para pokemons de tipo fuego. Potencia el ataque.

            
    -------

    Metodos

    -------
        embers(self, p:Pokemon):
            Realiza el ataque especial de tipo fuego. Se le aplica al ataque basico un multiplicador que es la temperatura. Devuelve el danho'
        
        fire_attack(self, p:Pokemon)->int:
            Realiza el ataque de tipo fuego. Devuelve el danho

        def effectiveness(self, p:Pokemon) -> int
            Devuelve un 1 si es efectivo, un 0 si no es efectivo y un -1 si no le afecta
        '''
    

    def __init__ (self, name:str, level:int, strength:int, defense:int, total_hp:int, hp:int, agility:int, temperature:float): 
         

         """Hereda los atributos de la clase Pokemon y anhadimos el atributo especial de los tipos fuego: temperature

        Atributos:
        ----------
            name: str
                Nombre del pokemon

            level: int
                Nivel del pokemon

            strength: int
                Fuerza con al que ataca

            defense: int
                Defensa que tiene. La defensa reduce el danho recibido

            total_hp: int
                Vida total del pokemon

            hp: int
                Vida puntual del pokemon

            agility: int
                Velocidad. Si un pokemon tiene mas velocidad que otro atacara antes

            pokemon_type: str
                Tipo que tiene: fuego, agua o planta

            temperature: float
                Aplica un boost en el ataque del pokemon
            -------
            Returns:
                None.
            """ 

         super().__init__(name, level, strength, defense, hp, total_hp, agility)
         self.pokemon_type = 'Fire'
         self.temperature = float(temperature)

#'''------------------------------------------Atributos-----------------------------------------'''
    @property 
    def temperature(self) -> float:
        return self._temperature
    @temperature.setter 
    def temperature(self, temperature:float)->None: 
        if isinstance(temperature, float) and temperature > 0:
            self._temperature = temperature
        else:
            raise ValueError("Temperature must be a non-negative float")

#'''------------------------------------------Metodos----------------------------------------------'''

    def fire_attack(self, p:Pokemon) -> int:
            """Realiza el ataque de tipo fuego. Devuelve el danho

            Atributos
            ----------
            self 

            p : Pokemon
             El pokemon contra el que peleas

            --------
            Returns: 
                damage : int
                    El maximo entre 1 y el ataque basico multiplicado por el factor
            """ 

            damage = max(1, (int(self.factor(p)*self.strength)) - p.defense)

            if damage > p.hp:
                damage = p.hp

            p.hp = p.hp - damage
            return damage


    def embers(self, p:Pokemon) -> int:
        
        """Realiza el ataque especial de tipo fuego. Se le aplica al ataque basico
        un multiplicador que es la temperatura. Devuelve el danho.

        Atributos
        ----------
        self 

        p : Pokemon
            El pokemon contra el que peleas
        --------
        Returns:
            damage : int
                el danho multiplicado por la temperatura menos la defensa del rival
        """ 

        damage = int(self.strength * self.temperature)

        if damage > p.hp:
            damage = p.hp

        p.hp = p.hp - damage    
        return damage

    def effectiveness(self, p:Pokemon) -> int:
            """Comprueba si es efectivo (1), si no es efectivo (0) o si no le afecta (-1)

            Atributos
            ----------
            self 

            p : Pokemon
                El pokemon contra el que peleas
            --------

            Returns:

                int
                    Devuelve un 1 si es efectivo, un 0 si no es efectivo y un -1 si no le afecta
        """ 

            factor = self.factor(p)
            if factor == 1.5:
                return 1
            elif factor == 1:
                return 0
            else:
                return -1





#'''---------------------------------------Grass pokemon----------------------------------------'''
class GrassPokemon(Pokemon):
    
    ''''Se define la clase que contiene a los pokemons de tipo planta' 
        Esta es una subclase de pokemon por lo que tiene todos los atributos de esta

    Atributos
    ----------
            name: str
                Nombre del pokemon

            level: int
                Nivel del pokemon

            strength: int
                Fuerza con al que ataca

            defense: int
                Defensa que tiene. La defensa reduce el danho recibido

            total_hp: int
                Vida total del pokemon

            hp: int
                Vida puntual del pokemon

            agility: int
                Velocidad. Si un pokemon tiene mas velocidad que otro atacara antes

            pokemon_type: str
                Tipo que tiene: fuego, agua o planta

            healing: float
                Factor de curacion para pokemons tipo planta

            
    -------

     Metodos
     -------
        heal(self) -> int
            Habilidad especial de tipo planta. Cura al usuario el porcentage que tenga en healing
        
        grass_attack(self, p:Pokemon) -> int
            Realiza el ataque de tipo planta. Devuelve el danho
        
        def effectiveness(self, p:Pokemon) -> int
            Devuelve un 1 si es efectivo, un 0 si no es efectivo y un -1 si no le afecta
        '''


    def __init__ (self, name:str, level:int, strength:int, defense:int, total_hp:int, hp:int, agility:int, healing:float):
           

            """Hereda los atributos de la clase Pokemon y anhadimos el atributo especial de los tipos planta: healing

            Atributos:
            ----------
            name: str
                Nombre del pokemon

            level: int
                Nivel del pokemon

            strength: int
                Fuerza con al que ataca

            defense: int
                Defensa que tiene. La defensa reduce el danho recibido

            total_hp: int
                Vida total del pokemon

            hp: int
                Vida puntual del pokemon

            agility: int
                Velocidad. Si un pokemon tiene mas velocidad que otro atacara antes

            pokemon_type: str
                Tipo que tiene: fuego, agua o planta

            healing: float
                cura al pokemon el un porcentaje, el que marque.
            -------
            Returns: 
                None.
            """ 

            super().__init__(name, level, strength, defense, hp, total_hp, agility)
            self.pokemon_type = 'Grass'
            self.healing = float(healing)

    #'''---------------------------------------------Atributos--------------------------------'''

    @property 
    def healing(self) -> float:
        return self._healing
    @healing.setter 
    def healing(self, healing:float):
        if isinstance(healing, float) and healing > 0:
            self._healing = healing
        else:
            raise ValueError("Healing must be a non-negative float")
    #'''----------------------------------------------Metodos----------------------------------'''

    def grass_attack(self, p:Pokemon) -> int:
            
            """Realiza el ataque de tipo planta. Devuelve el danho

            Atributos
            ----------
            self 

            p : Pokemon
                El pokemon contra el que peleas
            --------
            Returns: 
                damage : int
                   danho por el factor menos la defensa del rival
            """ 

            damage = max(1, (int(self.factor(p)*self.strength)) - p.defense)

            if damage > p.hp:
                damage = p.hp

            p.hp = p.hp - damage
            return damage





    def heal(self) -> int:
        """Habilidad especial de tipo planta. Cura al usuario el porcentage 
            que tenga en healing

        Atributos
        ----------
        self 

        p : Pokemon
            El pokemon contra el que peleas
        --------
        Returns:
            cura: int
                El numero que se le va a sumar a la vida actual del pokemon
        """ 
        cura =int(self.healing * self.hp)

        if cura > self.total_hp - self.hp:
            cura = self.total_hp - self.hp

        self.hp += cura
        return cura
    




    def effectiveness(self, p:Pokemon) -> int:
        """Comprueba si es efectivo (1), si no es efectivo (0) o si no le afecta (-1)

        Atributos
        ----------
        self 

        p : Pokemon
            El pokemon contra el que peleas
        --------
        Returns
            int
                Devuelve un 1 si es efectivo, un 0 si no es efectivo y un -1 si no le afecta
        """ 
        factor = self.factor(p)
        if factor == 1.5:
                return 1
        elif factor == 1:
                return 0
        else:
                return -1


