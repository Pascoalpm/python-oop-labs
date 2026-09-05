class River:
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)

print("=== Пример 2: Класс River ===\n")
volga = River("Волга", 3530)
seine = River("Сена", 776)
nile = River("Нил", 6852)

for river in River.all_rivers:
    print(river.name)

def get_info(self):
    print("длина {0} равна {1} км".format(self.name, self.length))

River.get_info = get_info

volga.get_info()
seine.get_info()
nile.get_info()