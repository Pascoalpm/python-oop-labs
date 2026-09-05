#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class Vector3D:

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):

        try:
            self.__x = float(x)
            self.__y = float(y)
            self.__z = float(z)
        except (ValueError, TypeError):
            print("Ошибка: все координаты должны быть числами")
            exit(1)

    def read(self, prompt: str = None):

        if prompt is None:
            line = input("Введите координаты x y z (через пробел): ")
        else:
            line = input(prompt)

        parts = line.strip().split()
        if len(parts) != 3:
            print("Ошибка: необходимо ввести три числа через пробел")
            exit(1)

        try:
            self.__x = float(parts[0])
            self.__y = float(parts[1])
            self.__z = float(parts[2])
        except ValueError:
            print("Ошибка: неверный формат чисел")
            exit(1)

    def display(self, name: str = "Vector"):
        """Вывод вектора на экран."""
        print(f"{name} = ({self.__x}, {self.__y}, {self.__z})")

    # === Арифметические операции ===

    def add(self, other: 'Vector3D') -> 'Vector3D':

        if not isinstance(other, Vector3D):
            raise ValueError("Операнд должен быть Vector3D")
        return Vector3D(
            self.__x + other.__x,
            self.__y + other.__y,
            self.__z + other.__z
        )

    def sub(self, other: 'Vector3D') -> 'Vector3D':

        if not isinstance(other, Vector3D):
            raise ValueError("Операнд должен быть Vector3D")
        return Vector3D(
            self.__x - other.__x,
            self.__y - other.__y,
            self.__z - other.__z
        )

    def dot(self, other: 'Vector3D') -> float:
        """
        Скалярное произведение векторов.
        (x1, y1, z1) · (x2, y2, z2) = x1*x2 + y1*y2 + z1*z2
        """
        if not isinstance(other, Vector3D):
            raise ValueError("Операнд должен быть Vector3D")
        return (self.__x * other.__x +
                self.__y * other.__y +
                self.__z * other.__z)

    def scalar_mul(self, scalar: float) -> 'Vector3D':

        try:
            s = float(scalar)
        except (ValueError, TypeError):
            raise ValueError("Скаляр должен быть числом")
        return Vector3D(
            self.__x * s,
            self.__y * s,
            self.__z * s
        )

    # === Операции сравнения ===

    def equals(self, other: 'Vector3D') -> bool:
        """Сравнение векторов на равенство."""
        if not isinstance(other, Vector3D):
            return False
        return (self.__x == other.__x and
                self.__y == other.__y and
                self.__z == other.__z)

    def greater(self, other: 'Vector3D') -> bool:
        return self.length() > other.length()

    def less(self, other: 'Vector3D') -> bool:

        return self.length() < other.length()

    # === Длина вектора ===

    def length(self) -> float:
        """Вычисление длины (модуля) вектора."""
        return math.sqrt(self.__x ** 2 + self.__y ** 2 + self.__z ** 2)

    def length_squared(self) -> float:
        """Квадрат длины вектора (без извлечения корня)."""
        return self.__x ** 2 + self.__y ** 2 + self.__z ** 2

    # === Свойства для доступа к координатам ===

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @property
    def z(self) -> float:
        return self.__z


def make_vector3d(x: float, y: float, z: float) -> Vector3D:

    return Vector3D(x, y, z)


if __name__ == "__main__":
    # Демонстрация работы класса

    print("         РАБОТА С ТРЁХМЕРНЫМИ ВЕКТОРАМИ")

    # 1. Создание векторов через конструктор
    print("\n=== 1. Создание векторов ===")
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)
    v1.display("v1")
    v2.display("v2")

    # 2. Сложение и вычитание
    print("\n=== 2. Сложение и вычитание ===")
    v_sum = v1.add(v2)
    v_sum.display("v1 + v2")

    v_sub = v1.sub(v2)
    v_sub.display("v1 - v2")

    # 3. Скалярное произведение
    print("\n=== 3. Скалярное произведение ===")
    dot_product = v1.dot(v2)
    print(f"v1 · v2 = {dot_product}")

    # 4. Умножение на скаляр
    print("\n=== 4. Умножение на скаляр ===")
    v_scaled = v1.scalar_mul(2.5)
    v_scaled.display("v1 * 2.5")

    # 5. Длина вектора
    print("\n=== 5. Длина вектора ===")
    print(f"|v1| = {v1.length():.4f}")
    print(f"|v2| = {v2.length():.4f}")

    # 6. Сравнение векторов
    print("\n=== 6. Сравнение векторов ===")
    print(f"v1 == v2: {v1.equals(v2)}")
    print(f"v1 > v2 (по длине): {v1.greater(v2)}")
    print(f"v1 < v2 (по длине): {v1.less(v2)}")

    # 7. Создание через внешнюю функцию
    print("\n=== 7. Создание через make_vector3d() ===")
    v3 = make_vector3d(0, 0, 0)
    v3.display("v3 (нулевой вектор)")
    print(f"Длина нулевого вектора: {v3.length()}")

    # 8. Ввод с клавиатуры
    print("\n=== 8. Ввод с клавиатуры ===")
    v4 = Vector3D()
    v4.read("Введите координаты x y z: ")
    v4.display("v4 (введённый)")

    # 9. Сравнение длины векторов с нулём (проверка)
    print("\n=== 9. Проверка сравнения ===")
    v_zero = Vector3D(0, 0, 0)
    v_test = Vector3D(3, 4, 0)
    print(f"|v_test| = {v_test.length()} (должно быть 5.0)")
    print(f"v_test > zero: {v_test.greater(v_zero)}")
    print(f"v_test == zero: {v_test.equals(v_zero)}")