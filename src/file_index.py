from pathlib import Path

def group_by_size(folder):
    size_map = {}

    for file in Path(folder).rglob("*"):
        if file.is_file():
            try:
                size = file.stat().st_size
                size_map.setdefault(size, []).append(file)
            except Exception:
                pass

    return size_map
