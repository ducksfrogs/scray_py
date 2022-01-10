import re
from html import unescape
from urllib.parse import urljoin

with open("dp.html") as f:
    html = f.read()



re.search(r'a.*d', 'abcdefg124')


re.search(r'a.*d', 'abcefg124DEF')


re.search(r'a.*d', 'abcefg124DEF', re.IGNORECASE)


m = re.search('a(.*)f', 'abcefg124DEF')


m


m.group(0)


m.group(1)






