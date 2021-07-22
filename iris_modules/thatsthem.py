import requests
from bs4 import BeautifulSoup as bs

def run(target):
        scraper = cloudscraper.create_scraper()
        url = f'https://thatsthem.com/email/{target}'
        coookies = dict(__stripe_mid='a3d075ce-148e-4cb8-aca8-9a550d8435291cb782',__stripe_sid='c2fee0d1-b6dc-4f12-bde7-57a6443a2323efce22',PHPSESSID='9176jbk32up4gnggimptb782ct',remember='F%2FnP3tJE%2FuxXA3tNaDn3kwJxRZS7ClMPvbd1SKL6U%2Bk8NnzUZu2bHX8opHRgdV98CAulpv3UH3Q%3D')
        path = scraper.get(url, cookies=coookies).text
        soup = bs(path, 'html.parser')
        name = str(soup.find("span", itemprop="name").text)
        phone = str(soup.find("span", itemprop="telephone").text)
        address = str(soup.find('span', itemprop='streetAddress').text)

        print(f''' Name     : {name}
 Phone    : {phone}
 Address  : {address}
''')