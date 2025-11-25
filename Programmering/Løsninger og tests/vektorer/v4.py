from typing import Iterable, List
from functools import reduce

# Opgave 1 - sum_of(squared(positives_of(...)))

# filtrerer negative tal
def positives_of(v):
    res = []
    i = 0
    n = len(v)
    while i < n:
        if v[i] >= 0:
            res.append(v[i])
        i += 1
    return res

# finder kvadrattallet af hvert tal
def squared(v):
    res = []
    i = 0
    n = len(v)
    while i < n:
        res.append(v[i] * v[i])
        i += 1
    return res

# reducerer ved at lægge alle tal sammen
def sum_of(v):
    total = 0
    i = 0
    n = len(v)
    while i < n:
        total += v[i]
        i += 1
    return total


# Opgave 2 - login attempts

# filtrerer logs
def root_login_attempts_of(logs):
    res = []
    i = 0
    n = len(logs)
    while i < n:
        if logs[i].get("username") == "root":
            res.append(logs[i])
        i += 1
    return res

# finder timestamps
def timestamps_of(attempts):
    res = []
    i = 0
    n = len(attempts)
    while i < n:
        ts = attempts[i].get("timestamp")
        if ts is not None:
            res.append(ts)
        i += 1
    return res

def summary_of(timestamps):
    if not timestamps:
        raise ValueError("Empty vector")
    
    #initier med første element
    first_ts, first_success = timestamps[0]
    last_ts, last_success = first_ts, first_success
    failures = 0
    successes = 0

    # tæller første element
    if first_success:
        successes += 1
    else:
        failures += 1

    i = 1
    n = len(timestamps)
    while i < n:
        ts, succ = timestamps[i]
        if ts < first_ts:
            first_ts = ts
        if ts > last_ts:
            last_ts = ts
        if succ:
            successes += 1
        else:
            failures += 1
        i += 1
    
    return first_ts, last_ts, failures, successes

def timestamps_of_with_success(attempts):
    res = []
    i = 0
    n = len(attempts)
    while i < n:
        ts = attempts[i].get("timestamp")
        succ = attempts[i].get("success", False)
        if ts is not None:
            res.append((ts, succ))
        i += 1
    return res


# Opgave 4 - Oneliners med filter og map

def positives_of_one_liner(v: Iterable[int]) -> List[int]:
    # filtrerer med indbygget filter
    return list(filter(lambda x: x >= 0, v))

def squared_one_liner(v: Iterable[int]) -> List[int]:
    # Afbilder med indbygget map.
    return list(map(lambda x: x * x, v))

def sum_of_one_liner(v: Iterable[int]) -> int:
    # Reducerer med builtin sum.
    # sum håndterer også tom input (returnerer 0)
    return sum(v)      

def sum_of_squared_positives_one_liner(v):    
    # Samme resultat som sum_of(squared(positives_of(v))) men skrevet som én linje.    
    return sum(map(lambda x: x * x, filter(lambda x: x >= 0, v)))


# Opgave 5 - oneliner med functools.reduce

def sum_of_reduce(v):
    # bruger functools.reduce i stedet for den indbyggede sum
    return reduce(lambda acc, x: acc + x, v, 0)

def prod_of_reduce(v):
    # produkt af elementerne ved brug af reduce
    return reduce(lambda acc, x: acc * x, v, 1)

def max_of_reduce(v):
    # Maximum ved brug af reduce
     if not v:
        raise ValueError("Empty vector")
     return reduce(lambda cur_max, x: x if x > cur_max else cur_max, v)

