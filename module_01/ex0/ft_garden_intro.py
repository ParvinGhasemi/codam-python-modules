#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    lavendar = Plant("hi", 12, 14)
    print("=== Welcome to My Garden ===")
    print(f"Plant: {"rose".capitalize()}")
    print(f"Height: {rose.height}cm")
    print(f"Age: {rose.age} days\n")
    print("=== End of Program ===")
