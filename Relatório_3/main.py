from pokedex import Pokedex

pokedex = Pokedex("Pokedex", "Pokemons")


pokedex.get_pokemons_by_type(["Grass", "Poison"])

pokedex.get_pokemon_by_id(12)

pokedex.get_all_pokemons()

pokedex.get_pokemon_by_HP(50)
