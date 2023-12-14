import requests

def get_name_country(name):
    url = "https://api.nationalize.io/?name={}".format(name)
    response = requests.get(url)
    data = response.json()
    print(data)

get_name_country("ahmad")

def get_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    data = response.json()
    print(data[20])

get_countries()