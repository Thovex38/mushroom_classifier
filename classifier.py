import sklearn
import numpy as np
from sklearn import preprocessing
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from joblib import dump, load

# load data
m = pd.read_csv('/Users/user/Downloads/mushroom/mushrooms.csv')
m.columns= m.columns.str.replace('-','_',regex=True)

# separate label and features
features = m.drop('class', axis=1)

label = m['class']

# use one hot encoding to convert categorical features into numerical
# we don't assume any order for each features so one hot encoding is more appropriated than other label encoder and each feature has a few level
feature_encoding = preprocessing.OneHotEncoder(handle_unknown='ignore')
feature_encoding.fit(features)

# save encoding and  columns orders in order to recreate the order for the web ap
features_columns = features.columns
dump(features_columns, 'application/data/features_columns.pkl')
dump(feature_encoding, 'application/data/feature_encoding.pkl')

features = feature_encoding.transform(features).toarray()

# encoding of the label (class of mushroom)
le = preprocessing.LabelEncoder()
le.fit(label)
label_encoded = le.transform(label)
label_encoded = np.array(label_encoded)


# Using Skicit-learn to split data into training and testing sets
# Split the data into training and testing sets
features = np.array(features)
train_features, test_features, train_labels, test_labels = train_test_split(features, label_encoded, test_size=0.25,
                                                                            random_state=42)
print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)

# let's try random forest as first approach: easy to implement: not a lot of hyperparameters tuning and no need to normalize (not needed anyway here)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
# Train the model on training data
rf.fit(train_features, train_labels);
# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
print('accuracy RF :'+str(accuracy_score(test_labels, predictions)))
# the accuracy is a good indicator here because the dataset is balanced (and there is no error)

# let's inspect the most important features :


#clf = DecisionTreeClassifier(random_state=0)
#clf = clf.fit(train_features, train_labels);
#predictions2 = clf.predict(test_features)
#print('accuracy DT:'+str(accuracy_score(test_labels, predictions2)))

# save rf model for web app
dump(rf, "application/data/rf.mdl")
