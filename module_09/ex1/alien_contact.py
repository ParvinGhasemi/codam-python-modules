"""
ContactType Enum
Define contact types: radio, visual, physical, telepathic
"""

"""
contact_id: String, 5-15 characters
•timestamp: DateTime of contact
•location: String, 3-100 characters
•contact_type: ContactType enum
•signal_strength: Float, 0.0-10.0 scale
•duration_minutes: Integer, 1-1440 (max 24 hours)
•witness_count: Integer, 1-100 people
•message_received: Optional string, max 500 characters
•is_verified: Boolean, defaults to False
"""

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
                duration_minutes=450,
                witness_count=2,
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

        print()
        print("=" * 60)

if __name__ == "__main__":
    main()
