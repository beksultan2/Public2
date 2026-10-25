import os
import requests

username = os.getenv("TEST_USERNAME")
password = os.getenv("TEST_PASSWORD")

if not username or not password:
    raise ValueError(
        "TEST_USERNAME жана TEST_PASSWORD өзгөрмөлөрүн орнотуу керек."
    )

r = requests.post(
    "http://127.0.0.1:8000/login/",
    json={
        "username": username,
        "password": password,
    },
)

print("LOGIN:", r.status_code)
r.raise_for_status()

token = r.json()["access"]

headers = {"Authorization": f"Bearer {token}"}

r = requests.get(
    "http://127.0.0.1:8002/cart/",
    headers=headers,
)

print("CART:", r.status_code, r.json())
