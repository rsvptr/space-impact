# Filename: resource_path.py

# Function: Utility file that defines the resource path and how to open files from a base path when provided.

# Importing all modules required for proper functioning of the code in this file.

import os
import sys

# Resource path information defined below.

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS # Stores the absolute (base) path to the assets in sys._MEIPASS. 
    except Exception:
        base_path = os.path.abspath(".") # Returns a normalized version of the pathname "."

    return os.path.join(base_path, relative_path) # Returns a string which represents the concatenated path.
