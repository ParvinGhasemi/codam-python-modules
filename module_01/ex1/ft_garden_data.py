#!/usr/bin/env python3

"""Organize and display data for multiple garden plants."""

class Plant:
    """Represent a plant with a name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes a plant."""
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        """Print the plant information."""
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, {self.age} days old"
            )


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()
