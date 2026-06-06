#!/usr/bin/env python3

"""Model different plant types using inheritance and method overriding.

This exercise extends the base Plant class with specialized plant types:
Flower, Tree, and Vegetable. Each child class inherits common plant
attributes and behavior, then adds its own specific data and methods.
"""


class Plant:
    """Represent a generic plant.

    A Plant stores common information shared by all plant types:
    name, height, and age. Height and age are stored as protected
    attributes and updated through controlled methods.

    Attributes:
        _name: The plant name.
        _height: The plant height in centimeters.
        _age: The plant age in days.
    """
    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a plant with validated height and age.

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

        Args:
            height: The new height in centimeters.

        Returns:
            True if the height was updated, False otherwise.
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

        Args:
            age: The new age in days.

        Returns:
            True if the age was updated, False otherwise.
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
        """Increase the plant height.

        Args:
            amount: The number of centimeters added to the plant height.
        """
        self._height += amount

    def age(self, days: int = 1) -> None:
        """Increase the plant age.

        Args:
            days: The number of days added to the plant age.
        """
        self._age += days

    def show(self) -> None:
        """Print the current plant information."""
        print(
            f"{self._name.capitalize()}: "
            f"{self.get_height():.1f}cm, {self._age} days old"
            )


class Flower(Plant):
    """Represent a flower.

    A Flower is a specialized Plant with a color and blooming state.

    Attributes:
        color: The flower color.
        has_bloomed: Whether the flower has bloomed.
    """

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        """Initialize a flower.

        Args:
            name: The flower name.
            height: The initial flower height in centimeters.
            age: The initial flower age in days.
            color: The flower color.
        """
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed: bool = False

    def bloom(self) -> None:
        """Mark the flower as bloomed."""
        self.has_bloomed = True

    def show(self) -> None:
        """Print flower information, including color and bloom state."""
        super().show()
        print(f" Color: {self.color}")
        if self.has_bloomed:
            print(f" {self._name.capitalize()} is blooming beautifully")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    """Represent a tree.

    A Tree is a specialized Plant with a trunk diameter and the ability
    to produce shade.

    Attributes:
        trunk_diameter: The tree trunk diameter in centimeters.
    """

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float
    ) -> None:
        """Initialize a tree.

        Args:
            name: The tree name.
            height: The initial tree height in centimeters.
            age: The initial tree age in days.
            trunk_diameter: The trunk diameter in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        """Print the shade produced by the tree."""
        shadow_height: float = round(self.get_height(), 1)
        shadow_width: float = round(self.trunk_diameter, 1)
        print(
            f"Tree {self._name} now produces a shade of "
            f"{shadow_height}cm long and {shadow_width}cm wide."
        )

    def show(self) -> None:
        """Print tree information, including trunk diameter."""
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    """Represent a vegetable plant.

    A Vegetable is a specialized Plant with a harvest season and a
    nutritional value. Its nutritional value increases when the
    vegetable ages.

    Attributes:
        harvest_season: The season when the vegetable can be harvested.
        nutritional_value: The vegetable nutritional value.
    """

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str,
            nutritional_value: int
    ) -> None:
        """Initialize a vegetable.

        Args:
            name: The vegetable name.
            height: The initial vegetable height in centimeters.
            age: The initial vegetable age in days.
            harvest_season: The harvest season.
            nutritional_value: The starting nutritional value.
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = nutritional_value

    def grow(self, amount: float = 1.9) -> None:
        """Increase the vegetable height.

        Args:
            amount: The number of centimeters added to the height.
        """
        super().grow(amount)

    def age(self, days: int = 1) -> None:
        """Increase the vegetable age and nutritional value.

        Args:
            days: The number of days added to the vegetable age and
                nutritional value.
        """
        super().age(days)
        self.nutritional_value += days

    def show(self) -> None:
        """Print vegetable information, including harvest and nutrition."""
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
