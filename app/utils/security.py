import hashlib


def generate_checksum(data: str):
    return hashlib.sha1(data.encode()).hexdigest()