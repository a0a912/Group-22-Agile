import json

from flask import Flask, render_template, jsonify, request, redirect, url_for
import csv
from pathlib import Path

app = Flask(__name__)

app.instance_path = Path("data").resolve()


@app.route("/")
def index():
    with open('data/mcq_questions.json', 'r') as mcq_file:
        mcq_questions_data = json.load(mcq_file)
    with open('data/written_questions.json', 'r') as written_file:
        written_questions_data = json.load(written_file)
    return render_template("test_duolingo.html", mcq_questions=mcq_questions_data, written_questions=written_questions_data)


if __name__ == "__main__":
	app.run(debug=True, port=8888)