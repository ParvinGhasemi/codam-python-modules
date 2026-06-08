#!/usr/bin/env python3

"""Track garden analytics using static methods, class methods, and inheritance.

This exercise extends the plant class hierarchy with statistics tracking.
It introduces nested classes, static methods, class methods, inheritance,
method overriding, and a shared function that displays statistics for any
plant type.
"""


class Plant:
    """Represent a plant with protected data and statistics.

    The Plant class stores common plant information and behavior. It also
    owns a nested Stats object that tracks grow(), age(), and show() calls.

    Attributes:
        _name: The plant name.
        _height: The plant height in centimeters.
        _age: The plant age in days.
        _stats: The plant statistics tracker.
    """

    class Stats:
        """Track method call statistics for a plant.

        The nested Stats class stores how many times selected Plant methods
        have been called.

        Attributes:
            _grow_calls: Number of times grow() was called.
            _age_calls: Number of times age() was called.
            _show_calls: Number of times show() was called.
        """
        def __init__(self) -> None:
            """Initialize all method call counters to zero."""
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def add_grow_counts(self) -> None:
            """Increase the grow() call counter by one."""
            self._grow_calls += 1

        def add_age_counts(self) -> None:
            """Increase the age() call counter by one."""
            self._age_calls += 1

        def add_show_counts(self) -> None:
            """Increase the show() call counter by one."""
            self._show_calls += 1

        def show(self) -> None:
            """Print the stored method call statistics."""
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a plant with validated height and age.

        Args:
            name: The plant name.
            height: The initial plant height in centimeters.
            age: The initial plant age in days.
        """
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._stats: Plant.Stats = Plant.Stats()

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

    def get_name(self) -> str:
        """Return the plant name."""
        return self._name

    def get_height(self) -> float:
        """Return the plant height in centimeters."""
        return self._height

    def get_age(self) -> int:
        """Return the plant age in days."""
        return self._age

    def grow(self, amount: float = 8.0) -> None:
        """Increase the plant height and update growth statistics.

        Args:
            amount: The number of centimeters added to the plant height.
        """
        self._height += amount
        self._stats.add_grow_counts()

    def age(self, days: int = 1) -> None:
        """Increase the plant age and update age statistics.

    Args:
        days: The number of days added to the plant age.
        """
        self._age += days
        self._stats.add_age_counts()

    def show(self) -> None:
        self._stats.add_show_counts()
        height: float = round(self._height, 1)
        print(
            f"{self._name.capitalize()}: "
            f"{height}cm, {self._age} days old"
        )

    def show_stats(self) -> None:
        """Print the plant information and update show statistics."""
        self._stats.show()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        """Return whether an age is greater than one year.

        Args:
            age: The age in days.

        Returns:
            True if age is greater than 365, False otherwise.
        """
        return age > 365

    @classmethod
    def create_anonymous_plant(cls) -> "Plant":
        """Create a plant with default anonymous values.

        Returns:
            A Plant instance named Unknown Plant with zero height and age.
        """
        return cls("Unknown Plant", 0.0, 0)


class Flower(Plant):
    """Represent a flower.

    A Flower is a specialized Plant with color and blooming state.

    Attributes:
        _color: The flower color.
        _has_bloomed: Whether the flower has bloomed.
    """
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._has_bloomed: bool = False

    def bloom(self) -> None:
        """Mark the flower as bloomed."""
        self._has_bloomed = True

    def show(self) -> None:
        """Print flower information, including color and bloom state."""
        super().show()
        print(f"Color: {self._color}")
        if self._has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    """Represent a tree.

    A Tree is a specialized Plant with a trunk diameter and extra shade
    statistics.

    Attributes:
        _trunk_diameter: The trunk diameter in centimeters.
        _shade_calls: Number of times produce_shade() was called.
    """

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        """Print the shade produced by the tree and update shade statistics."""
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter
        self._shade_calls: int = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        height: float = round(self._height, 1)
        diameter: float = round(self._trunk_diameter, 1)
        print(
            f"Tree {self._name} now produces a shade of "
            f"{height}cm long and {diameter}cm wide."
        )

    def show(self) -> None:
        """Print tree information, including trunk diameter."""
        super().show()
        diameter: float = round(self._trunk_diameter, 1)
        print(f"Trunk diameter: {diameter}cm")

    def show_stats(self) -> None:
        """Print tree statistics, including shade calls."""
        super().show_stats()
        print(f"{self._shade_calls} shade")


class Vegetable(Plant):
    """Represent a vegetable plant.

    A Vegetable is a specialized Plant with a harvest season and
    nutritional value.

    Attributes:
        _harvest_season: The vegetable harvest season.
        _nutritional_value: The vegetable nutritional value.
    """
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: int,
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season: str = harvest_season
        self._nutritional_value: int = nutritional_value

    def grow(self, amount: float = 2.1) -> None:
        """Increase the vegetable height.

        Args:
            amount: The number of centimeters added to the height.
        """
        super().grow(amount)

    def age(self, days: int = 1) -> None:
        """Increase vegetable age and nutritional value.

        Args:
            days: The number of days added to age and nutritional value.
        """
        super().age(days)
        self._nutritional_value += days

    def show(self) -> None:
        """Print vegetable information, including harvest and nutrition."""
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    """Represent a seed-producing flower.

    A Seed inherits from Flower and stores the number of seeds after
    blooming.

    Attributes:
        _seeds: The number of seeds produced.
    """

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seeds: int,
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds: int = seeds

    def bloom(self) -> None:
        """Bloom the flower and set the number of produced seeds."""
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        """Print seed information, including flower data and seed count."""
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    """Display statistics for any kind of plant.

    Args:
        plant: The plant object whose statistics should be displayed.
    """
    print(f"[statistics for {plant.get_name()}]")
    plant.show_stats()


def main() -> None:
    """Run the garden analytics demonstration."""
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print()

    print("=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print()

    print("=== Seed")
    sunflower: Seed = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)
    print()

    print("=== Anonymous")
    anonymous: Plant = Plant.create_anonymous_plant()
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
