# Sanskrit Metric Analyzer

A Flask-based web application for analyzing Sanskrit text metrics and patterns.

## Git Repository Information

This project is now version-controlled using Git. The repository is initialized and ready for collaborative development.

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

- Analyze Sanskrit text metrics and verse patterns
- Multiple metrical analysis types:
  - **Kandapadya**: 4-syllable metrical unit
  - **Shatpadi**: 6-line verse form (Shara, Kusuma, Bhoga, Bhamini, Parivardhini, Vardhaka)
  - **Ragale**: Irregular meter variations (Utsaha, Mandanila, Lalita)
  - **Vrutta**: Complex verse meters (Vidyunmaala, Maanavakam, Indravajra, Upendravajra, etc.)
  - **Laghu-Guru**: Light and heavy syllable analysis
- Web-based interface for text input and real-time analysis
- Full UTF-8 support for Devanagari script
- Automatic syllable classification and gana pattern recognition

## Recent Updates

### Version 1.0.1 - UTF-8 Encoding Fixes
- **Fixed**: Unicode encoding errors for Sanskrit Devanagari script
- **Changed**: All file operations in `modific.py` now explicitly use UTF-8 encoding
- **Impact**: Application now correctly processes and outputs Sanskrit text without character corruption
- **Files Modified**: 
  - `Akshara.txt` write operation (line 62)
  - `Normalized.txt` write operation (line 65)
  - `Chandassu.txt` write operations (lines 602, 647)
  - `laghu_Guru.txt` write operation (line 649)
  - `print_to_file()` method append operation (line 627)

### Version 1.0.0 - Initial Release
- Complete Flask-based Sanskrit metric analyzer
- Core analysis engine with three-module pipeline
- Web interface with multiple meter type analysis

## Installation

### Prerequisites
- Python 3.4 or higher
- pip (Python package manager)
- Git (for version control)

### Setup Steps

1. **Clone or Navigate to Repository** (for local setup):
```bash
cd "Sanskrit Metric Analyzer"
```

2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

3. **Verify Installation**:
```bash
python -c "import flask; print(f'Flask {flask.__version__} installed')"
```

## Project Statistics

- **Files**: 103 total (Python, HTML, CSS, JSON, data)
- **Lines of Code**: 31,000+ (including dependencies and static assets)
- **Core Modules**: 3 (Module1, Module2, Module3)
- **Meter Types Supported**: 45+
- **Routes Available**: 40+

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.1   | 2026-02-07 | UTF-8 encoding fixes for Devanagari support |
| 1.0.0   | 2019-04-27 | Initial release with Flask web interface |

---

**Last Updated**: February 7, 2026  
**Git Status**: ✓ Repository initialized and synced  
**Build Status**: ✓ All tests passing
