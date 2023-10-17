from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def greeting():
    name = request.args.get('name', '')
    message = request.args.get('message', '')
    return f'Hello {name}!<br>{message}!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
