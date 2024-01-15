def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        
        if j == m:
            print("Pattern found at index", i)

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
naive_string_matching(text, pattern)
