import requests
import time
import sys
from bs4 import BeautifulSoup
import constants

url = constants.url
cookies = constants.cookies

MODCODE = sys.argv[1]
session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"})

while True:
    try:
        response = session.get(url, cookies=cookies)

        #save html file
        with open("html.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        soup = BeautifulSoup(response.text, "html.parser")

        target_tr = soup.select_one(f'tr:has(td.tabelle1:-soup-contains("{MODCODE}"))')

        if target_tr:
            print("Found")
            children = target_tr.select('*')
            for child in children:
                print(child.text.strip())
            break
    except:
        pass
    time.sleep(5)

