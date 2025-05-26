class pair_elements:
    def twoSum (self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
value = int(input("Enter the number of elements in the list: "))
print (index1,)