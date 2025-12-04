
class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def x(self) -> float:
        return self._x
        
    def y(self) -> float:
        return self._y
        
    def moved(self, dx: float, dy: float) -> "Point":
        return Point(self._x + dx, self._y + dy)
        
    def move(self, dx: float, dy: float) -> "Point":
        self._x += dx
        self._y += dy
        return self
        
    def __repr__(self) -> str:
        return f"Point(x={self._x!r}, y={self._y!r})"