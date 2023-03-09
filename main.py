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
        soup = BeautifulSoup(response.text, "html.parser")

        if soup.select_one("h1").text.strip() == "Timeout":
            print("Session expired")
            break

        target_tr = soup.select_one(f'tr:has(td.tabelle1:-soup-contains("{MODCODE}"))')

        if target_tr:
            children = target_tr.select('*')
            print(f"Found: {children[1].text.strip()}")
            print(f"Semester: {children[2].text.strip()}")
            print(f"Grade: {children[3].text.strip()}")
            print(f"Perentage: {children[4].text.strip()}")
            print(f"State: {children[5].text.strip()}")
            print(f"ECTS: {children[6].text.strip()}")
            print(f"Notation: {children[7].text.strip()}")
            print(f"Try: {children[8].text.strip()}")
            print(f"Date: {children[9].text.strip()}")
            break
    except:
        pass
    time.sleep(5)

