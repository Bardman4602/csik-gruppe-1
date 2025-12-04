from v6 import *

# Opgave 1
def test_vector_sum_of():
    assert vector_sum_of([10, 40, 20], [5, 25, 8]) == [15, 65, 28]
    assert vector_sum_of([], []) == []
    with pytest.raises(ValueError):
        vector_sum_of([1, 2], [1])

#Opgave 2
def test_vector_min_of():
    assert vector_min_of([5, 40, 20], [10, 25, 8]) == [5, 25, 8]
    assert vector_min_of([], []) == []

# Opgave 3
def test_vector_avg_of():
    assert vector_avg_of([5, 40, 20], [10, 25, 8]) == [7.5, 32.5, 14.0]
    assert vector_avg_of([], []) == []

#Opgave 4
def test_vector_prod_of():
    assert vector_prod_of([5, 40, 20], [10, 25, 8]) == [50, 1000, 160]
    assert vector_prod_of([], []) == []

# Opgave 5
def test_merge_of():
    assert merge_of([2, 5, 9], [1, 3, 5, 11]) == [1, 2, 3, 5, 5, 9, 11]
    assert merge_of([], [1, 2]) == [1, 2]
    assert merge_of([1, 2], []) == [1, 2]
    assert merge_of([], []) == []

# Opgave 6
def test_combined_sales_of():
    a = [('apple', 30), ('banana', 20), ('orange', 15)]
    b = [('banana', 10), ('kiwi', 5), ('orange', 25)]
    expected = [
        ('apple', 30),          # kun i a
        ('banana', 30),         # 20+10
        ('kiwi', 5),            # kun i b
        ('orange', 40)          # 15+25
    ]
    assert combined_sales_of(a, b) == expected

    # Edge‑cases
    assert combined_sales_of([], []) == []
    assert combined_sales_of([], [('x', 1)]) == [('x', 1)]
    assert combined_sales_of([('y', 2)], []) == [('y', 2)]

# Opgave 7
def test_dot_product_of():
    assert dot_product_of([1, 2, 3], [7, 5, 4]) == 29
    assert dot_product_of([], []) == 0
    with pytest.raises(ValueError):
        dot_product_of([1, 2], [1])