from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
import sys


GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)  # 1&12: membr
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            member.rank in (Rank.CAPTAIN, Rank.COMMANDER)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_count += 1
            if experienced_count * 2 < len(self.crew):
                raise ValueError(
                    "Long missions require at least 50% experienced crew"
                )

        for member in self.crew:
            if not member.is_active:
                raise ValueError(
                    f"Crew member {member.name} must be active"
                )
        return self


def main() -> None:
    commander = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=42,
        specialization="Mission Command",
        years_experience=15,
    )

    lieutenant = CrewMember(
        member_id="CM002",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=35,
        specialization="Navigation",
        years_experience=8,
    )

    officer = CrewMember(
        member_id="CM003",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=28,
        specialization="Engineering",
        years_experience=3,
    )

    print("Space Mission Crew Validation")
    print("=" * 41)

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2027, 1, 15),
            duration_days=900,
            crew=[commander, lieutenant, officer],
            budget_millions=2500.0,
        )
    except ValidationError as error:
        print(f"{RED}Unexpected validation error:{RESET}")
        for issue in error.errors():
            print(issue["msg"])
    else:
        print(f"{GREEN}Valid mission created:{RESET}")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")

        for member in mission.crew:
            print(
                f"  - {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )

    print("=" * 41)

    # This crew has enough experience, but no Captain or Commander.
    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2027, 1, 15),
            duration_days=900,
            crew=[lieutenant, officer],
            budget_millions=2500.0,
        )
    except ValidationError as error:
        print(f"{RED}Expected validation error:{RESET}")
        for issue in error.errors():
            print(issue["msg"])
    else:
        print(f"{RED}CHECK FAILED: mission should be rejected.{RESET}")


def test_main() -> None:
    captain = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=Rank.CAPTAIN,
        age=42,
        specialization="Mission Command",
        years_experience=5,
    )

    officer = CrewMember(
        member_id="CM002",
        name="Alex Morgan",
        rank=Rank.OFFICER,
        age=30,
        specialization="Navigation",
        years_experience=2,
    )

    junior_captain = CrewMember(
        member_id="CM003",
        name="Jamie Lee",
        rank=Rank.CAPTAIN,
        age=28,
        specialization="Mission Command",
        years_experience=4,
    )

    inactive_officer = CrewMember(
        member_id="CM004",
        name="Robin Taylor",
        rank=Rank.OFFICER,
        age=35,
        specialization="Engineering",
        years_experience=8,
        is_active=False,
    )

    # Description, mission ID, days, crew, expected success.
    test_cases = [
        (
            "Valid mission",
            "M2026_MARS",
            180,
            [captain, officer],
            True,
        ),
        (
            "Invalid ID prefix",
            "X2026_MARS",
            180,
            [captain, officer],
            False,
        ),
        (
            "No Captain or Commander",
            "M2026_MARS",
            180,
            [officer],
            False,
        ),
        (
            "Long mission without enough experience",
            "M2026_MARS",
            366,
            [junior_captain, officer],
            False,
        ),
        (
            "Long mission with exactly 50% experienced crew",
            "M2026_MARS",
            366,
            [captain, officer],
            True,
        ),
        (
            "Exactly 365 days: experience rule does not apply",
            "M2026_MARS",
            365,
            [junior_captain, officer],
            True,
        ),
        (
            "Inactive crew member",
            "M2026_MARS",
            180,
            [captain, inactive_officer],
            False,
        ),
    ]

    for description, mission_id, days, crew, should_pass in test_cases:
        print("=" * 60)
        print(description)
        print(f"Expected: {'accepted' if should_pass else 'rejected'}")

        try:
            mission = SpaceMission(
                mission_id=mission_id,
                mission_name="Mars Exploration",
                destination="Mars",
                launch_date=datetime(2027, 1, 15),
                duration_days=days,
                crew=crew,
                budget_millions=2500.0,
            )
        except ValidationError as error:
            print(f"{RED}Result: rejected{RESET}")
            for issue in error.errors():
                print(f"{RED}  {issue['msg']}{RESET}")

            if should_pass:
                print(
                    f"{RED}CHECK FAILED: "
                    f"this mission should be valid.{RESET}"
                )
            else:
                print(f"{GREEN}Check passed.{RESET}")

        else:
            print(f"{GREEN}Result: accepted{RESET}")
            print(f"Mission: {mission.mission_name}")
            print(f"Duration: {mission.duration_days} days")
            print("Crew:")
            for member in mission.crew:
                print(f"  - {member.name} ({member.rank.value})")

            if should_pass:
                print(f"{GREEN}Check passed.{RESET}")
            else:
                print(
                    f"{RED}CHECK FAILED: "
                    f"this mission should be rejected.{RESET}"
                )

        print()


if __name__ == "__main__":
    if sys.argv[1:] == ["--tests"]:
        test_main()
    else:
        main()
