import sklearn
import numpy as np
from sklearn import preprocessing
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from joblib import dump, load


m = pd.read_csv('/Users/user/Downloads/mushroom/mushrooms.csv')

features = m.drop('class', axis=1)
features = pd.get_dummies(features)
column_features = features.columns
# save dummy columns
model_columns = list(features.columns)
dump(model_columns, 'model_columns.pkl')

label = m['class']

le = preprocessing.LabelEncoder()
le.fit(label)
label_encoded = le.transform(label)
label_encoded = np.array(label_encoded)
features = np.array(features)

# Using Skicit-learn to split data into training and testing sets
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, label_encoded, test_size=0.25,
                                                                            random_state=42)
print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)


rf = RandomForestClassifier(n_estimators=1, random_state=42)
# Train the model on training data
rf.fit(train_features, train_labels);
# Use the forest's predict method on the test data
predictions = rf.predict(test_features)


print('accuracy RF :'+str(accuracy_score(test_labels, predictions)))

clf = DecisionTreeClassifier(random_state=0)
clf = clf.fit(train_features, train_labels);
predictions2 = clf.predict(test_features)

print('accuracy DT:'+str(accuracy_score(test_labels, predictions2)))

# save model
dump(rf,"rf.mdl")
