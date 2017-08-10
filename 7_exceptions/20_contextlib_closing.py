from contextlib import closing
from urllib.request import urlopen

url = 'http://compscicenter.ru'
with closing(urlopen(url)) as page:
    print(page)
