import requests
from bs4 import BeautifulSoup

# = = = = = = = USER AGENT = = = = = = = #
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# = = = = = = = SITE LINK = = = = = = = #
your_link = 'https://telemetr.me/'

full_page = requests.get(
    your_link,
    headers=headers
)
soup = BeautifulSoup(
    full_page.content,
    'html.parser'
)

pref_link = ['https://t.me/', '/@', '/joinchat']
for a in soup.find_all('a', href=True):
    if any(word in a['href'] for word in pref_link):
        if a['href'].startswith('/joinchat'):
            link = a['href']
            print(f"Found the URL: https://t.me/{link[1:]}")
        elif a['href'].startswith('/@'):
            link = a['href']
            print(f"Found the URL: https://t.me/{link[2:]}")
        elif a['href'].startswith('https://t.me/'):
            link = a['href']
            print(f"Found the URL: {link}")
