class Shape:
    def __init__(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def compute_area(self):
        return self.length * self.width