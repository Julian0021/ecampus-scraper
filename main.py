import requests
import time
import sys
from bs4 import BeautifulSoup
import login

cookies, asi_token = login.get_login()
MODCODE = sys.argv[1] if len(sys.argv) > 1 else sys.exit("No module code given")

while True:
    try:
        url = f"https://ecampus.thm.de/qisstud/rds?state=notenspiegelStudent&next=list.vm&nextdir=qispos/notenspiegel/student&createInfos=Y&struct=auswahlBaum&nodeID=auswahlBaum%7Cabschluss%3Aabschl%3DBS%2Cstgnr%3D1%7Cstudiengang%3Astg%3DSWT%2Cpversion%3D2019&menu_open=n&expand=0&asi={asi_token}"
        response = requests.get(url=url, cookies=cookies)
        soup = BeautifulSoup(response.text, "html.parser")

        if soup.select_one("h1").text.strip() != "Leistungsübersicht":
            print("Session expired, logging in...")
            cookies, asi_token = login.get_login()
            continue

        target_tr = soup.select_one(
            f'tr:has(td.tabelle1:-soup-contains("{MODCODE}"))')

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
