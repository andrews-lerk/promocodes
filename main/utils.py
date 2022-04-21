import os
from config.settings import PROMOCODES_STORAGE_DIR
import json
from json import JSONDecodeError
import random

SYMBOLS = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'


def generate_promocodes(amount: int, group: str):
    """ Generate promocodes and add to json file """
    data = load_to_dict()
    for _ in range(amount):
        promocode = generate()
        if group_exists(data=data, group=group):
            while True:
                if promocode_exists(data=data, promocode=promocode):
                    promocode = generate()
                else:
                    data[group].append(promocode)
                    break
        else:
            while True:
                if promocode_exists(data=data, promocode=promocode):
                    promocode = generate()
                else:
                    data[group] = list()
                    data[group].append(promocode)
                    break
    load_to_json_file(data)
    return print('DONE')


def check_for_exist_promocode(promocode: str):
    ''' Check promocode, if json don't have promocode or json is empty it return does not exists '''
    data = load_to_dict()
    if data == {}:
        return print('Код не существует')
    for i in data:
        if data[i].count(promocode) != 0:
            return print(f'Код существует группа = {i}')
    return print('Код не существует')


def group_exists(data, group):
    ''' Check if group exists return true '''
    if data.get(group) is None:
        return False
    else:
        return True


def promocode_exists(data, promocode):
    """ for all groups check, if promocode already exists return true """
    check = False
    for i in data:
        if data[i].count(promocode) != 0:
            check = True
            break
        else:
            continue
    return check


def generate():
    ''' Generate promocode '''
    promocode = str()
    for _ in range(7):
        promocode += random.choice(SYMBOLS)
    return promocode


def load_to_json_file(data):
    ''' load dict data to json file '''
    with open(PROMOCODES_STORAGE_DIR / 'promocodes.json', 'w', encoding='utf-8') as file:
        return json.dump(data, file)


def load_to_dict():
    """ try load data from json file to dict,
    if file not exists or file is empty - func generate it and return empty dict """
    try:
        with open(PROMOCODES_STORAGE_DIR / 'promocodes.json', 'r', encoding='utf-8') as file:
            return dict(json.load(file))
    except FileNotFoundError:
        if not os.path.exists(PROMOCODES_STORAGE_DIR):
            os.mkdir(PROMOCODES_STORAGE_DIR)
        with open(PROMOCODES_STORAGE_DIR / 'promocodes.json', 'w', encoding='utf-8') as file:
            return dict()
    except JSONDecodeError:
        return dict()
