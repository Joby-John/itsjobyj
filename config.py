import os

# Read the ENV variable. 
# If it's not set, default to 'False'.
# .lower() == 'true' handles 'True', 'true', or 'TRUE'.
MAINTENANCE_MODE = os.environ.get('MAINTENANCE_MODE', 'False').lower() == 'true'