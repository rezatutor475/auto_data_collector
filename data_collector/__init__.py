"""
Auto Data Collector - Python Library

This library provides tools to collect, validate, and store structured personal information.
"""

from .models import PersonInfo
from .collector import collect_from_input, collect_from_dict, collect_from_json
from .storage import init_db, save_person, get_all_people, find_person_by_id
from .validators import validate_identity_card, validate_date_of_birth, validate_measurements
from . import utils

# Initialize database on import (optional, can be managed externally)
init_db()

# Convenience function for end users

def collect_and_save():
    """
    Collect information from user input and save it to storage.
    """
    person = collect_from_input()
    if validate_identity_card(person.identity_card_number):
        save_person(person)
        print("Person saved successfully.")
    else:
        print("Invalid identity card number.")

__all__ = [
    "PersonInfo",
    "collect_from_input",
    "collect_from_dict",
    "collect_from_json",
    "init_db",
    "save_person",
    "get_all_people",
    "find_person_by_id",
    "validate_identity_card",
    "validate_date_of_birth",
    "validate_measurements",
    "collect_and_save",
    "utils",
]

__version__ = "0.2.0"
__author__ = "Reza Torabi"
__license__ = "MIT"
