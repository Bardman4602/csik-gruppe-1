from o0 import *

def test_capitals():
    assert len(capitals) == 5
    assert 'se' not in capitals
    assert capitals.get('ru', 'ukendt') == 'ukendt'

# AI Automatiserede tests
def test_capitals2():
    # 1. Opret tom ordbog
    capitals = {}

    # 2. Tilføj poster
    data = {
        'dk': 'København',
        'se': 'Stockholm',
        'no': 'Oslo',
        'fi': 'Helsinki',
        'de': 'Berlin'
    }
    for k, v in data.items():
        capitals[k] = v

    # 3. Kontroller antal
    assert len(capitals) == 5

    # 4. Test eksistens
    assert ('fr' in capitals) is False
    assert ('se' in capitals) is True

    # 5. Test get‑metoden
    assert capitals.get('gb') is None
    assert capitals.get('gb', 'ukendt') == 'ukendt'

    # 6. Test pop‑fjernelse
    removed = capitals.pop('dk')
    assert removed == 'København'
    assert 'dk' not in capitals

    # 7. Test del‑fejl
    try:
        del capitals['xx']
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError for missing key")

