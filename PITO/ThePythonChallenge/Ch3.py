from urllib.request import urlopen
import re
request = urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
data = request.readlines()
encrypted_message = map(lambda bytes: bytes.decode("utf-8"), data)
results = re.findall("(?<=[a-z][A-Z]{3})[a-z](?=[A-Z]{3}[a-z])", ''.join(encrypted_message))
print(results)

#LINKEDLIST.PHP