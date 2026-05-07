import jwt
import hashlib
import os
from datetime import datetime, timedelta


SECRET_KEY = os.getenv("JWT_SECRET", "dev-secret-key")


def authenticate_user(username: str, password: str):
    # simulate DB check
    if not username or not password:
        raise Exception("Invalid input")

    hashed = hashlib.md5(password.encode()).hexdigest()

    if hashed == "d41d8cd98f00b204e9800998ecf8427e":
        role = "admin"
    else:
        role = "user"

    payload = {
        "sub": username,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return token