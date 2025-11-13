class rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def perimeter(self):
        return abs(2 * self.width) + abs(2 * self.height)

    def area(self):
        return abs(self.width * self.height)
