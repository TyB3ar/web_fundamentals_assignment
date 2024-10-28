# Task 1: 
import requests
import json 

# Task 2: 
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu") 

json_data = response.text 

pikachu_data = json.loads(json_data)

print(pikachu_data["name"])

print(pikachu_data["abilities"])


# Task 3:
def fetch_pokemon_data(pokemon_name):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}") 
        
        json_data = response.text 
        
        pokemon_data = json.loads(json_data) 
        
        print(f"\nName: {pokemon_data["name"]}\nAbilities: {pokemon_data["abilities"]}\nWeight: {pokemon_data["weight"]}")
        
    except Exception as e:
        print(f"Error: {e}")


def calculate_average_weight(pokemon_list):
    try:
        pokemon_weight = [] # empty list to add weight values to 
        
        for pokemon_name in pokemon_list:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}") 
        
            json_data = response.text 
        
            pokemon_data = json.loads(json_data)
            
            pokemon_weight.append(pokemon_data["weight"]) 
            
        average_weight = sum(pokemon_weight) / len(pokemon_weight) 
        
        print(f"\nAverage weight: {round(average_weight, 2)}") 
           
    except Exception as e:
        print(f"Error: {e}")

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

fetch_pokemon_data("pikachu") 

fetch_pokemon_data("bulbasaur")

fetch_pokemon_data("charmander")

calculate_average_weight(pokemon_names) 