# Opgave 1
def positives_of(v):
    result = []
    i = 0
    n = len(v)
    while i < n:
        if v[i] > 0:
            result.append(v[i])
        i += 1
    return result

# Opgave 2
def non_empty_of(strings):
    result = []
    i = 0
    n = len(strings)
    while i < n:
        if strings[i] != "":
            result.append(strings[i])
        i += 1
    return result

# Opgave 3
def suspicious_login_attempts_of(attempts):
    result = []
    i = 0
    n = len(attempts)
    while i < n:
        timestamp, user, success = attempts[i]
        if (not success) and (user == "root"):
            result.append(attempts[i])
        i += 1
    return result

# Opgave 4
def every_second_char_of(text):
    result = []
    i = 0
    n = len(text)
    while i < n:
        result.append(text[i])
        i += 2
    return result

# Opgave 5
def remove_negatives(v):
    i = 0               
    j = 0               
    n = len(v)
    while i < n:
        if v[i] >= 0:
            v[j] = v[i]
            j += 1
        i += 1
    del v[j:]

# Opgave 6
def remove_empty(strings):
    i = 0
    j = 0
    n = len(strings)
    while i < n:
        if strings[i] != "":
            strings[j] = strings[i]
            j += 1
        i += 1
    del strings[j:]

# Opgave 7
def remove_every_other(v):
    i = 0
    j = 0
    n = len(v)
    while i < n:
        if i % 2 == 1:
            v[j] = v[i]
            j += 1
        i += 1
    del v[j:]