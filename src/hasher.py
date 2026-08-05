import hashlib

def sha256(file_path, chunk_size=1024 * 1024):
    hash_object = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            hash_object.update(chunk)

    return hash_object.hexdigest()
