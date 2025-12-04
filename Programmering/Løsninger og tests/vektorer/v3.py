# Opgave 1 - Sum
def sum_of(v):
    total = 0
    n = len(v)
    i = 0
    while i < n:
        total += v[i]
        i += 1
    return total

# Opgave 2 - Find produktet af elementerne
def prod_of(v):
    prod = 1   
    n = len(v)
    i = 0
    while i < n:
        prod *= v[i]
        i += 1
    return prod

# Opgave 3 - sammenkædning af strings
def concat_of(v):
    result = ""   
    n = len(v)
    i = 0
    while i < n:
        result += v[i]
        i += 1
    return result

# Opgave 4 - Logisk AND af boolske værdier
def all_of(v):
    n = len(v)
    i = 0
    while i < n:
        if not v[i]:
            return False
        i += 1
    return True

# Opgave 5 - Any of
def any_of(v):
    n = len(v)
    i = 0
    while i < n:
        if v[i]:
            return True
        i += 1
    return False

# Opgave 7 - Max af elementer
def max_of(v):
    n = len(v)
    if n == 0:
        raise ValueError("Empty vector")
    current_max = v[0]
    i = 1
    while i < n:
        if v[i] > current_max:
            current_max = v[i]
        i += 1
    return current_max

# Opgave 8 - Retuner korteste string
def shortest_of(v):
    n = len(v)
    if n == 0:
        raise ValueError("Empty vector")
    shortest = v[0]
    i = 1
    while i < n:
        if len(v[i]) < len(shortest):
            shortest = v[i]
        i += 1
    return shortest

# Opgave 9 - Gennemsnit
def avg_of(v):
    n = len(v)
    if n == 0:
        raise ValueError("Empty vector")
    total = 0
    i = 0
    while i < n:
        total += v[i]
        i += 1
    return total / n

# Opgave 10 - Sepereret sum
def separated_sum_of(v):
    pos = 0
    neg = 0
    n = len(v)
    i = 0
    while i < n:
        if v[i] > 0:
            pos += v[i]
        elif v[i] < 0:
            neg += v[i]
        i += 1
    return pos, neg