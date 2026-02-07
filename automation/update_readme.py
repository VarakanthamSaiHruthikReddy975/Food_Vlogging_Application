import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional

# copy the python version into the read me file
def get_python_version() -> str:
    result = subprocess.run(
        ["python", "--version"],
        capture_output=True
        )
    return result.stdout.strip().replace("Python ", "")

