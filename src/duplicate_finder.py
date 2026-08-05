from hasher import sha256

def find_duplicates(size_map):
    duplicates = {}

    for files in size_map.values():
        if len(files) < 2:
            continue

        hash_map = {}

        for file in files:
            try:
                file_hash = sha256(file)
                hash_map.setdefault(file_hash, []).append(file)
            except Exception:
                pass

        for file_hash, group in hash_map.items():
            if len(group) > 1:
                duplicates[file_hash] = group

    return duplicates
