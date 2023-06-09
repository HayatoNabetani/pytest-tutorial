import requests

def sum_numbers(a,b):
    return (a + b) , a

def get_json_data(id):
    res = requests.get('http://aaaa', params={'id': id})
    res_json = res.json()
    return res_json

def get_user_names(user_ids):
    user_names = {}
    for id in user_ids:
        json_data = get_json_data(id)
        user_names[id] = json_data['name']
    return user_names

def user_name_validation(user_name):
    if user_name == None:
        raise ValueError('名前が設定されていません。')