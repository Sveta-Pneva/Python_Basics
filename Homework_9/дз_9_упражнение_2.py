class Road:
    def __init__(self, _length=0, _width=0, _m=25, _depth=1):
        self._length = _length
        self._width = _width
        self._m = _m
        self._depth = _depth
    def calc_m_asphalt(self):
        result = self._length * self._width * self._m * self._depth
        print(result)

r = Road(1, 2, 6, 24)
r.calc_m_asphalt()