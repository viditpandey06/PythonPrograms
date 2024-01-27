def bucket_sort(arr):
    # Find the maximum value in the array
    max_value = max(arr)
    
    # Create empty buckets
    buckets = [[] for _ in range(len(arr))]
    
    # Distribute the elements into the buckets
    for num in arr:
        index = int(num * len(arr) / (max_value + 1))
        buckets[index].append(num)
    
    # Sort each bucket individually
    for bucket in buckets:
        bucket.sort()
    
    # Concatenate the sorted buckets
    sorted_arr = [num for bucket in buckets for num in bucket]
    
    return sorted_arr
# Driver code
arr = [29, 13, 22, 37, 52, 49, 46, 71, 56]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
