import jwt
import hashlib
from datetime import datetime, timedelta

SECRET_KEY = "temporary-dev-secret"


def login_user(username: str, password: str):
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(hours=12),
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return token