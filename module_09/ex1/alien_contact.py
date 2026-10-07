from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if (
            self.contact_type == ContactType.PHYSICAL
            and not self.is_verified
        ):
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses."
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) must include a received message"
            )

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 60)
    for contact_id in ("AC1234567890Z", "BAC9876Z"):
        print(f"Testing contact_id = '{contact_id}'")

        try:
            contact = AlienContact(
                contact_id=contact_id,
                timestamp=datetime(2027, 10, 10, 14, 30),
                location="Area 52, Nevada",
                contact_type=ContactType.TELEPATHIC,
                is_verified=True,
                signal_strength=8.5,
                message_received="Greetings from Zeta Reticuli",
                duration_minutes=450,
                witness_count=3,
            )
            hours, minutes = divmod(contact.duration_minutes, 60)

        except ValidationError as error:
            print()
            print("Validation failed:")
            for issue in error.errors():
                print(issue["msg"])

        else:
            print("Valid contact report:")
            print(f"ID: {contact.contact_id}")
            print(f"Type: {contact.contact_type.value}")
            print(f"Location: {contact.location}")
            print(f"Signal: {contact.signal_strength}/10")
            print(f"Duration: {hours} hours and {minutes} minutes")
            print(f"Witnesses: {contact.witness_count}")
            print(f"Message: {contact.message_received}")

        print()
        print("=" * 60)


if __name__ == "__main__":
    main()
