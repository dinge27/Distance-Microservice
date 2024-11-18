import requests

url = "http://127.0.0.1:5000/distance"


data = {
    "point1": {"x": 3, "y": 7},
    "point2": {"x": 8, "y": 1}
}

print("Sending request...")
response = requests.post(url, json=data)

if response.status_code == 200:
    distance = response.json()
    print("Euclidean Distance:", distance.get('euclidean_distance'))
    print("Manhattan Distance:", distance.get('manhattan_distance'))
else:
    print("Error:", response.status_code, response.text)
