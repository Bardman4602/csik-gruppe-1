from d0 import *

# Opgave 1
def test_example_stream():
    assert example_stream() == [42, 87, 13, 16, 36, 25]

# Opgave 2
def test_two_independent_streams():
    a, b = two_independent_streams()
    assert a == b == [42, 87, 13, 16, 36, 25]

# Opgave 3
def test_stream_from():
    src = get_source()
    assert list(stream_from(src)) == src