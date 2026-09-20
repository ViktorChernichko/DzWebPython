from abc import ABC, abstractmethod


class Equipment(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def act(self):
        pass


class Sword(Equipment):
    def get_name(self):
        return "Sword"

    def act(self):
        return "Slashes the enemy with a sword"


class Axe(Equipment):
    def get_name(self):
        return "Axe"

    def act(self):
        return "Chops the enemy with an axe"


class Spear(Equipment):
    def get_name(self):
        return "Spear"

    def act(self):
        return "Pierces the enemy with a spear"


class Shield(Equipment):
    def get_name(self):
        return "Shield"

    def act(self):
        return "Blocks the incoming attack"


class Paladin:
    def __init__(self, left_hand, right_hand):
        self.left_hand = left_hand
        self.right_hand = right_hand

    def equip_left_hand(self, equipment):
        self.left_hand = equipment

    def equip_right_hand(self, equipment):
        self.right_hand = equipment

    def show_equipment(self):
        print(f"Left hand: {self.left_hand.get_name()}")
        print(f"Right hand: {self.right_hand.get_name()}")

    def attack(self):
        print(f"{self.left_hand.get_name()}: {self.left_hand.act()}")
        print(f"{self.right_hand.get_name()}: {self.right_hand.act()}")


if __name__ == "__main__":
    paladin = Paladin(Shield(), Sword())
    paladin.show_equipment()
    paladin.attack()

    print()
    paladin.equip_left_hand(Axe())
    paladin.equip_right_hand(Spear())
    paladin.show_equipment()
    paladin.attack()
