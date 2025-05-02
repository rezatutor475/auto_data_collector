import argparse
import logging
import sys
import os
import json
from data_collector.collector import ManualCollector, APICollector, FileCollector
from data_collector.validators import validate_person_info
from data_collector.storage import SQLServerStorage

def configure_logging(log_file=None):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            *( [logging.FileHandler(log_file)] if log_file else [] )
        ]
    )

def load_config(config_path="config.json"):
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def main():
    parser = argparse.ArgumentParser(description="Auto Data Collector CLI")
    parser.add_argument("--source", choices=["manual", "api", "file"], help="Data source: manual, api, or file")
    parser.add_argument("--file", type=str, help="Path to input file (for file source)")
    parser.add_argument("--api-url", type=str, help="URL to fetch data from API")
    parser.add_argument("--db-url", type=str, help="SQL Server connection string")
    parser.add_argument("--log", type=str, help="Optional log file path")
    parser.add_argument("--config", type=str, default="config.json", help="Path to configuration JSON file")
    args = parser.parse_args()

    # Load config file
    config = load_config(args.config)

    # Override config with CLI arguments if provided
    source = args.source or config.get("source", "manual")
    input_file = args.file or config.get("file")
    api_url = args.api_url or config.get("api_url")
    db_url = args.db_url or config.get("db_url")
    log_file = args.log or config.get("log_file")

    # Logging setup
    configure_logging(log_file)
    logging.info("Starting Auto Data Collector")

    # انتخاب کلکتور بر اساس ورودی
    try:
        if source == "manual":
            collector = ManualCollector()
        elif source == "api":
            if not api_url:
                raise ValueError("API URL is required when source is 'api'")
            collector = APICollector(api_url)
        elif source == "file":
            if not input_file:
                raise ValueError("Input file path is required when source is 'file'")
            if not os.path.exists(input_file):
                raise FileNotFoundError(f"File not found: {input_file}")
            collector = FileCollector(input_file)
        else:
            raise ValueError(f"Invalid source: {source}")
    except Exception as e:
        logging.error(f"Collector initialization failed: {e}")
        sys.exit(1)

    # جمع‌آوری و اعتبارسنجی
    try:
        person = collector.collect()
        validate_person_info(person)
        logging.info("Data collected and validated successfully")
    except Exception as e:
        logging.error(f"Data collection or validation failed: {e}")
        sys.exit(1)

    # ذخیره‌سازی
    try:
        if not db_url:
            raise ValueError("Database URL is required")
        storage = SQLServerStorage(db_url)
        storage.store_person_info(person)
        logging.info("Person info stored successfully")
    except Exception as e:
        logging.error(f"Failed to store person info: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
