import requests
import time
import sys
from bs4 import BeautifulSoup
import constants

url = constants.URL
cookies = constants.COOKIE

MODCODE = sys.argv[1] if len(sys.argv) > 1 else sys.exit("No module code given")

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
            td = target_tr.select('*')
            print(f"Found: {td[1].text.strip()}")
            print(f"Semester: {td[2].text.strip()}")
            print(f"Grade: {td[3].text.strip()}")
            print(f"Percentage: {td[4].text.strip()}")
            print(f"State: {td[5].text.strip()}")
            print(f"ECTS: {td[6].text.strip()}")
            print(f"Notation: {td[7].text.strip()}")
            print(f"Try: {td[8].text.strip()}")
            print(f"Date: {td[9].text.strip()}")
            break
    except:
        pass
    time.sleep(5)

