def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_name: str = seed_type.capitalize()

    match unit:
        case "packets":
            print(f"{seed_name} seeds: {quantity} packets available")
        case "grams":
            print(f"{seed_name} seeds: {quantity} grams total")
        case "area":
            print(f"{seed_name} seeds: covers {quantity} square meters")
        case _:
            print("Unknown unit type")
