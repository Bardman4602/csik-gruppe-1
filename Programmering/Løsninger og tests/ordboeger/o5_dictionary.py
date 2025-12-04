N = 7

def create():
    '''Creates and returns an empty dictionary.'''
    d = []
    i = 0
    while i < N:
        d.append([])
        i += 1
    return d

def set_entry(d, key, value):
    '''Adds or updates an entry in the dictionary d.

    If an entry with the given key already exists,
    the old value of that entry is replaced by the
    given value and the old value is returned.

    If not, a new entry is added, and None is returned.
    '''
    idx = hash(key) % N
    bucket = d[idx]

    for i, (k, v) in enumerate(bucket):
        if k == key:
            old = v
            bucket[i] = (key, value)
            return old
    bucket.append((key, value))
    return None
   

def lookup_entry(d, key):
    '''Looks up an entry in the dictionary d.
    
    Returns the value associated to the given key,
    or None, if there is no such entry.
    '''
    idx = hash(key) % N
    bucket = d[idx]

    for k, v in bucket:
        if k == key:
            return v
    return None

def delete_entry(d, key):
    '''Deletes an entry in the dictionary d.
    
    Returns the value associated to the given key,
    or None, if there is no such entry.
    '''
    idx = hash(key) % N
    bucket = d[idx]

    for i, (k, v) in enumerate(bucket):
        if k == key:
            # Fjern tuple fra listen og returnér den tilknyttede værdi
            del bucket[i]
            return v
    return None

def clear(d):
    '''Deletes all entries in the dictionary d.'''
    for i in range(N):
        d[i].clear()

def keys(d):
    '''Returns the keys of the dictionary d.

    The returned list is a detached snapshot of the current
    keys.
    '''
    result = []
    for bucket in d:
        for k, _ in bucket:
            result.append(k)
    return result