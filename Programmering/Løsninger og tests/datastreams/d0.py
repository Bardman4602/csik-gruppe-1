# Hjælpefunktioner
def get_source():
    return [42, 87, 13, 16, 36, 25]

# Opgave 1 - Eksempel
def example_stream():
    source = get_source()
    stream = iter(source)
    return [next(stream) for _ in range(len(source))]

# Opgave 2 - To uafhængige streams
def two_independent_streams():
    """
    Returnerer en tuple med to lister, hver bygget fra en separat iterator
    over den samme kilde. De to streams påvirker hinanden ikke – de er 
    helt uafhængige.
    """
    source = get_source()

    stream_a = iter(source)
    stream_b = iter(source)     

    a_first = next(stream_a)
    b_first = next(stream_b)
    a_second = next(stream_a)

    rest_a = list(stream_a)
    rest_b = list(stream_b)

    stream_a_result = [a_first, a_second] + rest_a
    stream_b_result = [b_first] + rest_b

    return stream_a_result, stream_b_result

# Opgave 3
"""
Objekt	            Er iterable?	    Hvad iteratoren producerer
Tuple((1,2,3))	        Ja	                Elementerne 1, 2, 3
Streng ("abc")	        Ja	                Tegnene 'a', 'b', 'c'
Ordbog ({'a':1})	    Ja	                Nøglerne 'a' (standard) – du kan også iterere over dict.values() eller dict.items()
Tal (42)	            Nej	                – (ikke iterable)
"""

# Opgave 4
def demo_for_loops():
    source_list = get_source()
    source_tuple = tuple(source_list)
    source_str = "Hej"
    source_dict = {"a": 1, "b": 2, "c": 3}

    for x in source_list:
        print(f"Liste element: {x}")

    for x in source_tuple:
        print(f"Tupel element {x}")

    for char in source_str:
        print(f"Antal tegn i streng: {char}")

    for key in source_dict:
        print(f"Nøgle i dict: {key} -> værdi: {source_dict[key]}")

# Opgave 5
"""
source = [42, 87, 13, 16, 36, 25]
stream = iter(source)

next(stream)        # → 42   (flytter iteratoren til position 1)
next(stream)        # → 87   (flytter iteratoren til position 2)

for x in stream:  # iteratoren fortsætter fra position 2
    print(x)

Efter de to next‑kald er iteratoren “peget” på elementet 13 (det tredje i listen).
for‑løkken bruger den samme iterator (stream). Den starter derfor med at hente 13, derefter 16, 36, og til sidst 25.
Når listen er udtømt, afslutter for‑løkken automatisk (intern StopIteration håndteres bag kulisserne).
"""

# Opgave 6 - Erstat while med for
def while_print_list():
    i = 0
    src = get_source()
    while i < len(src):
        print(src[i])
        i += 1

def for_print_list():
    for x in get_source():
        print(x)

def while_sum_dict(d):
    total = 0
    keys = list(d.keys())
    i = 0
    while i < len(keys):
        total += d[keys[i]]
        i += 1
    return total

def for_sum_dict(d):
    total = 0
    for v in d.values():
        total += v
    return total

# Opgave 7 - Generator med prints
def my_generator():
    print("Første yield")
    yield 42
    print("Anden yield")
    yield 87
    print("Tredje yield")
    yield 13
    print("Fjerde yield")
    yield 16
    print("Femte yield")
    yield 36
    print("Sjette yield")
    yield 25

# Opgave 8 - Stream fra generator
def stream_from(seq):
    i = 0
    length = len(seq)
    while i < length:
        yield seq[i]
        i += 1


if __name__ == "__main__":
    source = get_source()
    stream = iter(source)

    try:
        while True:
            print(next(stream))
    except StopIteration:
        print("Done!")
