from flask import Flask
from pythonp2p import Node

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    node = Node()  # start the node
    node.start()
    app.run()
