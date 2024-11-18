from flask import Flask, request
import math

app = Flask(__name__)

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

@app.route('/distance', methods=['POST'])
def distance():
    coordinates = request.get_json()

    point1 = coordinates['point1']
    point2 = coordinates['point2']

    x1 = point1['x']
    y1 = point1['y']
    x2 = point2['x']
    y2 = point2['y']

    euclidean = calculate_euclidean_distance(x1, y1, x2, y2)

    manhattan = calculate_manhattan_distance(x1, y1, x2, y2)

    response = {
        "euclidean_distance": euclidean,
        "manhattan_distance": manhattan
    }

    return response



if __name__ == "__main__":
    app.run(debug=True)