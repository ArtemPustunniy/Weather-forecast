import time
from flask import Flask, request, Response, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return 'Waiting...'


@app.route('/answer', methods=['POST', 'GET'])
def answer():
    if request.method == 'POST':
        my_name = request.json['my_name']
        my_surname = request.json['my_surname']
        print(my_name, my_surname)
        # Сохранение в базу данных
        return Response(status=200)


if __name__ == '__main__':
    app.run()
