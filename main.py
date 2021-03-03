import requests
from bs4 import BeautifulSoup

print('Pick A Crypto:')
crypto = input().lower().replace(" ", "-")

url = "https://coinmarketcap.com/currencies/" + crypto

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

cryptoname = soup.find('p', {
    'class': 'sc-1eb5slv-0 hNpJqV converter-item-name'
}).text


cryptoval = soup.find('div', {'class': 'priceValue___11gHJ'}).text

cryptostrip = cryptoval[1:]

print(cryptoname + ': ' + cryptostrip + ' USD')

print('Convert to something other than USD? y/n:')
cryptoconvert = input()

if cryptoconvert == 'y':

    print('To:')
    tocurr = input().upper()

    url2 = 'https://www.x-rates.com/calculator/?from=USD&to=' + tocurr + '&amount=' + cryptostrip

    r2 = requests.get(url2)

    soup2 = BeautifulSoup(r2.text, 'html.parser')

    part1 = soup2.find(class_="ccOutputTrail").previous_sibling
    part2 = soup2.find(class_="ccOutputTrail").get_text(strip=True)
    conversion = "{}{}".format(part1, part2)

    print(cryptoname + ': ' + conversion + ' ' + tocurr)

