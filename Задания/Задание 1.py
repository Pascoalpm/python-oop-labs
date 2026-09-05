#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Power:

    def __init__(self, first: float = 0.0, second: int = 0):

        try:
            self.__first = float(first)
            self.__second = int(second)
        except (ValueError, TypeError):
            print("Ошибка: неверный тип аргументов")
            print("first должно быть числом, second - целым числом")
            exit(1)

    def read(self, prompt: str = None):
        if prompt is None:
            line = input("Введите основание и степень (через пробел): ")
        else:
            line = input(prompt)

        parts = line.strip().split()
        if len(parts) != 2:
            print("Ошибка: необходимо ввести два числа через пробел")
            exit(1)

        try:
            self.__first = float(parts[0])
            self.__second = int(parts[1])
        except ValueError:
            print("Ошибка: неверный формат чисел")
            exit(1)

    def display(self):
        """Вывод значений на экран."""
        print(f"first = {self.__first}, second = {self.__second}")

    def power(self) -> float:


        return self.__first ** self.__second

    # Свойства для доступа к полям (дополнительно)
    @property
    def first(self) -> float:
        return self.__first

    @property
    def second(self) -> int:
        return self.__second


def make_power(first: float, second: int) -> Power:

    if not isinstance(first, (int, float)):
        print("Ошибка: first должно быть числом")
        exit(1)
    if not isinstance(second, int):
        print("Ошибка: second должно быть целым числом")
        exit(1)

    return Power(first, second)

if __name__ == "__main__":
    # Демонстрация работы класса

    # 1. Создание через конструктор
    print("=== Демонстрация 1: Конструктор ===")
    p1 = Power(2.5, 3)
    p1.display()
    print(f"2.5 ^ 3 = {p1.power()}")
    print()

    # 2. Создание через внешнюю функцию
    print("=== Демонстрация 2: make_power() ===")
    p2 = make_power(4.0, -2)
    p2.display()
    print(f"4.0 ^ -2 = {p2.power()}")
    print()

    # 3. Ввод с клавиатуры
    print("=== Демонстрация 3: Ввод с клавиатуры ===")
    p3 = Power()
    p3.read("Введите основание и степень: ")
    p3.display()
    print(f"{p3.first} ^ {p3.second} = {p3.power()}")
    print()

    # 4. Граничные случаи
    print("=== Демонстрация 4: Граничные случаи ===")

    # Нулевая степень
    p4 = Power(5.0, 0)
    print(f"5.0 ^ 0 = {p4.power()}")

    # Отрицательное основание с чётной степенью
    p5 = Power(-3.0, 2)
    print(f"(-3.0) ^ 2 = {p5.power()}")

    # Отрицательное основание с нечётной степенью
    p6 = Power(-3.0, 3)
    print(f"(-3.0) ^ 3 = {p6.power()}")

    # Дробное основание
    p7 = Power(0.5, 4)
    print(f"0.5 ^ 4 = {p7.power()}")

    # Отрицательная степень (дробь)
    p8 = Power(2.0, -3)
    print(f"2.0 ^ -3 = {p8.power()}")