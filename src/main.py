from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hi juju , you are so beautiful , i love you , bujuku bujukku"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
