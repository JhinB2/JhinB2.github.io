n = 2
odd = False
if n % 2 == 0:
    if 5 >= n >= 2:
        print("Not Weird")
    elif 20 >= n >= 6:
        print("Weird")
    elif n > 20:
        print("Not Weird")
else:
    print("Weird")
