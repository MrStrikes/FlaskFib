from flask import Flask
from math import sqrt


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/fib/<int:num>")
def fib(num):
    a,b = 1,1
    for i in range(num):
        a,b = b,a+b
    return str(a)

if __name__ == "__main__":
    app.run()
