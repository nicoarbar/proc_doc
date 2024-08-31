from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nico')
def home_nico():
    return "Hello, Nico!"
@app.route('/templates')

def home_nico():
    return "Hello, Nico!"

if __name__ == '__main__':
    app.run(debug=True)
