import requests

# Substitua aqui pelo seu access token real
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyMzY5MTU0LCJpYXQiOjE3NTIzNjgyNTQsImp0aSI6IjM0ODU5OWE4OGJlNjRiZmJhMzljODMzYjE5ZTJiZGMyIiwidXNlcl9pZCI6MX0.4AQARVaKD8S3kH-btuocCJSMpKE4z35RjSBfxbGk7uc"

headers = {"Authorization": f"Bearer {access_token}"}

url = "http://localhost:8000/api/accounts/me/"

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Resposta:")
print(response.json())
