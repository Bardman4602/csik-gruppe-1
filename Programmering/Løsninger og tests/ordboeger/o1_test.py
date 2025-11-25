from o1 import *

# Opgave 1
def test_index_of():
    v = [
        'dk',
        'se',
        'no',
        'gb'
    ]
    d = index_of(v)

    assert d['dk'] == 0
    assert d['se'] == 1
    assert d['no'] == 2
    assert d['gb'] == 3
    assert len(d) == 4
    assert list(d.keys()) == v

# Opgave 2
def test_mac_index_of():
    v = [
        (64, 3.2, 8,  '00:1A:2B:3C:4D:5E'),
        (128, 2.8, 16,'00:1A:2B:3C:4D:5F'),
        (32, 3.5, 6,  '00:1A:2B:3C:4D:60'),
        (256, 2.6, 32,'00:1A:2B:3C:4D:61'),
    ]
    d = mac_index_of(v)

    assert d['00:1A:2B:3C:4D:5E'] == 0
    assert d['00:1A:2B:3C:4D:5F'] == 1
    assert d['00:1A:2B:3C:4D:60'] == 2
    assert d['00:1A:2B:3C:4D:61'] == 3
    assert len(d) == 4

    assert list(d.values()) == list(range(len(v)))

def test_mac_index_of_duplicates():
    from pytest import raises
    dup_mac = '00:1A:2B:3C:4D:5E'
    bad_input = [
        (64, 3.2, 8, dup_mac),
        (128, 2.8, 16, dup_mac) 
    ]

    with raises(ValueError):
        mac_index_of(bad_input)