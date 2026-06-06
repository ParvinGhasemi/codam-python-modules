#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height) -> None:
        self._height = height

    def set_age(self, age) -> None:
        self._age = age
