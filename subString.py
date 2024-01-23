def sliding_window_substring(string, substring):
    n = len(string)
    m = len(substring)

    for i in range(n - m + 1):
        j = 0
        while j < m:
            if string[i + j] != substring[j]:
                break
            j += 1

        if j == m:
            return True

    return False

string = "Hello, world!"
substring = "world"

if sliding_window_substring(string, substring):
    print("Substring found!")
else:
    print("Substring not found.")
