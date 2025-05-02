import unittest
from unittest.mock import patch, MagicMock
from data_collector.storage import SQLServerStorage
from data_collector.models import PersonInfo
from datetime import date

class TestSQLServerStorage(unittest.TestCase):

    def setUp(self):
        self.connection_string = "mssql+pyodbc://user:pass@localhost/dbname?driver=ODBC+Driver+17+for+SQL+Server"
        self.storage = SQLServerStorage(self.connection_string)
        self.person = PersonInfo(
            full_name="John Doe",
            identity_card_number="XYZ12345",
            date_of_birth=date(1985, 5, 15),
            birth_place="Shiraz",
            height_cm=180.0,
            weight_kg=80.0,
            measurements="36C",
            body_art="None",
            body_type="Slim",
            butt_type="Flat",
            breast_size="Small",
            education_level="Master",
            marital_status="Married"
        )

    @patch("sqlalchemy.create_engine")
    def test_store_person_info_success(self, mock_create_engine):
        mock_engine = MagicMock()
        mock_conn = MagicMock()
        mock_engine.connect.return_value.__enter__.return_value = mock_conn
        mock_create_engine.return_value = mock_engine

        self.storage.store_person_info(self.person)
        self.assertTrue(mock_conn.execute.called)

    @patch("sqlalchemy.create_engine")
    def test_store_person_info_failure(self, mock_create_engine):
        mock_engine = MagicMock()
        mock_engine.connect.side_effect = Exception("Connection failed")
        mock_create_engine.return_value = mock_engine

        with self.assertRaises(Exception):
            self.storage.store_person_info(self.person)

    @patch("sqlalchemy.create_engine")
    def test_fetch_all_people(self, mock_create_engine):
        mock_engine = MagicMock()
        mock_conn = MagicMock()
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [
            ("John Doe", "XYZ12345", date(1985, 5, 15), "Shiraz", 180.0, 80.0, "36C", "None", "Slim", "Flat", "Small", "Master", "Married")
        ]
        mock_conn.execute.return_value = mock_result
        mock_engine.connect.return_value.__enter__.return_value = mock_conn
        mock_create_engine.return_value = mock_engine

        results = self.storage.fetch_all_people()
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].full_name, "John Doe")

    @patch("sqlalchemy.create_engine")
    def test_delete_person_by_id_success(self, mock_create_engine):
        mock_engine = MagicMock()
        mock_conn = MagicMock()
        mock_engine.connect.return_value.__enter__.return_value = mock_conn
        mock_create_engine.return_value = mock_engine

        self.storage.delete_person_by_id("XYZ12345")
        self.assertTrue(mock_conn.execute.called)

    @patch("sqlalchemy.create_engine")
    def test_delete_person_by_id_failure(self, mock_create_engine):
        mock_engine = MagicMock()
        mock_engine.connect.side_effect = Exception("Deletion failed")
        mock_create_engine.return_value = mock_engine

        with self.assertRaises(Exception):
            self.storage.delete_person_by_id("XYZ12345")

if __name__ == '__main__':
    unittest.main()
