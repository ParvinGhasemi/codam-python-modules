#!/usr/bin/env python3

"""Introduce a plant in the garden."""

class Plant:
    """Create a plant with 3 attributes: name, height, age."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)

    print("=== Welcome to My Garden ===")
    print(f"Plant: {rose.name.capitalize()}")
    print(f"Height: {rose.height}cm")
    print(f"Age: {rose.age} days\n")
    print("=== End of Program ===")
