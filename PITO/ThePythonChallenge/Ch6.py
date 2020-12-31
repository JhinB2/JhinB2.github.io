import zipfile,re
strNum = '90052'
text = []
while True:
    if strNum == '46145':
        break
    f = zipfile.ZipFile("ThePythonChallenge/Resources/channel.zip")
    content = f.read(strNum + ".txt").decode("utf-8")
    num = re.findall(r"\d",''.join(content))
    strNum = ''.join(num)
    comments = f.getinfo(strNum + '.txt').comment
    key = re.findall("(?<=[b\'])(.)(?=\')",''.join(str(comments)))
    text = text + key
final = ''.join(text)
print(final)