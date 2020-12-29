def test_duplicate(array_nums):
    nums_set = set(array_nums)              #Transform into set
    return len(array_nums) != len(nums_set) #A set is never repeated so check length
print(test_duplicate([1,2,3,4,5,6]))
print(test_duplicate([1,2,3,4,5,5]))