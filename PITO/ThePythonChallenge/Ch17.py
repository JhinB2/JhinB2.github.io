from urllib.request import urlopen
from urllib.parse import unquote_plus, unquote_to_bytes
import re, bz2

i = 0

finalNumber = "12345"

while True:
    h = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + finalNumber)
    raw = h.read().decode('utf-8')
    print(raw)
    cookie = h.getheader("Set-Cookie")