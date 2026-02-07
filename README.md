# Sanskrit Metric Analyzer

A Flask-based web application for analyzing Sanskrit text metrics and patterns.

## Project Structure

```
Sanskrit_Metric_Analyzer/
├── app.py                 # Main Flask application (do not modify)
├── run.py                 # Entry point for running the application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── config/               # Configuration directory
│   ├── __init__.py
│   └── settings.py       # Application settings
├── modules/              # Core processing modules
│   ├── __init__.py
│   ├── chandassu.py
│   ├── modific.py
│   └── modific-temp.py
├── data/                 # Data files directory
│   ├── Akshara.txt
│   ├── Chandassu.txt
│   ├── Kandapadya.txt
│   └── ... (other data files)
├── docs/                 # Documentation directory
│   └── doc-details-sanskrit
├── static/               # Static files (CSS, JS, images)
│   ├── bootstrap.min.css
│   ├── images/
│   └── styles/
└── templates/            # HTML templates
    ├── Home.html
    ├── Chandassu.html
    ├── Laghu_Guru.html
    └── ... (other templates)
```

## Features

- Analyze Sanskrit text metrics
- Various metrical pattern analysis (Chandassu, Kandapadya, etc.)
- Web-based interface for text input and analysis
- Support for multiple Sanskrit script analysis

## Installation

1. Install Python 3.4+
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Development Mode
```bash
python run.py
```

The application will be available at `http://localhost:5000`

### Using Gunicorn (Production)
```bash
gunicorn run:app
```

## Usage

1. Navigate to the home page
2. Select the metric analysis type (Chandassu, Kandapadya, Laghu-Guru, etc.)
3. Enter or upload Sanskrit text
4. View the analysis results

## Modules

- **chandassu.py**: Core module for Chandassu (poetic meter) analysis
- **modific.py**: Text modification and processing utilities
- **modific-temp.py**: Temporary modification functions

## File Paths

All data files are expected in the root directory or data/ directory. The application uses relative paths for file operations.

## Notes

- Ensure all text files are encoded in UTF-8
- Sanskrit Unicode ranges are handled automatically
- The application processes inputs through Python scripts in the modules directory
