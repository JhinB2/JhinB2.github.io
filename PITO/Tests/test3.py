
txt = "How the Avocado Became the Fruit of the Global Trade"
result = ""
li = list(txt.split(" "))
li.sort(key=len)
li2 = []
for i in li:
	i = '#' + i.lower()
	li2.insert(0,i)
li3 = li2[:3]
li3.sort()
print(li3)
print(li)