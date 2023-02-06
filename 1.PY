import requests,lxml
from bs4 import BeautifulSoup
import re


url = "http://bbs.hupu.com/lol"

resp = requests.get(url)


soup = BeautifulSoup(resp.text , 'lxml')
t = soup.select('.p-title')
print(t)

for tt in t:


    pattern = re.compile(r"[A-Za-z]|<|>|\/|=|-|\"|\n")

    # tttt = pattern.sub("", tt)

    print(tt)