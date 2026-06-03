#!/usr/bin/env python3

"""Organize and display data for multiple garden plants."""


class Plant:
    """Represent a plant with a name, height, growth_rate and age."""

    def __init__(
        self,
        name: str,
        height: float,
        growth_rate: float,
        age_days: int,
    ) -> None:
        """Initializes a plant."""
        self.name = name
        self.height = height
        self.growth_rate = growth_rate
        self.age_days = age_days

    def grow(self) -> None:
        """Increase the plant height using its growth rate."""
        self.height += self.growth_rate

    def age(self) -> None:
        """Increase the plant age by one day."""
        self.age_days += 1

    def show(self) -> None:
        """Print the plant information."""
        height = round(self.height, 1)
        print(
            f"{self.name.capitalize()}: "
            f"{height}cm, {self.age_days} days old"
            )


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25.0, 0.8, 30)
    start_height: float = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")
