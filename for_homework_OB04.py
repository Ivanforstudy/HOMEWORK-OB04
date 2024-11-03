
from abc import ABC, abstractmethod

# Шаг 1: Создание абстрактного класса для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Шаг 3: Модификация класса Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack_monster(self, monster):
        if self.weapon is not None:
            print(self.weapon.attack())
            monster.defeated()

class Monster:
    def __init__(self, name):
        self.name = name

    def defeated(self):
        print(f"{self.name} побежден!")

# Шаг 4: Реализация боя
if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    # Боец выбирает меч и атакует
    sword = Sword()
    fighter.change_weapon(sword)
    fighter.attack_monster(monster)

    # Создаем нового монстра
    monster = Monster("Новый монстр")

    # Боец выбирает лук и атакует
    bow = Bow()
    fighter.change_weapon(bow)
    fighter.attack_monster(monster)
