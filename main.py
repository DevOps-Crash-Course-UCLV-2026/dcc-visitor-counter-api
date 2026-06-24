import os

import redis
from flask import Flask

app = Flask(__name__)
redis = redis.Redis(host="redis", port=6379, db=0)


@app.route("/")
def hello_world():
    return "Welcome to DevOps Crash Course 2026"


@app.route("/visitor")
def visitor():
    redis.incr("visitor")
    visitor_num = redis.get("visitor").decode("utf-8")
    return "Visitor count: %s" % (visitor_num)


@app.route("/visitor/reset")
def reset_visitor():
    redis.set("visitor", 0)
    visitor_num = redis.get("visitor").decode("utf-8")
    return "Visitor count reseted to: %s" % (visitor_num)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
