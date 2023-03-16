import requests
from bs4 import BeautifulSoup
import credentials

login_url = 'https://ecampus.thm.de/service/rds?state=user&type=1&category=auth.login'
overview_url = 'https://ecampus.thm.de/service/rds?state=redirect&sso=qisstud&myre=state%253DnotenspiegelStudent%2526next%253Dtree.vm%2526nextdir%253Dqispos/notenspiegel/student%2526menuid%253DnotenspiegelStudent'

def get_login():
    response = requests.get(login_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    ajax_token = soup.find('input', {'id': 'ajaxToken'})['value']

    login_data = {
        'ajax-token': ajax_token,
        'asdf': credentials.USERNAME,
        'fdsa': credentials.PASSWORD
    }

    response = requests.post(login_url, data=login_data, allow_redirects=False)
    cookie = {"JSESSIONID": response.cookies['JSESSIONID']}

    response = requests.get(overview_url, cookies=cookie, allow_redirects=False)
    response = requests.get(
        response.headers['Location'], cookies=cookie, allow_redirects=False)

    cookie['JSESSIONID'] = response.cookies['JSESSIONID']  # New JSESSIONID
    response = requests.get(
        response.headers['Location'], cookies=cookie, allow_redirects=False)

    asi_token = response.url.split('asi=')[1]

    return cookie, asi_token