import time
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def main():
    return '1'
