from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from home route. Just extending the text.Still the error persist. Still...,,,"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port = 4000)



