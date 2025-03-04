# test_pokemon.py
import unittest
from pokemon import Pokemon, WaterPokemon, FirePokemon, GrassPokemon

class TestPokemon(unittest.TestCase):
    """
    Test class for Pokemon battle simulation.
    This class tests various functionalities of different types of Pokemon and their interactions.
    """

    def setUp(self):
        """
        Set up the testing environment before each test.
        This method is called before every individual test method. It initializes three types of Pokemon.
        """
        
        self.squirtle = WaterPokemon(name="Squirtle", level=5, strength=60, defense=25, 
                                     hp=75, total_hp=75, agility=10, surge_mode=False)
        self.bulbasaur = GrassPokemon(name="Bulbasaur",  level=5, strength=60, defense=25, 
                                      hp=75, total_hp=75, agility=10, healing=0.2)
        self.charmander = FirePokemon(name="Charmander", level=5, strength=60, defense=25, 
                                      hp=75, total_hp=75, agility=10, temperature=0.2)


    ###########################################################################
    #               Unit test cases for the generic methods
    ###########################################################################

    def test_is_debilitated(self):
        """
        Test the is_debilitated method of the Pokemon class.
        It should return True if a Pokemon's health points (hp) are equal to 0.
        """
        self.squirtle.hp = 0
        self.assertTrue(self.squirtle.is_debilitated(), msg="Pokemon with 0 HP should be debilitated.")

    def test_basic_attack(self):
        """
        Test the basic attack functionality.
        It checks if the HP of the opponent decreases correctly after a basic attack.
        """
        self.squirtle.basic_attack(self.charmander)
        self.assertEqual(self.charmander.hp, 40)

        self.charmander.basic_attack(self.squirtle)
        self.assertEqual(self.squirtle.hp, 40)

        self.bulbasaur.basic_attack(self.charmander)
        self.assertEqual(self.charmander.hp, 5)

    def test_basic_attack_non_below_zero(self):
        """
        Test that a basic attack doesn't reduce the opponent's HP below zero.
        """
        weak_opponent = GrassPokemon(name="WeakBulbasaur", level=5, strength=2, defense=2, 
                                     hp=5, total_hp=5, agility=5, healing=0.2)
        self.squirtle.basic_attack(weak_opponent)
        self.assertEqual(weak_opponent.hp, 0, msg="Opponent's HP should not go below zero.")

    def test_basic_attack_one_damage(self):
        """
        Test that a basic attack deals at least one damage.
        Even if the opponent's defense is higher than the attacker's strength.
        """
        tanky_opponent = GrassPokemon("TankyBulbasaur", level=5, strength=1000, defense=1000, 
                                      hp=1000, total_hp=1000, agility=1000, healing=0.2)
        self.squirtle.basic_attack(tanky_opponent)
        self.assertEqual(tanky_opponent.hp, 999, msg="Basic attack should deal at least 1 damage.")

    def test_effectiveness(self):
        """
        Test the effectiveness method for different type interactions.
        Checks if the effectiveness returns the correct multipliers.
        """

        self.assertEqual(self.squirtle.effectiveness(self.charmander), 1)
        self.assertEqual(self.charmander.effectiveness(self.bulbasaur), 1)
        self.assertEqual(self.bulbasaur.effectiveness(self.squirtle), 1)

        self.assertEqual(self.charmander.effectiveness(self.squirtle), -1)
        self.assertEqual(self.bulbasaur.effectiveness(self.charmander), -1)
        self.assertEqual(self.squirtle.effectiveness(self.bulbasaur), -1)

        self.assertEqual(self.charmander.effectiveness(FirePokemon("Charmander", level=5, strength=60, defense=25, 
                                                                   hp=75, total_hp=75, agility=15, temperature=0.2)), 0)
        self.assertEqual(self.bulbasaur.effectiveness(GrassPokemon("Bulbasaur",  level=5, strength=60, defense=25, 
                                                                   hp=75, total_hp=75, agility=5, healing=0.2)), 0)
        self.assertEqual(self.squirtle.effectiveness(WaterPokemon("Squirtle", level=5, strength=60, defense=25, 
                                                                  hp=75, total_hp=75, agility=10, surge_mode=False)), 0)


    def test_fire_attack_against_water(self):
        """
        Test the fire attack method when used against a Water-type Pokemon.
        The expected behavior is that the Water-type Pokemon's HP decreases correctly,
        considering the type disadvantage of Fire against Water.
        """
        expected_final_hp = 70
        self.charmander.fire_attack(self.squirtle)
        self.assertEqual(self.squirtle.hp, expected_final_hp, msg="Fire attack against Water-type should reduce HP to the expected amount considering type disadvantages.")

    def test_fire_attack_against_fire(self):
        """
        Test the fire attack method when used against another Fire-type Pokemon.
        The expected behavior is that the Fire-type Pokemon's HP decreases correctly,
        considering the type neutrality of Fire against Fire.
        """
        expected_final_hp = 40
        opponent = FirePokemon(name="Charmander2", level=5, strength=60, defense=25, 
                               hp=75, total_hp=75, agility=15, temperature=0.2)
        self.charmander.fire_attack(opponent)
        self.assertEqual(opponent.hp, expected_final_hp, msg="Fire attack against Fire-type should reduce HP considering type neutrality.")

    def test_fire_attack_against_grass(self):
        """
        Test the fire attack method when used against a Grass-type Pokemon.
        The expected behavior is that the Grass-type Pokemon's HP decreases correctly,
        considering the type advantage of Fire against Grass.
        """
        expected_final_hp = 10
        opponent = GrassPokemon(name="Bulbasaur2", level=5, strength=60, defense=25, 
                                hp=75, total_hp=75, agility=15, healing=0.2)
        self.charmander.fire_attack(opponent)
        self.assertEqual(opponent.hp, expected_final_hp, msg="Fire attack against Grass-type should reduce HP considering type advantage.")

    def test_fire_attack_non_below_zero(self):
        """
        Test the fire attack method to ensure it does not reduce the opponent's HP below zero.
        No Pokemon's HP should go negative.
        """
        expected_final_hp = 0
        opponent = GrassPokemon(name="Bulbasaur2", level=5, strength=2, defense=2, 
                                hp=5, total_hp=5, agility=15, healing=0.2)
        self.charmander.fire_attack(opponent)
        self.assertEqual(opponent.hp, expected_final_hp, msg="Fire attack should not reduce opponent's HP below zero.")

    def test_water_attack_against_grass(self):
        """
        Test the water attack method when used against a Grass-type Pokemon.
        The expected behavior is that the Grass-type Pokemon's HP decreases correctly,
        considering the type disadvantage of Water against Grass.
        """
        expected_final_hp = 70
        self.squirtle.water_attack(self.bulbasaur)
        self.assertEqual(self.bulbasaur.hp, expected_final_hp, msg="Water attack against Grass-type should reduce HP considering type disadvantages.")

    def test_water_attack_against_grass(self):
        """
        Test the water attack method when used against a Grass-type Pokemon.
        The expected behavior is that the Grass-type Pokemon's HP decreases correctly,
        considering the type disadvantage of Water against Grass.
        """
        expected_final_hp = 70
        self.squirtle.water_attack(self.bulbasaur)
        self.assertEqual(self.bulbasaur.hp, expected_final_hp, msg="Water attack against Grass-type should reduce HP considering type disadvantages.")

    def test_water_attack_against_water(self):
        """
        Test the water attack method when used against another Water-type Pokemon.
        The expected behavior is that the Water-type Pokemon's HP decreases correctly,
        considering the type neutrality of Water against Water.
        """
        expected_final_hp = 40
        opponent = WaterPokemon(name="Squirtle2", level=5, strength=60, defense=25, 
                                hp=75, total_hp=75, agility=15, surge_mode=False)
        self.squirtle.water_attack(opponent)
        self.assertEqual(opponent.hp, expected_final_hp, msg="Water attack against Water-type should reduce HP considering type neutrality.")

    def test_water_attack_against_fire(self):
        """
        Test the water attack method when used against a Fire-type Pokemon.
        The expected behavior is that the Fire-type Pokemon's HP decreases correctly,
        considering the type advantage of Water against Fire.
        """
        expected_final_hp = 10
        opponent = FirePokemon(name="Charmander2", level=5, strength=60, defense=25, 
                               hp=75, total_hp=75, agility=15, temperature=0.2)
        self.squirtle.water_attack(opponent)
        self.assertEqual(opponent.hp, expected_final_hp, msg="Water attack against Fire-type should reduce HP considering type advantage.")

    def test_water_attack_non_below_zero(self):
        """
        Test the water attack method to ensure it does not reduce the opponent's HP below zero.
        No Pokemon's HP should go negative.
        """
        expected_final_hp = 0
        weak_opponent = FirePokemon(name="Charmander2", level=5, strength=2, defense=2, 
                                    hp=5, total_hp=5, agility=15, temperature=0.2)
        self.squirtle.water_attack(weak_opponent)
        self.assertEqual(weak_opponent.hp, expected_final_hp, msg="Water attack should not reduce opponent's HP below zero.")

    def test_grass_attack_agains_fire(self):
        """
        Test the grass attack method when used against a Fire-type Pokemon.
        The expected behavior is that the Fire-type Pokemon's HP decreases correctly,
        considering the type disadvantage of Grass against Fire.
        """
        expected_final_hp = 70
        self.bulbasaur.grass_attack(self.charmander)
        self.assertEqual(self.charmander.hp, expected_final_hp, msg="Grass attack against Fire-type should reduce HP considering type disadvantages.")


    def test_grass_attack_against_grass(self):
        """
        Test the grass attack method when used against another Grass-type Pokemon.
        The expected behavior is that the Grass-type Pokemon's HP decreases correctly,
        considering the type neutrality of Grass against Grass.
        """

        expected_final_hp = 40
        opponent = GrassPokemon(name="Bulbasaur2", level=5, strength=60, defense=25, 
                                hp=75, total_hp=75, agility=15, healing=0.2)
        self.bulbasaur.grass_attack(opponent)
        self.assertEqual(opponent.hp, expected_final_hp, msg="Grass attack against Grass-type should reduce HP considering type neutrality.")

    def test_grass_attack_against_water(self):
        """
        Test the grass attack method when used against a Water-type Pokemon.
        The expected behavior is that the Water-type Pokemon's HP decreases correctly,
        considering the type advantage of Grass against Water.
        """
        expected_final_hp = 10
        opponent = WaterPokemon(name="Squirtle2", level=5, strength=60, defense=25, 
                                hp=75, total_hp=75, agility=15, surge_mode=False)
        self.bulbasaur.grass_attack(opponent)
        self.assertEqual(opponent.hp, expected_final_hp, msg="Grass attack against Water-type should reduce HP considering type advantage.")

    def test_grass_attack_non_below_zero(self):
        """
        Test the grass attack method to ensure it does not reduce the opponent's HP below zero.
        No Pokemon's HP should go negative.
        """
        expected_final_hp = 0
        weak_opponent = WaterPokemon(name="Squirtle2", level=5, strength=2, defense=2, 
                                hp=5, total_hp=5, agility=15, surge_mode=False)
        self.bulbasaur.grass_attack(weak_opponent)
        self.assertEqual(weak_opponent.hp, expected_final_hp, msg="Grass attack should not reduce opponent's HP below zero.")

    ###########################################################################
    # Unit test cases for the Fire-type Pokemon special ability embers
    ###########################################################################

    def test_embers(self):
        """
        Test the FirePokemon's embers attack.
        It should correctly reduce the HP of the opponent and respect type effectiveness.
        """
        expected_final_hp = 63
        opponent = GrassPokemon(name="Bulbasaur2", level=5, strength=60, defense=25, 
                                hp=75, total_hp=75, agility=15, healing=0.2)
        self.charmander.embers(opponent)
        self.assertEqual(opponent.hp, expected_final_hp)

    def test_embers_non_below_zero(self):
        """
        Test the FirePokemon's embers attack to ensure it does not reduce the opponent's HP below zero.
        No Pokemon's HP should go negative.
        """
        expected_final_hp = 0
        weak_opponent = GrassPokemon("Bulbasaur2", level=5, strength=2, defense=2, hp=5, 
                                     total_hp=5, agility=15, healing=0.2)
        self.charmander.embers(weak_opponent)
        self.assertEqual(weak_opponent.hp, expected_final_hp, msg="Embers attack should not reduce opponent's HP below zero.")

    ###########################################################################
    #  Unit test cases for the Water Pokemon special ability surge_mode
    ###########################################################################

    def test_water_pokemon_check_surge_activation(self):
        """
        Test the WaterPokemon's method to check surge activation.
        Surge mode should activate when the Pokemon's HP is less than half of the total.
        """
        # Damage the Pokemon to just above half HP and check surge mode activation
        self.squirtle.hp = (self.squirtle.hp // 2) + 1
        value = self.squirtle.check_surge_mode()
        self.assertFalse(value, msg="Surge mode should not activate above half HP.")

        # Further damage the Pokemon to below half HP and check surge mode activation
        self.squirtle.hp -= 2
        value = self.squirtle.check_surge_mode()
        self.assertTrue(value, msg="Surge mode should activate below half HP.")

    def test_water_pokemon_attack_surge_mode_against_water(self):
        """
        Test the WaterPokemon's water attack in surge mode against another Water-type Pokemon.
        Surge mode should increase the attack's effectiveness.
        """
        expected_final_hp = 34
        opponent = WaterPokemon(name="Squirtle2", level=5, strength=60, defense=25, 
                                hp=75, total_hp=75, agility=15, surge_mode=False)
        self.squirtle.hp = (self.squirtle.hp // 2) -1
        self.squirtle.water_attack(opponent)
        self.assertEqual(opponent.hp, expected_final_hp, msg="Surge mode water attack against Water-type should reduce HP considering increased effectiveness.")

    def test_water_pokemon_attack_surge_mode_against_grass(self):
        """
        Test the WaterPokemon's water attack in surge mode against a Grass-type Pokemon.
        Surge mode should increase the attack's effectiveness even with type disadvantage.
        """
        expected_final_hp = 64
        opponent = GrassPokemon(name="Bulbasaur2", level=5, strength=60, defense=25, 
                                hp=75, total_hp=75, agility=15, healing=0.2)
        self.squirtle.hp = (self.squirtle.hp // 2) -1
        self.squirtle.water_attack(opponent)
        self.assertEqual(opponent.hp, expected_final_hp, msg="Surge mode water attack against Grass-type should reduce HP considering increased effectiveness and type disadvantage.")


    def test_water_pokemon_attack_surge_mode_against_fire(self):
        """
        Test the WaterPokemon's water attack in surge mode against a Fire-type Pokemon.
        Surge mode should increase the attack's effectiveness, especially with type advantage.
        """
        expected_final_hp = 4
        opponent = FirePokemon(name="Charmander2", level=5, strength=60, defense=25, 
                               hp=75, total_hp=75, agility=15, temperature=0.2)
        self.squirtle.hp = (self.squirtle.hp // 2) -1
        self.squirtle.water_attack(opponent)
        self.assertEqual(opponent.hp, expected_final_hp, msg="Surge mode water attack against Fire-type should reduce HP considering increased effectiveness and type advantage.")

    ###########################################################################
    # Unit test cases for the Grass Pokemon special ability heal()
    ###########################################################################

    def test_grass_pokemon_heal_normal(self):
        """
        Test the GrassPokemon's heal method under normal conditions.
        The Pokemon should heal a portion of its HP, but not exceed its total HP.
        """
        initial_hp = self.bulbasaur.hp
        self.bulbasaur.hp -= 20  # Damage the Pokemon.
        self.bulbasaur.heal()  # Attempt to heal.
        self.assertTrue(self.bulbasaur.hp == 66,  msg="GrassPokemon should heal correctly without exceeding total HP.")

    def test_grass_pokemon_heal_over_maximum(self):
        """
        Test the GrassPokemon's heal method to ensure it doesn't heal over the maximum HP.
        The Pokemon's HP after healing should not exceed its total HP.
        """
        initial_hp = self.bulbasaur.hp
        self.bulbasaur.hp -= 5  # Damage the Pokemon.
        self.bulbasaur.heal()  # Attempt to heal.
        self.assertTrue(self.bulbasaur.hp == initial_hp, msg="GrassPokemon's HP after healing should not exceed total HP.")


if __name__ == '__main__':
    unittest.main(verbosity=2)