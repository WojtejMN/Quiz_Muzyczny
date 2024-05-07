from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Gość')
@app.route('/templates')
def podstrona1():
    return render_template('podstrona1.html', name='Gość')

if __name__ == '__main__':
    app.run(debug=True)
