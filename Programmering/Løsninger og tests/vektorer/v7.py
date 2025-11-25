from random import randrange
from v6 import merge_of

# Opgave 1 - Returnér en ny liste, hvor elementerne i values er i omvendt rækkefølge
def reverse_of(v):
    result = []
    i = len(v) - 1
    while i >= 0:
        result.append(v[i])
        i -= 1
    return result

# Opgave 1.2 = Vend rækkefølgen in-place
def reverse(v):
    n = len(v)
    i = 0
    while i < n // 2:
        j = n - 1 - i
        v[i], v[j] = v[j], v[i]
        i += 1

# Opgave 2 - Permuter elementerne i values tilfældigt in-place.
def shuffle(v):
    n = len(v)
    i = n -1
    while i > 0:
        j = randrange(i + 1)
        v[i], v[j] = v[j], v[i]
        i -= 1

# Opgave 3 - Returnér en ny sorteret udgave af values
def merge_sort_of(v):
    n = len(v)
    if n <= 1:
        return v.copy()
    
    mid = n // 2
    left = merge_sort_of(v[:mid])
    right = merge_sort_of(v[mid:])
    return merge_of(left, right)

# Opgave 4 - Grovsortering
def partial_sort(x, a, start=0, end=None):
    if end is None:
        end = len(a)

    # Bevar rækkefølgen med tre midlertidige lister
    reds = []
    whites = []
    blues = []

    for val in a[start:end]:
        if val < x:
            reds.append(val)
        elif val == x:
            whites.append(val)
        else:
            blues.append(val)

    # Flet dem sammen in-place
    a[start:end] = reds + whites + blues

    w = start + len(reds)
    b = w + len(whites)
    return (w, b)


# Opgave 5 - in-place sortering af del-listen
def quick_sort(a, start=0, end=None):
    if end is None:
        end = len(a)

    if end - start <= 1:
        return
    
    pivot_index = start + randrange(end - start)
    pivot_value = a[pivot_index]

    w, b = partial_sort(pivot_value, a, start, end)
    quick_sort(a, start, w)
    quick_sort(a, b, end)