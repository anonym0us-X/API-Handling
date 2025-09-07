# How to connect to an API using python

import requests

base_url = "https://pokeapi.co/api/v2/"

def getinfo(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

mypok = "pikachu"
poke_info = getinfo(mypok)
if poke_info:
    print(f"Name : {poke_info['name'].upper()}")
    print(f"ID : {poke_info["id"]} \nHeight : {poke_info["height"]} \nWeight : {poke_info["weight"]}")