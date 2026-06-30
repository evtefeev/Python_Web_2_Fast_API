import requests

url = "http://127.0.0.1:8000/userinput/"

for i in range(50):
    response = requests.post(
        url,
        json={
            "name": f"Alex{i}",
            "email": "alexe@gmail.com",
            "age": 15 + i,
        },
    )

    print(response.json())
