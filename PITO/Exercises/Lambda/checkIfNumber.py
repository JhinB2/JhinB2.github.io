isNum = lambda q:q.replace('.'," ",1).isdigit()
print(isNum('2432'))
print(isNum('4.235'))