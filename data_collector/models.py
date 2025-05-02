from dataclasses import dataclass, asdict
from datetime import date, datetime
from typing import Optional, Dict, Any
import json

@dataclass
class PersonInfo:
    """
    Data model representing personal information of an individual.
    """
    full_name: str
    identity_card_number: str
    date_of_birth: date
    birth_place: str
    height_cm: float
    weight_kg: float
    measurements: Optional[str] = None
    body_art: Optional[str] = None
    body_type: Optional[str] = None
    butt_type: Optional[str] = None
    breast_size: Optional[str] = None
    education_level: Optional[str] = None
    marital_status: Optional[str] = None

    def age(self, on_date: Optional[date] = None) -> int:
        """
        Calculate age based on date_of_birth.
        """
        today = on_date or date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert PersonInfo instance to a dictionary.
        """
        return asdict(self)

    def to_json(self) -> str:
        """
        Convert PersonInfo instance to a JSON string.
        """
        return json.dumps(self.to_dict(), default=str, ensure_ascii=False)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PersonInfo":
        """
        Create a PersonInfo instance from a dictionary.
        """
        data = data.copy()
        if isinstance(data.get("date_of_birth"), str):
            data["date_of_birth"] = datetime.strptime(data["date_of_birth"], "%Y-%m-%d").date()
        return cls(**data)

    @classmethod
    def from_json(cls, json_str: str) -> "PersonInfo":
        """
        Create a PersonInfo instance from a JSON string.
        """
        data = json.loads(json_str)
        return cls.from_dict(data)
