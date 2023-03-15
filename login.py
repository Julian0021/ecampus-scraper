import requests
import time
from bs4 import BeautifulSoup
import constants

USERNAME = constants.USERNAME
PASSWORD = constants.PASSWORD

login_url = 'https://ecampus.thm.de/service/rds?state=user&type=1&category=auth.login'

session = requests.session()
response = session.get(login_url)

soup = BeautifulSoup(response.text, 'html.parser')

ajax_token = soup.find('input', {'id': 'ajaxToken'})['value']

print(f"Found AJAX token: {ajax_token}")

login_data = {
    'ajax-token': ajax_token,
    'asdf': USERNAME,
    'fdsa': PASSWORD
}

response = session.post(login_url, data=login_data, allow_redirects=False)

jsessionid = response.cookies['JSESSIONID']

cookie = {
    "JSESSIONID": response.cookies['JSESSIONID']
}

response = session.get('https://ecampus.thm.de/service/rds?state=redirect&sso=qisstud&myre=state%253DnotenspiegelStudent%2526next%253Dtree.vm%2526nextdir%253Dqispos/notenspiegel/student%2526menuid%253DnotenspiegelStudent', cookies=cookie, allow_redirects=False)
response = session.get(response.headers['Location'], cookies=cookie, allow_redirects=False)

cookie['JSESSIONID'] = response.cookies['JSESSIONID']
print(f"Found JSESSIONID: {cookie['JSESSIONID']}")
response = session.get(response.headers['Location'], cookies=cookie, allow_redirects=False)

asi_token = response.url.split('asi=')[1]
print(f"Found ASI token: {asi_token}")