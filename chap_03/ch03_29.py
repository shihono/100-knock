# -*- coding : utf-8 -*-
import requests
from chap_03 import ch03_25
"29. 国旗画像のURLを取得する"


def main():
    infobox = ch03_25.main_25()
    payload = {
        'format': 'json',
        'action': 'query',
        'titles': 'File:'+ infobox['国旗画像'],
        'prop': 'imageinfo',
        'iiprop': 'url'
    }
    url = "https://ja.wikipedia.org/w/api.php"
    r = requests.get(url=url, params=payload)
    print(r.url)
    print(r.json()['query']['pages']['-1']['imageinfo'][0]['url'])


if __name__ == '__main__':
    main()