from flask import Flask, jsonify, request

app = Flask(__name__)

notes = []

@app.route('/')
def index():
    return "Welcome to the Notes API!"

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    notes.append(data)
    return jsonify({"message": "Note added!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
