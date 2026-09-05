class Rational:
    def __init__(self, a=0, b=1):
        a = int(a)
        b = int(b)
        if b == 0:
            raise ValueError()
        self.__numerator = abs(a)
        self.__denominator = abs(b)
        self.__reduce()

    def __reduce(self):
        def gcd(a, b):
            if a == 0:
                return b
            elif b == 0:
                return a
            elif a >= b:
                return gcd(a % b, b)
            else:
                return gcd(a, b % a)
        c = gcd(self.__numerator, self.__denominator)
        self.__numerator //= c
        self.__denominator //= c

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def display(self):
        print(f"{self.__numerator}/{self.__denominator}")

    def add(self, rhs):
        if isinstance(rhs, Rational):
            a = self.numerator * rhs.denominator + self.denominator * rhs.numerator
            b = self.denominator * rhs.denominator
            return Rational(a, b)
        else:
            raise ValueError()

print("=== Пример 6: Класс Rational ===\n")
r1 = Rational(3, 4)
print("r1 =", end=" ")
r1.display()

r2 = Rational(5, 6)
print("r2 =", end=" ")
r2.display()

r3 = r1.add(r2)
print("r1 + r2 =", end=" ")
r3.display()