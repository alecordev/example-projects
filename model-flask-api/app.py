import json

import joblib
import pandas as pd
from flask import Flask, request, jsonify


MODELS_DIR = "models/"
app = Flask(__name__)


def get_iris_model():
    loaded_clf = joblib.load(MODELS_DIR + "clf_iris.joblib")
    return loaded_clf


def str_to_float_list(arg):
    arg = arg.split(",")
    arg = [float(x) for x in arg]
    return arg


loaded_clf = get_iris_model()


def get_params(request):
    sep_length = str_to_float_list(request.args.get("sep_length"))
    sep_width = str_to_float_list(request.args.get("sep_width"))
    pet_length = str_to_float_list(request.args.get("petal_length"))
    pet_width = str_to_float_list(request.args.get("petal_width"))

    return sep_length, sep_width, pet_length, pet_width


@app.route("/predict_class", methods=["GET", "POST"])
def predict_class():
    sep_length, sep_width, pet_length, pet_width = get_params(request)
    new_row = pd.DataFrame(
        {
            "sepal length (cm)": [float(x) for x in sep_length],
            "sepal width (cm)": [float(x) for x in sep_width],
            "petal length (cm)": [float(x) for x in pet_length],
            "petal width (cm)": [float(x) for x in pet_width],
        }
    )
    y_pred = list(loaded_clf.predict(new_row))
    y_pred = [str(x) for x in y_pred]

    response = {"y_pred": ",".join(y_pred)}
    return jsonify(response)


def get_params_form(request):
    request_input = request.form.get("input")
    request_input = json.loads(request_input)

    sep_length = str_to_float_list(request_input["sep_length"])
    sep_width = str_to_float_list(request_input["sep_width"])
    pet_length = str_to_float_list(request_input["petal_length"])
    pet_width = str_to_float_list(request_input["petal_width"])

    return sep_length, sep_width, pet_length, pet_width


@app.route("/predict_class_form", methods=["GET", "POST"])
def predict_class_form():
    sep_length, sep_width, pet_length, pet_width = get_params_form(request)
    new_row = pd.DataFrame(
        {
            "sepal length (cm)": [float(x) for x in sep_length],
            "sepal width (cm)": [float(x) for x in sep_width],
            "petal length (cm)": [float(x) for x in pet_length],
            "petal width (cm)": [float(x) for x in pet_width],
        }
    )
    y_pred = list(loaded_clf.predict(new_row))
    y_pred = [str(x) for x in y_pred]

    response = {"y_pred": ",".join(y_pred)}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
