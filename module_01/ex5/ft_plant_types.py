#!/usr/bin/env python3

"""Secure plant data using encapsulation, getters, and setters.

This exercise demonstrates how a class can protect its internal data by
using protected attributes and controlled access methods. Plant height
and age are validated before being stored or updated.
"""


class Plant:
    """Represent a plant with protected height and age values.

    The class stores plant information using protected attributes. Height
    and age should be changed through setter methods so invalid values,
    such as negative numbers, can be rejected.

    Attributes:
        _name: The plant name.
        _height: The plant height in centimeters.
        _age: The plant age in days.
    """
    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a plant with validated height and age.

        The height starts at ``0.0`` and the age is initialized before
        validation methods are called. The setter methods are then used
        to apply the same validation rules used for later updates.

        Args:
            name: The plant name.
            height: The initial plant height in centimeters.
            age: The initial plant age in days.
        """
        self._name: str = name
        self._height: float = 0.0
        self._age: int = age

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> bool:
        """Update the plant height if the value is valid.

        A negative height is rejected and the current height remains
        unchanged.

        Args:
            height: The new height in centimeters.

        Returns:
            ``True`` if the height was updated, ``False`` otherwise.
        """
        if height < 0:
            print(
                f"{self._name.capitalize()}: "
                f"Error, height can't be negative"
                )
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        """Update the plant age if the value is valid.

        A negative age is rejected and the current age remains unchanged.

        Args:
            age: The new age in days.

        Returns:
            ``True`` if the age was updated, ``False`` otherwise.
        """
        if age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            return False
        self._age = age
        return True

    def get_height(self) -> float:
        """Return the plant height in centimeters."""
        return self._height

    def get_age(self) -> int:
        """Return the plant age in days."""
        return self._age

    def grow(self, amount: float = 0.8) -> None:
        self._height += amount

    def age(self, days: int = 1) -> None:
        self._age += days

    def show(self) -> None:
        """Print the current plant information."""
        print(
            f"{self._name.capitalize()}: "
            f"{self.get_height():.1f}cm, {self._age} days old"
            )


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed: bool = False

    def bloom(self) -> None:
        self.has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.has_bloomed:
            print(f" {self._name.capitalize()} is blooming beautifully")
        else:
            print(f" {self._name.capitalize()} has ot bloomed yet")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        shadow_height: float = round(self.get_height(), 1)
        shadow_width: float = round(self.trunk_diameter, 1)
        print(
            f"Tree {self._name} now produces a shade of "
            f"{shadow_height}cm long and {shadow_width}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str,
            nutritional_value: int
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = nutritional_value

    def grow(self, amount: float = 1.9) -> None:
        super().grow(amount)

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose: Flower = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak: Tree = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato: Vegetable = Vegetable("tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for day in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
