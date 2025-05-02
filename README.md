# Auto Data Collector

Auto Data Collector is a Python library for collecting, validating, and storing personal data from various sources such as manual input, files, or APIs.

## Features

* Support for manual, file-based, and API-based data collection
* Built-in data validation
* Storage support for Microsoft SQL Server
* Configurable logging
* Flexible configuration using a JSON file

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the main application with specific source and database connection:

```bash
python -m auto_data_collector --source api --api-url https://api.example.com/person --db-url "mssql+pyodbc://user:pass@server/db?driver=ODBC+Driver+17+for+SQL+Server"
```

Or use a configuration file:

```bash
python -m auto_data_collector --config config.json
```

## Project Structure

```
auto_data_collector/
├── data_collector/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   ├── collector.py
│   ├── validators.py
│   └── utils.py
├── tests/
├── examples/
├── config.json
├── README.md
├── setup.py
└── requirements.txt
```

## Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a Pull Request

Before submitting, please ensure tests are passing:

```bash
pytest
```

## License

[MIT License](LICENSE)
