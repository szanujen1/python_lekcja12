def mediana_sort(L, left, right):
    L = sorted(L)
    if len(L) % 2 == 1:
        return L[int((left + right) / 2)]
    else:
        return (L[int((left + right) / 2)] + L[int((left + right) / 2) + 1]) / 2


L = [2, 1, 7, 8, 11, 0, 66]
print(mediana_sort(L, 0, len(L) - 1))

L = [2, 1, 7, 8, 11, 0, 66, 77]
print(mediana_sort(L, 0, len(L) - 1))
