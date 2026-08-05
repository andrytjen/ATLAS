from pathlib import Path
from hasher import sha256

def scan_folder(folder):
    hashes = {}

    for file in Path(folder).rglob("*"):
        if file.is_file():
            try:
                file_hash = sha256(file)

                hashes.setdefault(file_hash, []).append(file)

            except Exception:
                pass

    return hashes
