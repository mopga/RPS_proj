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
async def resp():
    return rps.rps(line, p2)

if __name__ == '__main__':
    f = open('nabor.txt')

    for line in f.read():
        p1 = line
        p2 = choice(choises)
        resp
    f.close()
