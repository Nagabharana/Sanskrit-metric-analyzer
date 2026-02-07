# Sanskrit Metric Analyzer

A Flask-based web application for analyzing Sanskrit text metrics and patterns.

## Git Repository Information

This project is now version-controlled using Git. The repository is initialized and ready for collaborative development.

### Getting Started with Git

**Clone the Repository** (if available on a remote):
```bash
git clone <repository-url>
cd "Sanskrit Metric Analyzer"
```

**Local Repository**:
- Repository Location: `e:\BACKUP\Sanskrit Metric Analyzer\.git`
- Default Branch: `master`
- Current Commit: `024cd77` (Initial commit)

### Common Git Commands

**Check Status**:
```bash
git status
```

**View Commit History**:
```bash
git log --oneline
```

**Create a New Branch**:
```bash
git branch feature-name
git checkout feature-name
# or: git switch feature-name
```

**Stage and Commit Changes**:
```bash
git add .                    # Stage all changes
git commit -m "Description"  # Commit with message
```

**Push to Remote** (after configuring remote):
```bash
git remote add origin <repository-url>
git branch -M main          # Rename to main (optional)
git push -u origin main
```

**View Changes**:
```bash
git diff                     # Unstaged changes
git diff --staged            # Staged changes
```

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

## Development Workflow

### Making Changes with Git

**1. Create a Feature Branch**:
```bash
git checkout -b feature/improve-analysis
```

**2. Make Your Changes**:
- Edit files as needed
- Test thoroughly with sample Sanskrit text

**3. Stage and Commit**:
```bash
git status                          # Check what changed
git add <filename>                  # Stage specific files
# or
git add .                           # Stage all changes

git commit -m "Add feature description"
```

**4. View Your Commits**:
```bash
git log --oneline -5                # Show last 5 commits
git show 024cd77                    # View specific commit details
```

**5. Merge Back to Master** (when ready):
```bash
git checkout master
git merge feature/improve-analysis
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

## Analysis Pipeline

The Sanskrit metric analysis uses a three-stage processing pipeline:

### Stage 1: Line Partition (Module1)
- **Input**: Raw Sanskrit text from user or file
- **Process**: Breaks text into aksharas (syllables) using linguistic rules
- **Output**: `Akshara.txt`, `Normalized.txt`
- **Class**: `modific.Module1.line_partition()`

### Stage 2: Syllable Classification (Module2)
- **Input**: Akshara list from Module1
- **Process**: Classifies each syllable as लघु (light/short) or गुरु (heavy/long)
- **Output**: Classification map and laghu-guru list
- **Class**: `modific.Module2.laghu_guru()`

### Stage 3: Meter Analysis (Module3)
- **Input**: Original aksharas + classification from Module2
- **Process**: Identifies verse meter type by matching against 45+ predefined patterns
- **Output**: `Chandassu.txt` (meter identification), `laghu_Guru.txt` (pattern display)
- **Class**: `modific.Module3.chandassu()`

## Modules Detail

### modific.py
Main analysis engine containing three modules:
- **Module1**: Syllable decomposition using `line_partition()`
- **Module2**: Light/heavy classification using `laghu_guru()`
- **Module3**: Meter identification using `chandassu()`

All file operations use UTF-8 encoding for proper Devanagari support.

### app.py  
Flask application with 40+ routes for:
- Web interface serving
- User input handling
- Analysis execution via `run_python_script()`
- Result display and formatting



## File Paths

All data files are expected in the root directory or data/ directory. The application uses relative paths for file operations.

## Encoding & Localization

- **Character Set**: UTF-8 (required for Devanagari script)
- **Font Support**: Supports all Unicode Devanagari characters (U+0900 - U+097F)
- **File Encoding**: All input/output files use UTF-8 encoding
- **Script Support**: Sanskrit, Hindi, and other Indic scripts

## Git Configuration

### Local Configuration
Repository Details:
- **Repository Path**: `e:\BACKUP\Sanskrit Metric Analyzer\.git`
- **User Name**: Developer
- **User Email**: developer@localhost
- **Default Branch**: master
- **Initial Commit**: 024cd77

### Viewing Configuration
```bash
git config --list                   # Show all configuration
git config user.name               # Show current user
git config user.email              # Show current email
```

### Updating Configuration
```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Setting Up Remote Repository
```bash
git remote add origin https://github.com/your-user/sanskrit-analyzer.git
git branch -M main
git push -u origin main
```

## Troubleshooting

### Common Issues

**1. Python Import Errors**
```bash
# Ensure dependencies are installed
pip install -r requirements.txt --upgrade

# Verify Flask installation
python -c "import flask; print(flask.__version__)"
```

**2. File Encoding Errors**
- Ensure all text files are saved as UTF-8
- Check that `modific.py` has `encoding='utf-8'` in all file operations

**3. Git LF/CRLF Warnings**
```bash
# Configure Git line endings (Windows)
git config core.autocrlf true

# Configure Git line endings (Mac/Linux)
git config core.autocrlf input
```

**4. Flask Port Already in Use**
```bash
# Run on different port
python run.py --port 5001

# Or kill the existing process (Windows PowerShell)
Stop-Process -Name python
```

## Contributing

Contributions are welcome! Here's the process:

1. **Fork or Clone** the repository
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Make your changes** and test thoroughly
4. **Commit with clear messages**:
   ```bash
   git commit -m "Add brief description of changes"
   ```
5. **Push to your branch**:
   ```bash
   git push origin feature/your-feature
   ```
6. **Create a Pull Request** with a description of your changes

### Code Standards
- Use UTF-8 encoding for all files
- Add comments for complex algorithms
- Test with sample Sanskrit texts
- Update README.md if behavior changes

## Support & Documentation

- **Framework**: Flask 2.3.3
- **Python**: 3.4+
- **Dependencies**: See [requirements.txt](requirements.txt)
- **Documentation**: See [FRAMEWORK_STRUCTURE.md](FRAMEWORK_STRUCTURE.md)

## License & Attribution

This project analyzes Sanskrit metrics based on classical Chandas (prosody) theory.

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
