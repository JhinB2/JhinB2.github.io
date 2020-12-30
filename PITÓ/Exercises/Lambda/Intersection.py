nums1 = [1,2,3,5,7,8,9,10]
nums2 = [1,2,4,8,9]
print("Original arrays:")
print(nums1)
print(nums2)
result = list(filter(lambda x: x in nums1,nums2)) #idk man no idea
print("Intersection in arrays: ",result)