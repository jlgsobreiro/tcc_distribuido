from flask import Flask, render_template, request
import pythonp2p

import setuptools

app = Flask(__name__)
node = pythonp2p.Node()  # start the node


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    response = ''
    if request.method == 'POST':
        ip = request.form.get("ip", '')
        port = request.form.get("port", 65432)
        print(f'IP:{ip} PORT:{port}')
        response = node.connect_to(ip, port)
    return render_template('main.html', response=response)


if __name__ == '__main__':
    node.start()
    app.run(host='0.0.0.0')
