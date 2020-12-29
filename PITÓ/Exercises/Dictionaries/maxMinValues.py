myDict = {'x':500,'y':5874,'z':560}
key_max = max(myDict.keys(),key=(lambda k: myDict[k])) #Honestly no idea what this is
key_min = min(myDict.keys(),key=(lambda k: myDict[k])) #same