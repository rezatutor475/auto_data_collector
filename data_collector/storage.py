import pyodbc
from typing import List, Optional
from .models import PersonInfo

# Connection settings (replace with your own credentials)
CONN_STRING = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=PersonDB;'
    'UID=your_username;'
    'PWD=your_password'
)

def get_connection():
    return pyodbc.connect(CONN_STRING)

def init_db():
    """
    Initialize the database table if it doesn't exist.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='People' AND xtype='U')
        CREATE TABLE People (
            full_name NVARCHAR(100),
            identity_card_number NVARCHAR(50) PRIMARY KEY,
            date_of_birth DATE,
            birth_place NVARCHAR(100),
            height_cm FLOAT,
            weight_kg FLOAT,
            measurements NVARCHAR(50),
            body_art NVARCHAR(100),
            body_type NVARCHAR(100),
            butt_type NVARCHAR(100),
            breast_size NVARCHAR(50),
            education_level NVARCHAR(100),
            marital_status NVARCHAR(50)
        )
    ''')
    conn.commit()
    conn.close()

def save_person(info: PersonInfo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO People VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        info.full_name,
        info.identity_card_number,
        info.date_of_birth,
        info.birth_place,
        info.height_cm,
        info.weight_kg,
        info.measurements,
        info.body_art,
        info.body_type,
        info.butt_type,
        info.breast_size,
        info.education_level,
        info.marital_status
    ))
    conn.commit()
    conn.close()

def update_person(info: PersonInfo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE People SET
            full_name = ?,
            date_of_birth = ?,
            birth_place = ?,
            height_cm = ?,
            weight_kg = ?,
            measurements = ?,
            body_art = ?,
            body_type = ?,
            butt_type = ?,
            breast_size = ?,
            education_level = ?,
            marital_status = ?
        WHERE identity_card_number = ?
    ''', (
        info.full_name,
        info.date_of_birth,
        info.birth_place,
        info.height_cm,
        info.weight_kg,
        info.measurements,
        info.body_art,
        info.body_type,
        info.butt_type,
        info.breast_size,
        info.education_level,
        info.marital_status,
        info.identity_card_number
    ))
    conn.commit()
    conn.close()

def delete_person(identity_card_number: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM People WHERE identity_card_number = ?', (identity_card_number,))
    conn.commit()
    conn.close()

def get_all_people() -> List[PersonInfo]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM People')
    rows = cursor.fetchall()
    conn.close()
    return [PersonInfo(*row) for row in rows]

def find_person_by_id(identity_card_number: str) -> Optional[PersonInfo]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM People WHERE identity_card_number = ?', (identity_card_number,))
    row = cursor.fetchone()
    conn.close()
    return PersonInfo(*row) if row else None
