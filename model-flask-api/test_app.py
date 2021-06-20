import requests


def test_predict_class_form():
    """ POST as if a FORM was submitted """
    data = {
        "input": '{"sep_length": "3", "sep_width": "4", "petal_length": "5", "petal_width": "4"}'
    }

    resp = requests.post("http://localhost:8080/predict_class_form", data=data)
    print(resp.status_code)
    print(resp.json())


def test_predict_class():
    """ Variables in the URL """
    data = {
        "sep_length": "3",
        "sep_width": "4",
        "petal_length": "5",
        "petal_width": "4",
    }

    resp = requests.get("http://localhost:8080/predict_class", params=data)
    print(resp.status_code)
    print(resp.json())


if __name__ == "__main__":
    test_predict_class()
    test_predict_class_form()
