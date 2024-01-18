def sum_of_subset(arr, target):
    n = len(arr)
    subset = [0] * n
    total_sum = sum(arr)
    result = []

    def backtrack(index, current_sum):
        if current_sum == target:
            result.append(subset[:index])
            return
        if index == n or current_sum > target or current_sum + total_sum < target:
            return

        subset[index] = arr[index]
        backtrack(index + 1, current_sum + arr[index])

        subset[index] = 0
        backtrack(index + 1, current_sum)

    backtrack(0, 0)
    return result

arr = [1, 2, 3, 4, 5]
target = 7

result = sum_of_subset(arr, target)
print("Subsets with sum", target, "are:")
for subset in result:
    print(subset)
