import unittest
from unittest.mock import patch, MagicMock, mock_open
from data_collector.collector import ManualCollector, APICollector, FileCollector
from data_collector.models import PersonInfo
from datetime import date
import json

class TestManualCollector(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        'Jane Doe', 'XY123456', '1990-01-01', 'Tehran', '170', '65',
        '34C', 'Tattoo', 'Fit', 'Round', 'Large', 'Bachelor', 'Single'])
    def test_collect_manual_input(self, mock_input):
        collector = ManualCollector()
        person = collector.collect()
        self.assertIsInstance(person, PersonInfo)
        self.assertEqual(person.full_name, 'Jane Doe')

    @patch('builtins.input', side_effect=['', '', '', '', '', '', '', '', '', '', '', '', ''])
    def test_collect_manual_input_invalid(self, mock_input):
        collector = ManualCollector()
        person = collector.collect()
        self.assertIsInstance(person, PersonInfo)

class TestAPICollector(unittest.TestCase):

    @patch('requests.get')
    def test_collect_from_api(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'full_name': 'Ali Rezaei',
            'identity_card_number': 'CD654321',
            'date_of_birth': '1988-03-15',
            'birth_place': 'Mashhad',
            'height_cm': 175,
            'weight_kg': 70,
            'measurements': '38B',
            'body_art': 'None',
            'body_type': 'Average',
            'butt_type': 'Flat',
            'breast_size': 'Medium',
            'education_level': 'PhD',
            'marital_status': 'Single'
        }
        mock_get.return_value = mock_response

        collector = APICollector("http://api.example.com/person")
        person = collector.collect()
        self.assertIsInstance(person, PersonInfo)
        self.assertEqual(person.identity_card_number, 'CD654321')

    @patch('requests.get')
    def test_collect_from_api_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        collector = APICollector("http://api.example.com/person")
        with self.assertRaises(Exception):
            collector.collect()

class TestFileCollector(unittest.TestCase):

    def setUp(self):
        self.json_data = json.dumps({
            "full_name": "Sara Ahmadi",
            "identity_card_number": "EF987654",
            "date_of_birth": "1992-07-10",
            "birth_place": "Isfahan",
            "height_cm": 160,
            "weight_kg": 55,
            "measurements": "32D",
            "body_art": "None",
            "body_type": "Petite",
            "butt_type": "Round",
            "breast_size": "Small",
            "education_level": "Associate",
            "marital_status": "Married"
        })

    @patch('builtins.open', new_callable=mock_open)
    def test_collect_from_file(self, mock_file):
        mock_file.return_value.__enter__.return_value.read.return_value = self.json_data
        collector = FileCollector("fake_path.json")
        person = collector.collect()
        self.assertIsInstance(person, PersonInfo)
        self.assertEqual(person.birth_place, "Isfahan")

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_collect_from_file_not_found(self, mock_file):
        collector = FileCollector("missing.json")
        with self.assertRaises(FileNotFoundError):
            collector.collect()

if __name__ == '__main__':
    unittest.main()
