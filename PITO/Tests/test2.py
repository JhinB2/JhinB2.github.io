import re

sent = "a very large appliance"

result = re.findall("(?<=[a,e,i,o,u])( )(?=[a,e,i,o,u])", ''.join(sent))
if len(result) >= 1:
    print(True)
else:
    print(False)