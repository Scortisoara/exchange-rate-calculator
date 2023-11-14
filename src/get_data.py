import requests

def request_cnb_data():
    URL = "https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    response = requests.get(URL)
    return response.text

def get_cnb_data():
    data = request_cnb_data()
    lines = data.splitlines()

    date = lines[0].split()[0]

    result = []

    for line in lines[2:]:
        currency = line.split("|")[3]
        rate = line.split("|")[4]
        result.append({"date": date, "currency": currency, "rate": rate})

    return result
