import requests


def get_programming_languages(key):
    url = 'https://api.e-science.pl/api/azon/programminglanguages/'
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e


def get_research_centers(key):
    url = 'https://api.e-science.pl/api/azon/databases/pwr_research_centers/'
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e


def get_laboratories(key):
    url = 'https://api.e-science.pl/api/azon/databases/elaboratory/'
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e


def get_api(key):
    url = 'https://api.e-science.pl/api/azon/api/'
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e


def get_databases(key):
    url = 'https://api.e-science.pl/api/azon/databases/'
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e


def get_persons(key):
    url = 'https://api.e-science.pl/api/azon/persons/'
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e


def get_custom_url(url, key):
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e
