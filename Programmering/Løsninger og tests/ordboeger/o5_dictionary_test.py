import o5_dictionary

def test_lookup_in_empty():
    d = o5_dictionary.create()
    assert o5_dictionary.lookup_entry(d, 'unknown') is None


def test_add_to_empty():
    d = o5_dictionary.create()
    old = o5_dictionary.set_entry(d, 'dk', 'Copenhagen')
    assert old is None
    assert o5_dictionary.lookup_entry(d, 'dk') == 'Copenhagen'
    assert o5_dictionary.lookup_entry(d, 'unknown') is None


def test_update_existing():
    d = o5_dictionary.create()
    o5_dictionary.set_entry(d, 'dk', 'Copenhagen')
    old = o5_dictionary.set_entry(d, 'dk', 'København')
    assert old == 'Copenhagen'
    assert o5_dictionary.lookup_entry(d, 'dk') == 'København'


def test_delete_present():
    d = o5_dictionary.create()
    o5_dictionary.set_entry(d, 'fr', 'Paris')
    removed = o5_dictionary.delete_entry(d, 'fr')
    assert removed == 'Paris'
    # efter sletning skal lookup give None
    assert o5_dictionary.lookup_entry(d, 'fr') is None


def test_delete_missing():
    d = o5_dictionary.create()
    assert o5_dictionary.delete_entry(d, 'nonexistent') is None


def test_clear():
    d = o5_dictionary.create()
    o5_dictionary.set_entry(d, 'a', 1)
    o5_dictionary.set_entry(d, 'b', 2)
    o5_dictionary.clear(d)
    # Alle lookups skal nu give None
    assert o5_dictionary.lookup_entry(d, 'a') is None
    assert o5_dictionary.lookup_entry(d, 'b') is None
    # Keys‑listen skal også være tom
    assert o5_dictionary.keys(d) == []


def test_keys_snapshot():
    d = o5_dictionary.create()
    o5_dictionary.set_entry(d, 'x', 10)
    o5_dictionary.set_entry(d, 'y', 20)

    ks = o5_dictionary.keys(d)          # snapshot
    ks.append('z')                   # ændring på snapshot må **ikke** påvirke dict’en

    assert set(o5_dictionary.keys(d)) == {'x', 'y'}   # kun de reelle nøgler
    assert 'z' not in o5_dictionary.keys(d)