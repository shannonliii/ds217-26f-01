# SUPPLIED BLOCK: do not edit this block.
import sys
from pathlib import Path

PROJECT_LABEL = "DataSci 217 Assignment 01"
python_family = str(sys.version_info.major) + "." + str(sys.version_info.minor)
script_filename = Path(__file__).name
# END SUPPLIED BLOCK

print(f"Python family: {python_family}")
print(f"Project: {PROJECT_LABEL}")
print(f"Script: {script_filename}")
