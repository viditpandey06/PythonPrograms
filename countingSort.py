def counting_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)

    # Create a count array to store the count of each element
    count = [0] * (max_element + 1)

    # Count the occurrences of each element in the array
    for num in arr:
        count[num] += 1

    # Create a sorted array by iterating over the count array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

# Test the counting sort function
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)

# Display the original array and the sorted array
print("Original array:", arr)
print("Sorted array:", sorted_arr)
