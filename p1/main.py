#Importamos las dos clases creadas anteriormente, la libreria sys, y la
#libreria pandas para hacer el analisis de despues

import sys
from pokemon import *
from trainer import *
import pandas as pd



#Creamos funciones para el combate

def inicio_batalla(p1:Pokemon, p2:Pokemon)->Pokemon:
        """ Devuelve el pokemon que ataca primero, por tanto el pokemon atacante,
            y tambien define el pokemon que recibe ese ataque .
            Elige el pokemon que ataca primero en base a la verlocidad 
            (agility) del pokemon.

            Atributos:
            ----------
            p1: Pokemon
                Es el pokemon del entrenador 1
            p2: Pokemon
                Es el pokemon del entrenador 2
            -------
            Return:
                Atacante: Pokemon
                    pokemon que lanza el ataque 
                Defensor: Pokemon
                    pokemon que recibe el ataque
                    
        """ 
        if p1.agility >= p2.agility:
            atacante = p1
            defensor = p2
        else:
            atacante = p2
            defensor = p1

        return atacante, defensor



def ronda(atacante:Pokemon, defensor:Pokemon, round_counter:int, primaria:int, information:list):
    """ Acciones que se toman durante la ronda
        Durante el combate, va ronda por ronda ejecutando 
        donde un pokemon ataca al otro.
        
        Parametros
        ----------
            atacante: Pokemon
                El pokemon que ataca
            defensor: Pokemon
                El pokemon que recibe el ataque
            round: int
                El numero de la ronda
            primaria: int
                Contador para el dataframe
            information: list
                variable auxiliar para el analisis de datos
        -------
        Return:
            None
            Lo unico anhade una lista a informacion, donde queda registrado datos 
            de la ronda para analizar mas adelante
        """ 
    if round_counter%2 == 0:
        damage = atacante.basic_attack(defensor)
        ataque_tipo = 0
        cura = 0

        print(f'{atacante.name} uses a basic_attack on {defensor.name}! (Damage: {damage} HP: {defensor.hp})')

    else:
        if atacante.pokemon_type == 'Fire':
            ataque = 'Fire attack'
            damage1 = atacante.fire_attack(defensor)
            damage2 = 0
            damage = 0
            cura = 0

            print(f'{atacante.name} uses a {ataque} on {defensor.name}! (Damage: {damage1} HP: {defensor.hp})')
            
            if not(defensor.is_debilitated()):
                damage2 = atacante.embers(defensor)
                print(f'{atacante.name} uses embers on {defensor.name}! (Damage: {damage2} HP: {defensor.hp})')

            ataque_tipo = damage1 + damage2

        elif atacante.pokemon_type == 'Grass':
            ataque = 'Grass attack'
            ataque_tipo = atacante.grass_attack(defensor)
            damage = 0

            print(f'{atacante.name} uses a {ataque} on {defensor.name}! (Damage: {ataque_tipo} HP: {defensor.hp})')
            cura = atacante.heal()

            print(f'{atacante.name} is healing! (Healing: +{cura} HP: {atacante.hp})')
            

        else:
            ataque = 'Water atack'
            ataque_tipo = atacante.water_attack(defensor)
            damage = 0
            cura = 0

            print(f'{atacante.name} uses a {ataque} on {defensor.name}! (Damage: {ataque_tipo} HP: {defensor.hp})')
            
            
        
    danho_total = damage + ataque_tipo

    #Guardamos los datos de esta ronda

    values = [primaria, atacante.name, atacante.pokemon_type,  defensor.name, defensor.pokemon_type, damage, cura, ataque_tipo, danho_total]
    information.append(values)

    
                  


