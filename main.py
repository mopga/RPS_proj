from random import choice
from flask import Flask
import rps


print("""
         Hello! This is Rock/Paper/Scissors Game!
         Try to input R (ROCK) / P (PAPER) / S (SCISSORS)
         Good luck!
      """)
choises = "RPS"

app = Flask(__name__)


@app.route("/")
def index():
    return rps.rps(line, p2)


@app.route("/result")
def result(p1, p2):
    return rps.rps(p1, p2)


if __name__ == '__main__':
    index()
    while True:
        result()

