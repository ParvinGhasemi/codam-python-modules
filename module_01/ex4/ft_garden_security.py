#!/usr/bin/env python3

class Plant:
    """info about the class"""

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = age

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
            return False
        self._height = height
        print(f"Height updated: {self.get_height():.1f}cm")
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
            return False
        self._age = age
        print(f"Age updated: {self.get_age()} days")
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self):
        return self._age

    def show(self):
        print(f"{self._name.capitalize()}: {self.get_height():.1f}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose: Plant = Plant("rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-25.0)
    rose.set_age(-2)
    print()

    print(f"Current state: ", end="")
    rose.show()

