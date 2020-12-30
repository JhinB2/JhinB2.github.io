def compute(n):
    return lambda x:x*n
result = compute(2)
print("Double the number of 15 = ",result(15))