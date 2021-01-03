arr = [2,3,6,6,5,7]
arr.sort()
a = -2
while arr[-1] == arr[a]:
    a = a - 1
    if (len(arr) == abs(a) - 1):
        break
print(arr[a])
    