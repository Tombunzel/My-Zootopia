import requests


def fetch_data(animal_name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': 'a7X7Veruy6m06+jyPu0Iig==tBPyQCi8e9wMLc1s'})
    if response.status_code == requests.codes.ok:
        res_list = response.text
        return res_list
    else:
        print("Error:", response.status_code, response.text)
        quit()
