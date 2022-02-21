import requests

def superh():
    url = ' https://superheroapi.com/api/2619421814940190/search/name'
    params = {"mind": "intelligence"}
    response = requests.get(url, params=params, timeout=5)
    # print(response)

def intelligence_heroes(heroes):
    intelligence = {}
    for name in heroes:
        intelligence_heroe = superh()
        intelligence[name] = str(intelligence_heroe)
    max_value = max(intelligence, key=intelligence.get)
    print(f'Самый умный супергерой: {max_value}')

heroes = ['Hulk', 'Captain America', 'Thanos']
print(intelligence_heroes(heroes))




