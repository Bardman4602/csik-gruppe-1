from c3_Dictionary import Dictionary

def test_basic_flow():
    d = Dictionary()
    assert d.size() == 0
    assert d.lookup_entry('x') is None

    # Første indsættelse
    assert d.add_entry('x', 10) is None
    assert d.size() == 1
    assert d.lookup_entry('x') == 10
    assert d.contains_key('x') is True

    # Erstat eksisterende nøgle
    old = d.add_entry('x', 20)
    assert old == 10
    assert d.lookup_entry('x') == 20
    assert d.size() == 1          # størrelse ændrer sig ikke ved erstatning

    # Slet
    val = d.delete_entry('x')
    assert val == 20
    assert d.size() == 0
    assert d.lookup_entry('x') is None
    assert d.contains_key('x') is False

def test_multiple_keys_and_hash_spread():
    d = Dictionary()
    keys = ['a', 'bb', 'ccc', 'dddd', 'eeee', 'fffff', 'gggggg']
    for i, k in enumerate(keys):
        d.add_entry(k, i * 10)

    assert d.size() == len(keys)

    # Alle værdier skal kunne slås op korrekt
    for i, k in enumerate(keys):
        assert d.lookup_entry(k) == i * 10
        assert d.contains_key(k) is True

    # Slet et par og tjek igen
    assert d.delete_entry('bb') == 10
    assert d.delete_entry('dddd') == 30
    assert d.size() == len(keys) - 2
    assert d.lookup_entry('bb') is None
    assert d.contains_key('bb') is False

def test_hash_collision_handling():
    """
    Vi bruger en meget lille startkapacitet for at tvinge flere
    sammenstød (collision) i de samme buckets.
    """
    d = Dictionary(initial_capacity=3)   # 3 buckets → mange collisions
    key1 = 'key_one'
    key2 = 'key_two'

    d.add_entry(key1, 'first')
    d.add_entry(key2, 'second')

    # Begge skal stadig kunne findes korrekt
    assert d.lookup_entry(key1) == 'first'
    assert d.lookup_entry(key2) == 'second'

    # Erstatning i en bucket med collision
    old = d.add_entry(key1, 'new_first')
    assert old == 'first'
    assert d.lookup_entry(key1) == 'new_first'

def test_dynamic_resizing_up_and_down():
    d = Dictionary(initial_capacity=4)   # lille start for at trigge vækst hurtigt

    # Fyld tabellen så den overstiger load‑factor > 1 → fordobling til 8
    for i in range(5):                  # 5 > 4 → trigger resize
        d.add_entry(f'k{i}', i)

    assert len(d._v) == 8               # bekræft at tabellen voksede
    assert d.size() == 5

    # Slet ned til under ¼ af kapaciteten → halvering til 4 igen
    for i in range(4):
        d.delete_entry(f'k{i}')

    assert len(d._v) == 4               # tabellen krympede igen
    assert d.size() == 1                # kun ét element tilbage

def test_non_string_keys():
    d = Dictionary()
    tup_key = (1, 'a')
    int_key = 42

    d.add_entry(tup_key, 'tuple value')
    d.add_entry(int_key, 'int value')

    assert d.lookup_entry(tup_key) == 'tuple value'
    assert d.lookup_entry(int_key) == 'int value'
    assert d.contains_key(tup_key) is True
    assert d.contains_key(int_key) is True

    # Slet dem igen
    assert d.delete_entry(tup_key) == 'tuple value'
    assert d.delete_entry(int_key) == 'int value'
    assert d.size() == 0