"""Routes for logged-in application."""
from flask import Blueprint, render_template, request, make_response, jsonify
from flask_login import current_user
from flask import current_app as app
from .assets import compile_auth_assets
from flask_login import login_required
import pandas as pd
import numpy as np
from joblib import dump, load

# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')
compile_auth_assets(app)

with open(f'application/data/rf.mdl', 'rb') as f:
    model = load(f)

with open(f'application/data/model_columns.pkl', 'rb') as f:
    model_columns = load(f)

# @main_bp.route('/', methods=['GET'])
# @login_required
# def dashboard():
#     """Serve logged in Dashboard."""
#     return render_template('dashboard.html',
#                            title='Flask-Login Tutorial.',
#                            template='dashboard-template',
#                            current_user=current_user,
#                            body="You are now logged in!")



@main_bp.route('/', methods=['GET'])
@login_required
def index():
    """Serve logged in Dashboard."""
    return render_template("index.html")



@app.route('/predict', methods=['POST'])
@login_required
def predict():

    input_form = pd.DataFrame(request.form,index=[0])
    features = pd.get_dummies(input_form)
    for col in model_columns:
        if col not in features.columns:
            features[col] = 0
    features = np.array(features)
    print("TODO deal with case where feature never appear in dataset like ring type c")
    predictions = model.predict(features)[0]
    res = ("eatable" if predictions else "poisonous")
    print(predictions)

    return render_template('index.html',result=res)

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    data = pd.DataFrame.from_dict(data)
    features = pd.get_dummies(data)
    for col in model_columns:
        if col not in features.columns:
            features[col] = 0
    features = np.array(features)
    predictions = model.predict(features)
    output = {"Request "+ str(i) : "eatable" if predictions[i] else "poisonous" for i in range(0, len(predictions))}
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(output), 200, headers)
