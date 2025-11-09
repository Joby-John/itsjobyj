import os

MAINTENANCE_MODE = os.environ.get('MAINTENANCE_MODE', 'False').lower() == True