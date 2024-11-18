from flask import Flask, request

app = Flask(__name__)

#going to use post since we are sending a
@app.route('/receive_message', methods=['POST'])
def receive_message():
    # Extract message from the JSON payload of the request
    data = request.get_json()
    message = data.get("message", "")
    
    # Print the message to the terminal
    print(message)
    
    # Send a response back to the caller
    return {"status": "Message received", "message": message}

if __name__ == '__main__':
    # Run the server on localhost:5000
    app.run(debug=True)
