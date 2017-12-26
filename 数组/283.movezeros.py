def movezeros(L):
    k = 0
    for i in range(len(L)):
        if L[i] != 0:
            if i != k:
                L[k], L[i] = L[i], L[k]
                k += 1
            else:
                k += 1
    return L
