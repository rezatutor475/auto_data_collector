import unittest
from datetime import date, timedelta
from data_collector.models import PersonInfo
from data_collector.validators import validate_person_info

class TestPersonInfoModel(unittest.TestCase):

    def setUp(self):
        self.person = PersonInfo(
            full_name="Jane Doe",
            identity_card_number="AB123456",
            date_of_birth=date(1990, 1, 1),
            birth_place="Tehran",
            height_cm=170.5,
            weight_kg=65.0,
            measurements="34B",
            body_art="Piercing",
            body_type="Athletic",
            butt_type="Round",
            breast_size="Medium",
            education_level="Bachelor",
            marital_status="Single"
        )

    def test_model_fields_assignment(self):
        self.assertEqual(self.person.full_name, "Jane Doe")
        self.assertEqual(self.person.identity_card_number, "AB123456")
        self.assertEqual(self.person.birth_place, "Tehran")
        self.assertEqual(self.person.education_level, "Bachelor")
        self.assertEqual(self.person.marital_status, "Single")

    def test_date_of_birth_type(self):
        self.assertIsInstance(self.person.date_of_birth, date)

    def test_valid_height_range(self):
        self.assertTrue(50 <= self.person.height_cm <= 250)

    def test_valid_weight_range(self):
        self.assertTrue(30 <= self.person.weight_kg <= 300)

    def test_valid_measurements_format(self):
        self.assertRegex(self.person.measurements, r"\d{2,3}[A-Z]{1,3}")

    def test_validate_person_info(self):
        self.assertTrue(validate_person_info(self.person))

    def test_invalid_identity_card(self):
        self.person.identity_card_number = "###"
        self.assertFalse(validate_person_info(self.person))

    def test_underage_person(self):
        self.person.date_of_birth = date.today() - timedelta(days=17*365)
        self.assertFalse(validate_person_info(self.person))

    def test_invalid_education_level(self):
        self.person.education_level = "Unknown"
        self.assertFalse(validate_person_info(self.person))

    def test_invalid_marital_status(self):
        self.person.marital_status = "Complicated"
        self.assertFalse(validate_person_info(self.person))

if __name__ == '__main__':
    unittest.main()
