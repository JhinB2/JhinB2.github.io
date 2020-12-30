nums1 = [1,2,3]
nums2 = [4,5,6]
print(nums1,nums2)
result = map(lambda x,y: x+y,nums1,nums2)
print(list(result))