# Playwright with Pytest Framework

This is a test automation framework using Playwright with Pytest.

## Project Structure
```
├── pages/          # Page Object Models
│   └── base_page.py
├── tests/          # Test files
│   └── test_example.py
├── conftest.py     # Pytest fixtures and configuration
└── requirements.txt # Project dependencies
```

## Setup Instructions

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:
```bash
playwright install
```

## Running Tests

To run all tests:
```bash
pytest
```

To run tests with detailed output:
```bash
pytest -v
```

To run a specific test file:
```bash
pytest tests/test_example.py
```

## Additional Configuration

- Tests are configured to run in headless mode by default
- Use `--headed` flag to run tests in headed mode: `pytest --headed`
- Use `-k` flag to run specific test by name: `pytest -k "test_name"`
