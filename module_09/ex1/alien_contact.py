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

from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL: str = "physical"
    TELEPATHIC: str = "telepathic"


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





def main() -> None:
    print("hi")

if __name__ == "__main__":
    main()
