# Problem Statement: Given an array of integers nums and an integer target, return indices of two numbers that add up to target. Assume exactly one solution exists.
# Approach: Use a hash map to store seen numbers and their indices. For each num, check if (target - num) exists in the map.
# Example: nums = [2,7,11,15], target = 9 → [0,1] (2+7=9).
nums = [2, 5, 3, 4, 9, 15]
target = 9
def two_sums(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(two_sums(nums, target))