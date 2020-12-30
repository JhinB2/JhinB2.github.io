nums = [1,2,3,5,7,8,9,10]
print(nums)
odds = len(list(filter(lambda x: (x%2 != 0),nums)))
evens = len(list(filter(lambda x: (x%2 == 0),nums)))
print("Evens: ",evens)
print("Odds: ",odds)