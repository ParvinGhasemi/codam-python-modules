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
            print("Height update rejected")
            return False
        self._height = height
        print(f"Height updated: {self.get_height():.1f}cm")
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
            print("Age update rejected")
            return False
        self._age = age
        print(f"Age updated: {self.get_age()} days")
        return True

    def get_height(self) -> float:
        """Return the plant height in centimeters."""
        return self._height

    def get_age(self) -> int:
        """Return the plant age in days."""
        return self._age

    def show(self) -> None:
        """Print the current plant information."""
        print(
            f"{self._name.capitalize()}: "
            f"{self.get_height():.1f}cm, {self._age} days old"
            )


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

    print("Current state: ", end="")
    rose.show()
