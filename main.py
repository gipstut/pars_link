import requests
import re
from urllib.parse import urlparse

def chek_list(u):
    if u in full_list:
        pass
    else:
        full_list.append(u)

link = input()
full_list = []
code = requests.get(link).text
pattern = r'<a.+href=[\'"]([^./][^\'"]*)[\'"]'
full_link = re.findall(pattern, code)
for i in full_link:
    u = urlparse(i).hostname
    chek_list(u)

new_list = []

for foo in full_list:
    if foo != None:
        new_list.append(foo)
new_list.sort()
for foo1 in new_list:
    print(foo1)

