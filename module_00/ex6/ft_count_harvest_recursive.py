def ft_count_harvest_recursive() -> None:
    end: int = int(input("Days until harvest: "))

    def recursive_printer(day: int) -> None:
        if day <= end:
            print(f"Day {day}")
            recursive_printer(day + 1)
        return

    recursive_printer(1)
    print("Harvest time!")
