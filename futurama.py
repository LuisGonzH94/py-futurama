import requests
url = "https://futurama-dam.web.app/api/characters"
response = requests.get(url)
data = response.json()

# Problema 1:
def characters(personajes):
    personajes = [character['name'] for character in personajes]
    return personajes



# Problema 2:

def charactersDead(status):
    data_items = data['hits']
    personajes = [character['name'] for character in data_items if character['status'] == status]
    return personajes 

# Problema 3:
def characterByGender(gender):
    data_items = data['hits']
    personajes = [character['name'] for character in data_items if character['gender'] == gender]
    return personajes
    

# print(characters(data['hits']))
# print(charactersDead('DEAD'))
# print(characterByGender('FEMALE'))