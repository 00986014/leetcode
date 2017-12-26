def reverseVowels(s):
    l = [x for x in s]
    i, j = 0, len(l)-1
    while i<j:
        while l[i] not in 'aeiouAEIOU' and i<j:
            i += 1
        while l[j] not in 'aeiouAEIOU' and i<j:
            j -= 1
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    return ''.join(l)
