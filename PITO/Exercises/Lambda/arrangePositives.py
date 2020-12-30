nums = [-1,2,-3,5,7,8,9,-10]
print(nums)
result = [x for x in nums if x<0] + [x for x in nums if x>=0]
print(result)