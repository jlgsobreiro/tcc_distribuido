from flask import Flask, render_template, request, redirect, url_for
from pythonp2p import Node

app = Flask(__name__)


node = Node('127.0.0.1', 65432, 65433)  # start the node
@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    response = ''
    print('Aplicativo acessado')
    if request.method == 'POST':
        ip = request.form.get("ip", '')
        port = request.form.get("port", 65432)
        print(f'IP:{ip} PORT:{port}')
        response = node.connect_to(ip, int(port))
    return render_template('main.html', response=response)


@app.route('/salvar', methods=['GET', 'POST'])
def salvar():  # put application's code here
    node.savestate('state.json')
    return redirect(url_for('hello_world', response='Ok'))


if __name__ == '__main__':
    node.start()
    app.run(host='0.0.0.0')
