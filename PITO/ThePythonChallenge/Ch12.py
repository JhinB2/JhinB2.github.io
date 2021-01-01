data = open('ThePythonChallenge/Resources/evil2.gfx', 'rb').read()
print(data)
for i in range(5):
    open('ThePythonChallenge/Resources/%d.jpg' % i ,'wb').write(data[i::5])