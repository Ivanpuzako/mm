import pandas as pd 
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
import argparse
import os
import pickle

parser = argparse.ArgumentParser()
parser.add_argument('preprocessed')
parser.add_argument('output_dir')
args = parser.parse_args()
output_dir = args.output_dir

df = pd.read_csv(args.preprocessed)
X = df[['Pclass', 'Sex', 'Age', 'Fare', 'Parch']]
y = df[['Survived']]
X_scaled = scale(X)

X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=101)
output_filenames = ('train_features.pkl', 'val_features.pkl', 'train_labels.pkl', 'val_labels.pkl')
if not os._exists(output_dir):
    os.mkdir(output_dir)
for data, file in zip(train_test_split(X_scaled, y, test_size=0.2, random_state=101),  output_filenames): 
    file_path = os.path.join(args.output_dir, file)
    pickle.dump(data, open(file_path, 'wb'))