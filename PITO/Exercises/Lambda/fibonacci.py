from functools import reduce
fib_series = lambda n: reduce(lambda x,_: x+[x[-1]+x[-2]],range(n-2),[0,1]) #no clue
print("Fiboono: ",fib_series(10))