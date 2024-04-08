def KMP_search(text, pattern):
    prefix = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[j] != pattern[i]:
            j = prefix[j-1]
        if pattern[j] == pattern[i]:
            j += 1
        prefix[i] = j

    j = 0
    for i in range(len(text)):
        while j > 0 and pattern[j] != text[i]:
            j = prefix[j-1]
        if pattern[j] == text[i]:
            j += 1
        if j == len(pattern):
            print(f"Wzorzec znaleziony na pozycji: {i - j + 1}")
            j = prefix[j-1]