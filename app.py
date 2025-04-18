from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/form', methods=['POST'])
def home():
    name = request.form.get('name')
    return f'Hello, {name}!'

if __name__ == "__main__":
    app.run(app.run(host='194.87.95.213', port=8080), debug=True)