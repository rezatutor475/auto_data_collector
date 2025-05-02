import re
from datetime import date
from .models import PersonInfo

def validate_identity_card_number(value: str) -> bool:
    """
    Must be alphanumeric and 6-20 characters.
    """
    return bool(re.fullmatch(r"[A-Za-z0-9]{6,20}", value))

def validate_date_of_birth(value: date) -> bool:
    """
    Must be in the past and person must be at least 18 years old.
    """
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    return value < today and age >= 18

def validate_height(height: float) -> bool:
    return 50 <= height <= 250

def validate_weight(weight: float) -> bool:
    return 30 <= weight <= 300

def validate_measurements(measurements: str) -> bool:
    """
    Basic format validation: e.g. 32DD, 34B, etc.
    """
    return bool(re.fullmatch(r"\d{2,3}[A-Z]{1,3}", measurements)) if measurements else True

def validate_education_level(level: str) -> bool:
    """
    Checks if education level is within accepted categories.
    """
    accepted_levels = {"High School", "Diploma", "Bachelor", "Master", "PhD"}
    return level in accepted_levels if level else True

def validate_marital_status(status: str) -> bool:
    """
    Checks marital status.
    """
    accepted_statuses = {"Single", "Married", "Divorced", "Widowed"}
    return status in accepted_statuses if status else True

def validate_non_empty_string(value: str, min_len: int = 2, max_len: int = 100) -> bool:
    return bool(value) and min_len <= len(value.strip()) <= max_len

def validate_person_info(info: PersonInfo) -> bool:
    return all([
        validate_non_empty_string(info.full_name),
        validate_identity_card_number(info.identity_card_number),
        validate_date_of_birth(info.date_of_birth),
        validate_non_empty_string(info.birth_place),
        validate_height(info.height_cm),
        validate_weight(info.weight_kg),
        validate_measurements(info.measurements),
        validate_education_level(info.education_level),
        validate_marital_status(info.marital_status)
    ])
