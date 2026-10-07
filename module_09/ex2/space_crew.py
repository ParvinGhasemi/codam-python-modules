from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum


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
    officer = CrewMember(
        member_id="CM001",
        name="Alex Morgan",
        rank=Rank.OFFICER,
        age=30,
        specialization="Navigation",
        years_experience=2,
    )

    captain = CrewMember(
        member_id="CM002",
        name="Sarah Connor",
        rank=Rank.CAPTAIN,
        age=42,
        specialization="Mission Command",
        years_experience=3,
    )

    captain = CrewMember(
        member_id="CM002",
        name="Sarah Connor",
        rank=Rank.CAPTAIN,
        age=42,
        specialization="Mission Command",
        years_experience=3,
    )

    test_cases = [
        ("Crew without a leader", [officer]),
        ("Crew with a leader", [officer, captain]),
    ]

    for description, crew in test_cases:
        print(description)
        print("=" * 40)

        try:
            mission = SpaceMission(
                mission_id="M2026_MARS",
                mission_name="Mars Exploration",
                destination="Mars",
                launch_date=datetime(2026, 12, 1),
                duration_days=400,
                crew=crew,
                budget_millions=2500.0,
            )
        except ValidationError as error:
            print("Validation failed:")
            for issue in error.errors():
                print(issue["msg"])
        else:
            print(f"Valid mission: {mission.mission_name}")
            for member in mission.crew:
                print(f"- {member.name}: {member.rank.value}")

        print()


if __name__ == "__main__":
    main()
