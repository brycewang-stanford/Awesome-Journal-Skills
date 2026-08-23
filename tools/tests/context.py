"""Put ``tools/`` on the import path.

The tools import each other by bare module name (``from venue_lib import ROOT``)
because they are run as ``python3 tools/x.py``, which puts ``tools/`` on the path
automatically. Under ``unittest discover`` the working directory is the repository
root instead, so the tests re-create that condition explicitly.
"""

from __future__ import annotations

import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parent

if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
