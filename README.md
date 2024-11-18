# Requesting Data

To request data from this microservice, simply send a json object following this format, replacing the pounds with numbers:

data = {
    "point1": {"x": #, "y": #},
    "point2": {"x": #, "y": #}
}

Ther server will be run on http://127.0.0.1:5000/distance. Here is an example using the previous address and random set of points:

url = "http://127.0.0.1:5000/distance"

data = {
    "point1": {"x": 3, "y": 7},
    "point2": {"x": 8, "y": 1}
}

response = requests.post(url, json=data)

# Receiving Data

Receiving data from the server is incredibly simple. Using the same example as above, the data from the server will be stored in the response variable, following this format, where the pounds represent the calculated euclidean and manhattan distance:

response = {
    "euclidean_distance": #,
    "manhattan_distance": #
}

![UML Diagram (1)](https://github.com/user-attachments/assets/d82dd412-bc90-4862-843e-ce88d2bd255b)
