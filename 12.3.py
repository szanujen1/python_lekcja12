def mediana_sort(L, left, right):
    result = L[left:right + 1]
    # print(result)
    if len(result) % 2 == 1:
        return result[int((left + right) / 2)]
    else:
        return (result[int((left + right) / 2)] + result[int((left + right) / 2) + 1]) / 2


L = [2, 1, 7, 8, 11, 0, 66]
print(mediana_sort(L, 0, 4))

L = [2, 1, 7, 8, 11, 0, 66, 77]
print(mediana_sort(L, 0, len(L) - 1))
