# مثال نحوه استفاده از کتابخانه auto_data_collector
from data_collector.collector import ManualCollector, APICollector, FileCollector
from data_collector.storage import SQLServerStorage
from data_collector.validators import validate_person_info
from data_collector.models import PersonInfo
import random

# تابع کمکی برای تست چند منبع جمع‌آوری اطلاعات
def collect_from_source(source):
    collector = source
    person_info = collector.collect()
    try:
        validate_person_info(person_info)
        return person_info
    except ValueError as e:
        print(f"Validation failed: {e}")
        return None

# شبیه‌سازی انتخاب تصادفی منبع اطلاعاتی
sources = [
    ManualCollector(),
    APICollector("http://api.example.com/person"),
    FileCollector("example_person.json")
]

selected_collector = random.choice(sources)
person_info = collect_from_source(selected_collector)

# اگر اعتبارسنجی موفقیت‌آمیز بود، ذخیره‌سازی انجام شود
if person_info:
    connection_string = "mssql+pyodbc://user:pass@localhost/your_db?driver=ODBC+Driver+17+for+SQL+Server"
    storage = SQLServerStorage(connection_string)

    try:
        storage.store_person_info(person_info)
        print("Person information saved successfully.")
    except Exception as e:
        print(f"Database error: {e}")
else:
    print("Data collection or validation failed. Not saving.")
