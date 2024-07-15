import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '83219472e40a286168e43356817f3f98'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN }
body_registration = {
    "trainer_token": TOKEN,
    "email": "elenatsoy7@mail.ru",
    "password": "Kirililena15"
}
body_confirmation= {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Дино",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "43509",
    "name": "бобби",
    "photo_id": 2
}

body_pokebol = {
    "pokemon_id": "43509"
}


'''response = requests.post(url=f'{URL}/trainers/reg', headers= HEADER, json=body_registration )
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers=HEADER, json=body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)'''

'''"id":"43509"'''
'''message = response_create.json() ['id']
print(message)'''

'''response_name = requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_name)
print(response_name.text)'''

response_pokebol = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokebol)
print(response_pokebol.text)
