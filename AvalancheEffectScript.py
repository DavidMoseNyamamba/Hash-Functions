import hashlib
password1 = "mySecurePassword123"
password2 = "mySecurePassword124"

print("SHA-256 (1):", hashlib.sha256(password1.encode()).hexdigest())
print("SHA-256 (2):", hashlib.sha256(password2.encode()).hexdigest())