class Pet:
    kind = "mammal"
    n_pets = 0
    pet_names = []

    def __init__(self, spec, name):
        self.spec = spec
        self.name = name
        self.legs = 4

print("=== Пример 3: Класс Pet ===\n")
tom = Pet("cat", "Tom")
avocado = Pet("dog", "Avocado")
ben = Pet("goldfish", "Benjamin")

print("Pet.n_pets =", Pet.n_pets)
print("tom.n_pets =", tom.n_pets)
print("avocado.n_pets =", avocado.n_pets)
print("ben.n_pets =", ben.n_pets)

Pet.n_pets = 3
print("\nПосле Pet.n_pets = 3:")
print("Pet.n_pets =", Pet.n_pets)
print("tom.n_pets =", tom.n_pets)
print("avocado.n_pets =", avocado.n_pets)
print("ben.n_pets =", ben.n_pets)

print("\nИзменение kind для ben:")
ben.kind = "fish"
print("Pet.kind =", Pet.kind)
print("tom.kind =", tom.kind)
print("avocado.kind =", avocado.kind)
print("ben.kind =", ben.kind)