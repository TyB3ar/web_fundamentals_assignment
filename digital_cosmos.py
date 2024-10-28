# Task 1: 
import requests
from bs4 import BeautifulSoup
import json


# Task 2: 
def fetch_planet_data():
    try:
        url = 'https://api.le-systeme-solaire.net/rest/bodies/' 
        response = requests.get(url) 
        planets = response.json()['bodies'] 
        
        planet_list = [] 
        
        for planet in planets:
            if planet['isPlanet']: 
                name = planet['englishName']  # gets planet English name
                mass = planet['mass']['massValue'] # gets planet mass
                orbit_period = planet['sideralOrbit'] # gets planet orbit period
                print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")    
                planet_list.append(
                    {"name" : name,
                     "mass" : mass,
                     "orbit" : orbit_period
                     }
                )          
            
        return planet_list 

    except Exception as e:
        print(f"Error: {e}") 
        
# Task 3:
def find_heaviest_planet(planets):
    try:
        heaviest_planet = max(planets, key=lambda x: x['mass'])
        return heaviest_planet['name'], heaviest_planet['mass']
            
    except Exception as e:
        print(f"Error: {e}")  


planets = fetch_planet_data() 

name, mass = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {name} with a mass of {mass} kg.")

