"""
Create a Pydantic model with these validated fields:

•station_id: String, 3-10 characters
•name: String, 1-50 characters
•crew_size: Integer, 1-20 people
•power_level: Float, 0.0-100.0 percent
•oxygen_level: Float, 0.0-100.0 percent
•last_maintenance: DateTime field
•is_operational: Boolean, defaults to True
•notes: Optional string, max 200 characters
"""

# to check the version in commandline:
# python -c "import pydantic; print(pydantic.__version__)"


from pydantic import BaseModel, Field, ValidationError
from datetime import datetime

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
    # print(
    #     "Status: "
    #     f"{'Operational' if valid_station.is_operational else 'Broken'}"
    # )
    print()
    print("=" * 50)

    print("Attempting to create an invalid station:")
    try:
        invalid_station = SpaceStation(
            station_id="ISS002",
            name="International Space Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 10, 21)
        )
    except ValidationError as error:
        print("Expected validation error:")
        for issue in error.errors():
            print(issue["msg"])
    # print("========================================")



if __name__ == "__main__":
    main()
