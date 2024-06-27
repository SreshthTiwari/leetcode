# O(n^2) bruteforce

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i] + nums[j]==target:
                return [i, j]
            
# O(n) hashmap

def twosum(nums, target):
    hash_ = {}
    for idx, num in enumerate(nums):
        if target - num in hash_:
            print(idx, target, num, hash_)
            return [hash_[target - num], idx]
        hash_[num] = idx
        print(hash_)

print("solution: ", twosum([2, 3, 43, 5], 7))