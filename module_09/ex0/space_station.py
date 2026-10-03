from pydantic import BaseModel, Field, ValidationError
from datetime import datetime

"""
python -m pip install mypy "pydantic>=2,<3"
python -m mypy --strict space_station.py
"""


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    valid_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2026, 9, 21)
    )

    print()
    print("Space Station Data Validation")
    print("=" * 50)
    print("Valid station created:")
    print(f"ID: {valid_station.station_id}")
    print(f"Name: {valid_station.name}")
    print(f"Crew: {valid_station.crew_size} people")
    print(f"Power: {valid_station.power_level}%")
    print(f"Oxygen: {valid_station.oxygen_level}%")

    status: str = (
        "Operational" if valid_station.is_operational else "Not Operational"
    )
    print(f"Status: {status}")

    print()
    print("=" * 60)

    print()
    print("Attempting to create an invalid station:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="International Space Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 12, 21)
        )
    except ValidationError as error:
        print("Expected validation error:")
        print()
        for issue in error.errors():
            field: str | int = issue["loc"][0]
            message: str = issue["msg"]
            if issue["type"] == "missing":
                print(f" {field}: {message}")
            else:
                print(f" {field}: {message} - (received: {issue["input"]!r})")
            print()

    print("=" * 60)
    print()

    try:
        print("Testing what happens if we feed variables with string:")
        print()
        converted_station = SpaceStation.model_validate({
            "station_id": "ISS003",
            "name": "Conversion Test",
            "crew_size": "six",
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2026-12-21T14:30:00",
        })
    except ValidationError as error:
        print("<<< !!!!! Something went wrong - Conversion Failed !!!!! >>>")
        print()
        for issue in error.errors():
            print(f"{issue['loc'][0]}: {issue['msg']}")
        print()
        print(" **********  End of Errors    ********** ")
        print()
    else:
        print("If crew and datetime are in correct format but as strings")
        print(f"    crew_size:      {converted_station.crew_size}")
        print(f"    crew_size type: {type(converted_station.crew_size)}")

        print()
        print(f"    date:   {converted_station.last_maintenance}")
        print(f"    type of date:  {type(converted_station.last_maintenance)}")


if __name__ == "__main__":
    main()
