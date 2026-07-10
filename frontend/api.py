import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"


def chat(message):

    response = requests.post(
        f"{BASE_URL}/chat",
        json={"message": message}
    )

    return response.json()


def report(file):

    response = requests.post(
        f"{BASE_URL}/report/upload",
        files={
            "file": (
                file.name,
                file,
                "application/pdf"
            )
        }
    )

    response.raise_for_status()

    return response.json()

def vision(file):

    file.seek(0)

    response = requests.post(
        f"{BASE_URL}/vision/upload",
        files={
            "file": (
                file.name,
                file.read(),
                file.type
            )
        }
    )

    response.raise_for_status()

    return response.json()