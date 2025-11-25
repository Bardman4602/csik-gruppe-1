from c2_Dictionary import Dictionary

def test_basic_flow():
    d = Dictionary()
    assert d.size() == 0
    assert d.lookup_entry('x') is None

    # add
    assert d.add_entry('x', 10) is None
    assert d.size() == 1
    assert d.lookup_entry('x') == 10
    assert d.contains_key('x') is True

    # replace
    old = d.add_entry('x', 20)
    assert old == 10
    assert d.lookup_entry('x') == 20

    # delete
    val = d.delete_entry('x')
    assert val == 20
    assert d.size() == 0
    assert d.lookup_entry('x') is None
    assert d.contains_key('x') is False

def test_multiple_lengths():
    d = Dictionary()
    entries = [
        ('', 2),          # length 0
        ('a', 8),         # length 1
        ('c', 9),         # length 1
        ('foo', 42),      # length 3
        ('bar', 87),      # length 3
    ]
    for k, v in entries:
        d.add_entry(k, v)

    assert d.size() == 5
    expected = [
        [('', 2)],                     # 0
        [('a', 8), ('c', 9)],         # 1
        [],                            # 2
        [('foo', 42), ('bar', 87)],   # 3
    ]
    assert d._v == expected

    for k, v in entries:
        assert d.lookup_entry(k) == v

    # delete a key from bucket length 1
    assert d.delete_entry('c') == 9
    assert d.size() == 4
    assert d._v[1] == [('a', 8)]

def test_nonexistent_length():
    d = Dictionary()
    d.add_entry('abc', 123)   # length 3
    # bucket for længde 2 er tom, men eksisterer
    assert d._v[2] == []
    assert d.lookup_entry('xy') is None   # længde 2, men ingen entry