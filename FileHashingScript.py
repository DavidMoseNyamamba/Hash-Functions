import hashlib

def hash_file(filename, algo):
    h = getattr(hashlib, algo)()
    with open(filename, 'rb') as f:
        chunk = f.read()
        h.update(chunk)
    return h.hexdigest()

print("SHA-256 (file):", hash_file("sample.txt", "sha256"))