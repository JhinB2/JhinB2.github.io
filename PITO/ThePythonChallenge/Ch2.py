from urllib.request import urlopen
import re

request = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
data = request.readlines()
encrypted_message = map(lambda bytes: bytes.decode("utf-8"), data[37:1257])
rare_chars = re.findall('[a-zA-Z]+', ''.join(encrypted_message))
message = ''.join(rare_chars)

print (message)