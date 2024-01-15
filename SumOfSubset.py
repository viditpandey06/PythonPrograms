def backtrack(nums, target, path, res):
    if target == 0:
        res.append(path)
        return
    if target < 0:
        return
    for i in range(len(nums)):
        backtrack(nums[i+1:], target-nums[i], path+[nums[i]], res)

def find_subset_sum(nums, target):
    res = []
    backtrack(nums, target, [], res)
    return res

# Example usage:
nums = [1, 2, 3, 4, 5]
target = 7
result = find_subset_sum(nums, target)
print(result)
