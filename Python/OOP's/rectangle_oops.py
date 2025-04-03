class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

length, width = map(int, input().split())
rectangle = Rectangle(length, width)
print(rectangle.area())
print(rectangle.perimeter())
