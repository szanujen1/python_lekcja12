def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    middle = int((left + right) / 2)
    if left > right:
        print("Number cannot be found")
        return
    if L[middle] == y:
        print("Found y under index: ", middle)
        return middle
    if L[middle] > y:
        right = middle - 1
        return binarne_rek(L, left, right, y)
    if L[middle] < y:
        left = middle + 1
        return binarne_rek(L, left, right, y)


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    binarne_rek(L, 0, len(L) - 1, i)

print()
L = [1, 5, 9, 11, 20, 34, 77]
binarne_rek(L, 0, len(L) - 1, 77)
binarne_rek(L, 0, len(L) - 1, 0)
binarne_rek(L, 0, len(L) - 1, 349)
