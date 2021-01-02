from urllib.request import urlopen
import re
i = 0
finalNumber = "45439"
while i<400:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + finalNumber
    request = urlopen(url)
    data = request.readlines()
    encrypted_message = map(lambda bytes: bytes.decode("utf-8"), data)
    results = re.findall("\d", ''.join(encrypted_message))
    finalNumber = ''.join(results)
    print(data)