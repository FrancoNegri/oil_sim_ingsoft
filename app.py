from flask import Flask, render_template
app = Flask(__name__)
from logger import Logger
import time

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/log')
def log():
	logger = Logger("log.txt")
	logger.logear('Escrito a las %s' % time.strftime("%H:%M:%S"))
	return 'Ok'


if __name__ == "__main__":
	app.run(debug=True)