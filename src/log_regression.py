import os
import argparse
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

parser = argparse.ArgumentParser()
parser.add_argument('data_dir')
parser.add_argument('output_dir')
args = parser.parse_args()
output_dir = args.output_dir

train_data_path = os.path.join(args.data_dir, 'train_features.pkl')
train_labels_path = os.path.join(args.data_dir, 'train_labels.pkl')
X_train = pickle.load(open(train_data_path,'rb'))
y_train = pickle.load(open(train_labels_path,'rb'))


logistic_regression = LogisticRegression(random_state=101,C=2.0, solver='liblinear')
logistic_regression.fit(X_train, y_train.values.ravel())

if not os._exists(output_dir):
    os.mkdir(output_dir)
model_path = os.path.join(output_dir, 'log_regression.pkl')
pickle.dump(logistic_regression, open(model_path, 'wb'))
