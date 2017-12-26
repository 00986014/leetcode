def isPalindrome(s):
    s = s.lower()
    i, j = 0, len(s)-1
    l = ''
    for k in range(26):
        l = l+chr(k+97)
    for k in range(10):
        l = l+str(k)
    while i<j:
        while s[i] not in l and i<j:
            i += 1
        while s[j] not in l and i<j:
            j -= 1
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True
