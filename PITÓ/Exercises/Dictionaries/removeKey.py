d = {0:10,1:20,2:30}
if 2 in d:
    del d[2]
for key,value in d.items():
    print(key,'->',value)