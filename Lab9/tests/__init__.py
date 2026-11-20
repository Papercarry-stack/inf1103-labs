import os
import sys

# Make the project's modules importable when tests run from any directory.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
