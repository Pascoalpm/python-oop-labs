class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError

    def area(self):
        return self.__width * self.__height

print("=== Пример 5: Класс Rectangle (@property) ===\n")
rect = Rectangle(10, 20)

print("Чтение через property:")
print("rect.width =", rect.width)
print("rect.height =", rect.height)
print("rect.area() =", rect.area())

print("\nИзменение через property:")
rect.width = 50
rect.height = 70

print("rect.width =", rect.width)
print("rect.height =", rect.height)
print("rect.area() =", rect.area())