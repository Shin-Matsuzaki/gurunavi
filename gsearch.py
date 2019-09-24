import requests
import yaml


def main():
    with open('key.yaml') as file:
        API_KEY = yaml.load(file)['API_KEY']
    # API_KEY = 'acf4e7e5c6089e5a360d1ddf1fcb4f0c'
    url = f'https://api.gnavi.co.jp/RestSearchAPI/v3'
    payload = {'keyid': API_KEY,
               'freeword': 'ワイン',
               'hit_per_page': 5}

    response = requests.get(url, params=payload)
    shop_list = response.json()['rest']
    for shop in shop_list:
        print(f'{shop["name"]},{shop["url"]},{shop["access"]["line"]}{shop["access"]["station"]}')

    # shop = shop_list[1]["access"]["line"] + shop_list[1]["access"]["station"]
    # print(shop)


if __name__ == '__main__':
    main()
