from flask import Flask, jsonify, url_for, render_template
import socket

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route('/user/<username>')
def profile(username):
    return f"{username}\'s profile"


def fetch_details():
    
    return str(socket.gethostname()), str(socket.gethostbyname(socket.gethostname()))

@app.route('/details')
def details():
    host, ip = fetch_details()
    return render_template('index.html', HOSTNAME=host, IP=ip)


with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('profile', username='bob'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)