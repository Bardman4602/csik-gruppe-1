import pytest
from v3 import sum_of

# Opgave 1 - Element‑for‑element‑sum af to vektorer af samme længde.
def vector_sum_of(a, b):
    if len(a) != len(b):
        raise ValueError("Vektorer skal have samme længde")
    result = []
    i = 0
    n = len(a)
    while i < n:
        result.append(a[i] + b[i])
        i += 1
    return result

# Opgave 2 - Element‑for‑element‑minimum af to vektorer af samme længde.
def vector_min_of(a, b):
    if len(a) != len(b):
        raise ValueError("Vektorer skal have samme længde")
    result = []
    i = 0
    n = len(a)
    while i < n:
        result.append(a[i] if a[i] < b[i] else b[i])
        i += 1
    return result

# Opgave 3 - Element‑for‑element‑gennemsnit af to vektorer af samme længde
def vector_avg_of(a, b):
    if len(a) != len(b):
        raise ValueError("Vektorer skal have samme længde")
    result = []
    i = 0
    n = len(a)
    while i < n:
        result.append((a[i] + b[i]) / 2.0)
        i += 1
    return result

# Opgave 4 - Element‑for‑element‑produkt af to vektorer af samme længde.
def vector_prod_of(a, b):
    if len(a) != len(b):
        raise ValueError("Vektorer skal have samme længde")
    result = []
    i = 0
    n = len(a)
    while i < n:
        result.append(a[i] * b[i])
        i += 1
    return result

# Opgave 5 - flet to sorterede lister til én sorteret liste
def merge_of(a, b):
    i = 0 
    j = 0 
    n_a = len(a)
    n_b = len(b)
    merged = []

    while i < n_a or j < n_b:
        if i >= n_a:
            merged.append(b[j])
            j += 1
            continue
        if j >= n_b:
            merged.append(a[i])
            i += 1
            continue

        if a[i] < b[j]:                 # case 1
            merged.append(a[i])
            i += 1
        elif b[j] < a[i]:               # case 2
            merged.append(b[j])
            j += 1
        else:                           # case 3 (a[i] == b[j])
            merged.append(a[i])
            merged.append(b[j])
            i += 1
            j += 1
        
    return merged

# Opgave 6 - flet 2 lister
def combined_sales_of(a, b):
    i = 0
    j = 0
    n_a = len(a)
    n_b = len(b)
    merged = []

    while i < n_a or j < n_b:
        if i >= n_a:
            merged.append(b[j])
            j += 1
            continue
        if j >= n_b:
            merged.append(a[i])
            i += 1
            continue

        prod_a, vol_a = a[i]
        prod_b, vol_b = b[j]

        if prod_a < prod_b:
            merged.append((prod_a, vol_a))
            i += 1
        elif prod_b < prod_a:
            merged.append((prod_b, vol_b))
            j += 1
        else:
            merged.append((prod_a, vol_a + vol_b))
            i += 1
            j += 1

    return merged

# Opgave 7 - bruger vector_prod_of + sum_of
def dot_product_of(a, b):
    prod_vec = vector_prod_of(a, b)
    return sum_of(prod_vec)

# Kør hele filen direkte her
if __name__ == "__main__":
    print("vector_sum_of :", vector_sum_of([10, 40, 20], [5, 25, 8]))
    print("vector_min_of :", vector_min_of([5, 40, 20], [10, 25, 8]))
    print("vector_avg_of :", vector_avg_of([5, 40, 20], [10, 25, 8]))
    print("vector_prod_of:", vector_prod_of([5, 40, 20], [10, 25, 8]))
    print("merge_of      :", merge_of([2, 5, 9], [1, 3, 5, 11]))
    print("combined_sales_of:",
          combined_sales_of(
              [('apple', 30), ('banana', 20)],
              [('banana', 10), ('orange', 5)]
          ))
    print("dot_product_of:", dot_product_of([1, 2, 3], [7, 5, 4]))