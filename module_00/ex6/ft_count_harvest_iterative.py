def ft_count_harvest_iterative() -> None:
    start: int = 1
    end: int = int(input("Days until harvest: "))
    for day in range(start, end + 1):
        print(f"Day {day}")
    print("Harvest time!")
