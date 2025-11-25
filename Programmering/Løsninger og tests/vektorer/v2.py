# Opgave 1 - 2x hvert tal
def doubled(v):
    n = len(v)
    result = [None] * n
    i = 0
    while i < n:
        result[i] = 2 * v[i]
        i += 1
    return result

# Opgave 2 - kvadratrod af hvert tal
def squared(v):
    n = len(v)
    result = [None] * n
    i = 0
    while i < n:
        result[i] = v[i] * v[i]
        i += 1
    return result

# Opgave 3 - Længden af hver string
def length(v):
    n = len(v)
    result = [None] * n
    i = 0
    while i < n:
        result[i] = len(v[i])
        i += 1
    return result

# Opgave 4 - decrement
def decrement(v):
    n = len(v)
    i = 0
    while i < n:
        v[i] = v[i] - 1
        i += 1

# Opgave 5 - Moms
def add_danish_vat(v):
    n = len(v)
    i = 0
    while i < n:
        v[i] = v[i] * 1.25
        i += 1

# Opgave 6 - logisk negation
def negate(v):
    n = len(v)
    i = 0
    while i < n:
        v[i] = not v[i]
        i += 1

