import os
import argparse
import pickle
import numpy as np
import sklearn.metrics as metrics
#from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

parser = argparse.ArgumentParser()
parser.add_argument('data_dir')
parser.add_argument('model')
parser.add_argument('metric_file')
args = parser.parse_args()

model_path = args.model 

X_test_path = os.path.join(args.data_dir, 'val_features.pkl')
y_test_path =  os.path.join(args.data_dir, 'val_labels.pkl')

model, X_test, y_test = [pickle.load(open(file, 'rb')) for file in (model_path, X_test_path, y_test_path)]

y_pred = model.predict_proba(X_test)[:,1]

score  = roc_auc_score(y_test, y_pred)

with open(args.metric_file, 'w') as file:
    file.write(str(score))



















