import sklearn
import numpy as np
from sklearn import preprocessing
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from joblib import dump, load

# load data
m = pd.read_csv('application/data/mushrooms.csv')
m.columns = m.columns.str.replace('-', '_', regex=True)

# separate label and features
features_original = m.drop('class', axis=1)
label = m['class']

# encoding of the label (class of mushroom)
le = preprocessing.LabelEncoder()
le.fit(label)
label_encoded = le.transform(label)
label_encoded = np.array(label_encoded)
# save label encoding for web app
mapping_label_encoded = dict(zip(le.classes_, le.transform(le.classes_)))
dump(mapping_label_encoded, 'application/data/mapping_label_encoded.pkl')
# Split the data into training and testing sets
print("Divide the dataset into training data (75%) and test data (25%)")

train_features, test_features, train_labels, test_labels = train_test_split(features_original, label_encoded,
                                                                            test_size=0.25,
                                                                            random_state=42)

# use one hot encoding to convert categorical features into numerical
# we don't assume any order for each features so one hot encoding is more appropriated than other label encoder and each feature has a few level
feature_encoding = preprocessing.OneHotEncoder(handle_unknown='ignore')
feature_encoding.fit(train_features)
train_features = feature_encoding.transform(train_features).toarray()
test_features = feature_encoding.transform(test_features).toarray()

print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)

# let's try random forest as first approach: easy to implement: not a lot of hyperparameters tuning and no need to normalize (not needed anyway here)
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on training data
rf.fit(train_features, train_labels)
# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# the accuracy is a good indicator here because the dataset is balanced (and there is no error)
print('accuracy RF on test set:' + str(accuracy_score(test_labels, predictions)))

# # let's run cv on 10 fold to get a better overview
categorical_transformer_pipeline = Pipeline(steps=[('onehot', preprocessing.OneHotEncoder(handle_unknown='ignore'))])
rf1 = RandomForestClassifier(n_estimators=100, random_state=42)
my_pipeline = Pipeline(steps=[('preprocessor', categorical_transformer_pipeline),
                              ('model', rf1)
                              ])

print("cross validation to have a more stable estimate")
cv_scores = cross_val_score(my_pipeline, features_original, label_encoded, cv=15)
print("All cv scores:")
print(cv_scores)
print('\n')
print("Mean score:")
print("Mean score - Random Forest: ", cv_scores.mean())

# now that we have a good estimate for how well the classification is, we can train the model on the whole dataset for the web app
# we can also encode the features on the whole
feature_encoding = preprocessing.OneHotEncoder(handle_unknown='ignore')
feature_encoding.fit(features_original)
features = feature_encoding.transform(features_original)

rf.fit(features, label_encoded)

# save encoding and  columns orders in order to recreate the order for the web ap
features_columns = features_original.columns
dump(features_columns, 'application/data/features_columns.pkl')
dump(feature_encoding, 'application/data/feature_encoding.pkl')

# save rf model for web app
dump(rf, "application/data/rf.mdl")
