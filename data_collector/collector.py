from datetime import datetime
from typing import Optional, List
import json
import requests
from .models import PersonInfo

def collect_manual_input() -> PersonInfo:
    """
    Collect personal data manually via CLI input.
    """
    def input_with_prompt(prompt: str, optional: bool = False) -> Optional[str]:
        value = input(prompt)
        return value if value or not optional else None

    full_name = input_with_prompt("Full name: ")
    identity_card_number = input_with_prompt("Identity card number: ")
    dob_str = input_with_prompt("Date of birth (YYYY-MM-DD): ")
    date_of_birth = datetime.strptime(dob_str, "%Y-%m-%d").date()
    birth_place = input_with_prompt("Birth place: ")
    height_cm = float(input_with_prompt("Height (cm): "))
    weight_kg = float(input_with_prompt("Weight (kg): "))

    # Optional attributes
    measurements = input_with_prompt("Measurements (e.g. 32DD): ", optional=True)
    body_art = input_with_prompt("Body Art: ", optional=True)
    body_type = input_with_prompt("Body Type: ", optional=True)
    butt_type = input_with_prompt("Butt Type: ", optional=True)
    breast_size = input_with_prompt("Breast Size: ", optional=True)
    education_level = input_with_prompt("Level of Education: ", optional=True)
    marital_status = input_with_prompt("Marital Status: ", optional=True)

    return PersonInfo(
        full_name=full_name,
        identity_card_number=identity_card_number,
        date_of_birth=date_of_birth,
        birth_place=birth_place,
        height_cm=height_cm,
        weight_kg=weight_kg,
        measurements=measurements,
        body_art=body_art,
        body_type=body_type,
        butt_type=butt_type,
        breast_size=breast_size,
        education_level=education_level,
        marital_status=marital_status
    )

def collect_from_json_file(file_path: str) -> List[PersonInfo]:
    """
    Collect personal data from a local JSON file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [PersonInfo.from_dict(item) for item in data]

def collect_from_api(endpoint: str) -> List[PersonInfo]:
    """
    Collect personal data from a REST API.
    """
    response = requests.get(endpoint)
    response.raise_for_status()
    data = response.json()
    return [PersonInfo.from_dict(item) for item in data]
