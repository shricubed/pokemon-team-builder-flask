import requests

class Tea(object):
    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers.update({'User Agent': 'CMSC388J Spring 2021 Project 2'})
        self.base_url = 'https://pokeapi.co/api/v2'

    def get_pokemon_list(self):
        """
        Returns a list of pokemon names
        """
        pokemon = []
        resp = self.sess.get(f'{self.base_url}/pokemon?limit=1200')
        for poke_dict in resp.json()['results']:
            pokemon.append(poke_dict['name'])
        return pokemon
    
