def exchange_elem(arr):
    n = len(arr)
    mid = n // 2

    arr[:mid], arr[mid:] = arr[mid:], arr[:mid]
    
    return arr

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output_list = exchange_elem(input_list)
print(input_list)
print(output_list)
