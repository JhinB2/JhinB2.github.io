
ins = "HackerRank.com presents \"Pythonist 2\"."

result = ""

for i in ins:
    if i.islower() == True:
        i = i.upper()
    else:
        i = i.lower()
    result = result + i

print(result)