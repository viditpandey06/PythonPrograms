def majority_element(nums):
    try:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        
        return candidate
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
nums = [1, 2, 2, 3, 2, 4, 2]
result = majority_element(nums)
print(f"The majority element is: {result}")