#-------------------------------------------x---------------------------------------

            
class PokemonSimulator:
    """A class that simulates Pokemon trainers and their Pokemon."""

    def create_trainer_and_pokemons(self, text: str):
        """
        Creates a trainer and their pokemons from a given text input.

        Parameters:
        text (str): Multiline text where the first line is the trainer's name and subsequent lines contain Pokemon details.
        
        Returns:
        None: The function is currently set up to return None. Intended to return a Trainer instance in future development.
        """

        lines = text.split("\n")
        trainer_name = lines[0]
        pokemons = []

        # Iterating over each pokemon line in the input
        for line in lines[1:]:
            parts = line.split(' (')
            pokemon_name = parts[0] # Extracting the pokemon's name
            details = parts[1].strip(')').split(', ')  # Splitting other attributes
            # Extracting and converting each attribute
            pokemon_type = details[0].split(': ')[1]
            level = int(details[1].split(': ')[1])
            strength = int(details[2].split(': ')[1])
            defense = int(details[3].split(': ')[1])
            hp = int(details[4].split(': ')[1])
            total_hp = hp # Setting total_hp equal to the initial hp
            agility = int(details[5].split(': ')[1])
            

            # Creating pokemons based on their type
            if pokemon_type == 'Fire':
                temperature = float(details[6].split(': ')[1])
                # TODO: Implement creation of a FirePokemon
                print ("TODO: Crear un FirePokemon - ", end="")

                pokemon_creado=FirePokemon(pokemon_name, level, strength, defense, total_hp,hp,agility,temperature)
                
                # Printing the attributes for now
                print (f"name: {pokemon_name}, level: {level}, strength: {strength}, defense: {defense}, hp: {hp}, total_hp: {total_hp}, agility: {agility}, temperature: {temperature} ")



            elif pokemon_type == 'Grass':
                # TODO: Implement creation of a GrassPokemon
                healing = float(details[6].split(': ')[1])
                # Printing the attributes for now
                print ("TODO: Crear un GrassPokemon - ", end="")
                print (f"name: {pokemon_name},  level: {level}, strength: {strength}, defense: {defense}, hp: {hp}, total_hp: {total_hp}, agility: {agility}, healing: {healing} ")

                pokemon_creado = GrassPokemon(pokemon_name, level, strength, defense, total_hp,hp,agility,healing)


            elif pokemon_type == 'Water':
                surge_mode = False
                # TODO: Implement creation of a WaterPokemon
                print ("TODO: Crear un WaterPokemon - ", end="")
                # Printing the attributes for now
                print (f"name: {pokemon_name}, level: {level}, strength: {strength}, defense: {defense}, hp: {hp}, total_hp: {total_hp}, agility: {agility}, surge_mode: {surge_mode} ")

                pokemon_creado=WaterPokemon(pokemon_name, level, strength, defense, total_hp,hp,agility,surge_mode)


            else: 
                raise ValueError(f"Invalid Pokemon type: {pokemon_type}")
            
            pokemons.append(pokemon_creado)
        trainer = Trainer(trainer_name, pokemons)




        # Reminder to implement the instance creation of Trainer
        print (f"TODO: Crear instancia de Trainer con nombre {trainer_name} y su lista de pokemon {pokemons} (primero deberas anadir los Pokemon creados a esta lista)\n\n")
        return trainer

    def parse_file(self, text: str):
        """
        Parses the given text to create trainers and their pokemons.

        Parameters:
        text (str): The full text to be parsed, representing two trainers and their Pokemon.

        Returns:
        None: Currently does not return anything. Intended to return a list of Trainer instances in future development.
        """

        info_trainer_1, info_trainer_2 = text.strip().split("\n\n")

        trainer1 = self.create_trainer_and_pokemons(info_trainer_1)
        trainer2 = self.create_trainer_and_pokemons(info_trainer_2)

        return trainer1, trainer2



