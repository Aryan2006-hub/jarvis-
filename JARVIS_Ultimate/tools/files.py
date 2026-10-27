from pathlib import Path
import os

KNOWN_DIRS = {
    "downloads": Path.home() / "Downloads",
    "documents": Path.home() / "Documents",
    "desktop": Path.home() / "Desktop",
    "pictures": Path.home() / "Pictures",
}

def open_folder(name):
    path = KNOWN_DIRS.get(name.lower())
    if not path or not path.exists():
        return False, f"I couldn't find the {name} folder."
    os.startfile(str(path))
    return True, f"Opening {name}."

def list_folder(name):
    path = KNOWN_DIRS.get(name.lower())
    if not path or not path.exists():
        return []
    return [p.name for p in list(path.iterdir())[:30]]
