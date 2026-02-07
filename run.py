"""
Entry point for Sanskrit Metric Analyzer Flask Application
Runs the Flask development server
"""
import os
from app import app

if __name__ == '__main__':
    environment = os.environ.get('FLASK_ENV', 'development')
    app.run(debug=True, host='127.0.0.1', port=5000)
