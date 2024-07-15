import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '83219472e40a286168e43356817f3f98'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN }
TRAINER_ID = 6478


def test_status_code():
    response = requests.get(url= f'{URL}/trainers',params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200


def test_part_code():
    response = requests.get('https://pokemonbattle.ru:/v2/trainers',params={'trainer_id' : TRAINER_ID})
    assert response.json()['trainer_name'] == 'Бубалех'