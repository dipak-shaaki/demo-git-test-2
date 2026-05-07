import os
import requests

REPORT_DIR = "reports"


def fetch_external_data(url: str):
    # risky external call
    response = requests.get(url)
    return response.text


def generate_report(user_id: str, external_data=None):
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    file_path = f"{REPORT_DIR}/{user_id}_report.txt"

    with open(file_path, "w") as f:
        f.write(f"Report for user: {user_id}\n")

        if external_data:
            f.write("\nExternal Data:\n")
            f.write(external_data)

    return file_path