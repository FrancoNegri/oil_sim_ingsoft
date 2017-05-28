from flask import Flask, render_template, request
app = Flask(__name__)
import json

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/log', methods=['POST'])
def log():
	return json.dumps(request.form)


if __name__ == "__main__":
	app.run(debug=True)