from flask import Flask, render_template, request, jsonify
from model_plot import main
from predict_solubility import smiles_to_solubility
import numpy as np
import os

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def sol_app():
    if request.method == "POST":
        smile_string = request.form.get("smiles")
        smile_sol = smiles_to_solubility([smile_string])
        return render_template("index.html", sol_val=list(smile_sol), filename=os.path.abspath("image_480.png"))
    return render_template("index.html")


if __name__ == '__main__':
    app.run()