from c0 import Point

def test_moved_returns_new_instance():
    p = Point(1, 2)
    q = p.moved(3, 4)

    assert p.x() == 1
    assert p.y() == 2

    assert q.x() == 4
    assert q.y() == 6

    assert p is not q

def test_move_mutates_in_place():
    p = Point(10, -5)
    returned = p.move(2, 3)

    assert returned is p
    assert p.x() == 12
    assert p.y() == -2

    p.move(-2, -2).move(0, 5)

    assert p.x() == 10
    assert p.y() == 1          