import requests


def get_entries_page(key, page=0):
    url = 'https://api.e-science.pl/api/azon/entry/filter/?limit=100&offset=0' + \
        str(page) + '00'
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e


def get_author_entries(key, pk):
    url = 'https://api.e-science.pl/api/azon/authors/entries/' + str(pk) + '/'
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e


def get_all_entries(key):
    url = 'https://api.e-science.pl/api/azon/entry/all/?limit=100&offset=0'
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e


def get_all_entries_short(key):
    url = 'https://api.e-science.pl/api/azon/entry/all/short/'
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e