def main():

    """
    The main function that reads from a file and starts the simulation.
    """

    with open(sys.argv[1]) as f:
        pokemon_text = f.read()
        simulator = PokemonSimulator()
        trainer1, trainer2 = simulator.parse_file(pokemon_text)
        print ("""TODO: Implement the rest of the practice from here. Define classes and functions and
        maintain the code structured, respecting the object-oriented programming paradigm""")

        #Escogemos el pokemon que saldra a pelear de cada entrenador y definimos unas variables
        round_counter, contador_real, primaria, information = 1, 1, 0, []

        p1 = trainer1.select_first_pokemon()
        p2 = trainer2.select_first_pokemon()

        #p1 sera el primer pokemon del entrenador 1 y p2 del entrenador 2

        #'''----------------------------------------------------------------------------------------------------------------------------------------------'''


        print(f'''
        =================================
        Battle between: {trainer1.name} vs {trainer2.name} begins!
        {trainer1.name} chooses {p1.name}
        {trainer2.name} chooses {p2.name}
        =================================
        ''')
        
        #'''----------------------------------------------------------------------------------------------------------------------------------------------'''

    #Empezamos el combate

    while trainer1.all_debilitated() == False and trainer2.all_debilitated() == False:

        print('')
        print(f'Round combat: {contador_real}')
        print('')

        #Comprobamos si hay algun pokemon debilitado, y si lo hay, colocamos al siguiente pokemon

        if p1.is_debilitated() == True:
        
            round_counter = 1
            anterior = p1.name
            p1 = trainer1.select_next_pokemon(p2)

            print(f'How {anterior} is debilitated, {trainer1.name} chooses {p1.name}\n')

        elif p2.is_debilitated() == True:

            round_counter = 1
            anterior = p2.name
            p2 = trainer2.select_next_pokemon(p1)

            print(f'How {anterior} is debilitated, {trainer2.name} chooses {p2.name}\n')

    
        #Definimos atacante y defensor
            
        atacante, defensor = inicio_batalla(p1, p2)

        print(f'Pokemon round {round_counter} starts.\nFighter1: {atacante} \nFighter2: {defensor} ')


        #Realiza los ataques el primer pokemon, y si el que recibe no se debilita ataca el segundo

        ronda(atacante, defensor, round_counter, primaria, information)
        primaria += 1

        if defensor.is_debilitated() == True:
            print(f'{defensor.name} is debilitated')
            print('')

        #Ataca el segundo (si no muere el defensor)
        else:
            atacante, defensor = defensor, atacante

            ronda(atacante, defensor, round_counter, primaria, information)
            primaria += 1
            if defensor.is_debilitated() == True:
                    print(f'{defensor.name} is debilitated')
            print('')
        round_counter += 1
        contador_real += 1
        
    #Se repite el bucle hasta que mueran todos los pokemons de un entrenador
        
    #Comprobamos que entrenador tiene todos los pokemons debilitados
                    
    if trainer1.all_debilitated() == True:
        winner = trainer2
    else:
        winner = trainer1
    
    print(f'''
            =================================
            End of the Battle: {winner.name} wins!
            ================================= 
''')

    
    print('''

Combat stats:

          
''')
    
    #Definimos un dataframe, junto a una variable contador, para analizar despues 
    #el danho causado y mas datos


    data = pd.DataFrame(information, columns = ['Llave_primaria', 'Atacante', 'Tipo_atacante', 'Defensor', 'Tipo_defensor', 'Danho', 'Curacion', 'Ataque_tipo', 'Danho_total'])
    print(data)

    print('''

    ''')
    
    #Creamos y mostramos por pantalla las estadisticas del combate


    #Danho causado por cada pokemon individualmente
    print('Danho causado por cada pokemon individualmente\n')

    group_col = "Atacante"
    target_col = 'Danho_total'
    data_damage_pk = data.groupby(group_col).agg({target_col :["mean","std"]}).round(decimals=2)


    print(data_damage_pk)
    print('''

    ''')
        
    #Danho causado por cada tipo
    print('Danho causado por cada tipo\n')

    group_col = "Tipo_atacante"
    target_col = 'Danho_total'
    data_damage_type = data.groupby(group_col).agg({target_col :["mean","std"]}).round(decimals=2)

    print(data_damage_type)
    print('''

    ''')

    #Vida recuperada por cada pokemon
    print('Vida recuperada por cada pokemon\n')


    group_col = "Atacante"
    target_col = "Curacion"
    data_heal_pk = data.groupby(group_col).agg({target_col :["mean","std"]}).round(decimals=2)

    print(data_heal_pk)
    print('''

    ''')

    #Vida recuperada por cada tipo
    print('Vida recuperada por cada tipo\n')


    group_col = "Tipo_atacante"
    target_col = "Curacion"
    data_heal_type = data.groupby(group_col).agg({target_col :["mean","std"]}).round(decimals=2)

    print(data_heal_type)
    print('''

    ''')

    #Danho causado de un tipo al resto
    print('Danho causado de un tipo al resto\n')
    
    group_col =["Tipo_atacante","Tipo_defensor"]
    target_col = 'Danho_total'
    data_type_damage = data.groupby(group_col).agg({target_col :["mean","std"]}).round(decimals=2)
    print(data_type_damage)    


    #si en la desviacion tipica (std) devuelve NaN, 
    #es porque solo se registra un dato y por tanto no hay desviacion tipica
    #Se puede modificar para que ponga 0 para que ponga 0 se gasta memoria
    #en vano ya que se entiende bien que ponga NaN, ya que significa que no hay
    
if __name__ == '__main__':
    main()
