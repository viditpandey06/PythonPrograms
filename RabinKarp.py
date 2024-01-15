def rabin_karp(text, pattern):
    # Calculate the hash value of the pattern
    pattern_hash = hash(pattern)

    # Calculate the hash value of the first window in the text
    text_hash = hash(text[:len(pattern)])

    # Iterate through each window in the text
    for i in range(len(text) - len(pattern) + 1):
        # Check if the hash values match
        if text_hash == pattern_hash:
            # Check if the window matches the pattern
            if text[i:i+len(pattern)] == pattern:
                return i

        # Calculate the hash value of the next window
        if i < len(text) - len(pattern):
            text_hash = hash(text[i+1:i+len(pattern)+1])

    return -1
# Driver code
text = "Hello, world!"
pattern = "world"
index = rabin_karp(text, pattern)
if index != -1:
    print(f"Pattern found at index {index}")
else:
    print("Pattern not found")
