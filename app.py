import flask
import pandas as pd
import numpy as np
from joblib import dump, load


with open(f'rf.mdl', 'rb') as f:
    model = load(f)

with open(f'model_columns.pkl', 'rb') as f:
    model_columns = load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return flask.render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    input_form = pd.DataFrame(flask.request.form,index=[0])
    features = pd.get_dummies(input_form)
    for col in model_columns:
        if col not in features.columns:
            features[col] = 0
    features = np.array(features)
    print("TODO deal with case where feature never appear in dataset like ring type c")
    predictions = model.predict(features)[0]
    res = ("eatable" if predictions else "poisonous")
    print(predictions)

    return flask.render_template('index.html',result=res)

@app.route('/results',methods=['POST'])
def results():

    data = flask.request.get_json(force=True)
    data = pd.DataFrame.from_dict(data)
    features = pd.get_dummies(data)
    for col in model_columns:
        if col not in features.columns:
            features[col] = 0
    features = np.array(features)
    predictions = model.predict(features)
    output = {"Request "+ str(i) : "eatable" if predictions[i] else "poisonous" for i in range(0, len(predictions))}

    return flask.jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)