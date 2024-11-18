import requests

# URL for the local Flask server
url = 'http://127.0.0.1:5000/receive_message'

# JSON payload with the message
payload = {"message": "This is a message from CS361"}

# Send a POST request
response = requests.post(url, json=payload)

# Print the response from the server
print("Server response:", response.json())
