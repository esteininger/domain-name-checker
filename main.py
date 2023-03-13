import requests

tlds = ['.ai', '.io', '.so', '.com', '.dev']

names = ["cactus", "lemur", "quail", "robin", "swan", "hawk", "mink", "lark", "rook", "kudu", "ibex"]


priv = ''
url = "https://api.jsonwhoisapi.com/v1/whois"


def check_domain(domain):
    headers = {
        'Authorization': priv,
        'cache-control': "no-cache"
    }

    querystring = {"identifier": domain}
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return response.json()


for name in names:
    for tld in tlds:
        to_check = name + tld
        details = check_domain(to_check)
        if not details['created']:
            print(to_check, " is available")
