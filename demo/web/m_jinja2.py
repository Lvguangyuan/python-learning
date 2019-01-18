from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/sign', methods=['GET'])
def form():
    return render_template('form.html')


@app.route('/sign', methods=['POST'])
def sign():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '123':
        return render_template('success.html', username=username)
    else:
        error = 'Username or password not correct!'
        return render_template('error.html', username=username, error=error)


if __name__ == '__main__':
    app.run()
