import re
if __name__ == '__main__':
    n = int(input("N: "))
o = 0
li = []
while o < n:
    inst = input("Insts: ")
    di = re.findall(r"\d*\.*?\d+", ''.join(inst))
    instructs = re.findall("[A-Z,a-z]", ''.join(inst))
    instructs = ''.join(instructs)
    if instructs == "insert":
        li.insert(int(di[0]),int(di[1]))
    elif instructs == "print":
        print(li)
    elif instructs == "remove":
        li.remove(int(di[0]))
    elif instructs == "append":
        li.append(int(di[0]))
    elif instructs == "sort":
        li.sort()
    elif instructs == "pop":
        li.pop()
    elif instructs == "reverse":
        li.reverse()
    di = []
    instructs = []
    o = o + 1