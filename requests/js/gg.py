import requests
from bs4 import BeautifulSoup

save_file = 'gg.html'

url = 'https://www.google.com'


r = requests.get(url)
soup = BeautifulSoup(r.text)
# print(soup.prettify())
with open(save_file, 'w') as f:
    f.write(soup.prettify())
print(r.cookies)
# print(r.text)