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
            f"Created: {self.name.capitalize()}: "
            f"{height:.1f}cm, {self.age_days} days old"
            )


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Rose", 25.0, 0.8, 30),
        Plant("Oak", 200.0, 0.2, 365),
        Plant("Cactus", 5.1, 0.1, 90),
        Plant("Sunflower", 80.7, 2.0, 45),
        Plant("Fern", 13.4, 0.4, 120),
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.show()
