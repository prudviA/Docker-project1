from flask import Flask, jsonify
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    count = cache.incr('hits')
    return jsonify(message="Welcome to Flask with Redis!", hits=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
