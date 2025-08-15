import hashlib

password = "mySecurePassword123"
print("MD5:     ", hashlib.md5(password.encode()).hexdigest())
print("SHA-1:   ", hashlib.sha1(password.encode()).hexdigest())
print("SHA-256: ", hashlib.sha256(password.encode()).hexdigest())