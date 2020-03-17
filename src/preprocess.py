import numpy as np
import pandas as pd 
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('data')
parser.add_argument('output_dir')
args = parser.parse_args()
data_path = args.data
df = pd.read_csv(data_path, index_col='PassengerId')

df = df.drop(columns=['Cabin'])
df['Age'] = df['Age'].fillna(df.groupby(['Pclass'])['Age'].transform(np.mean))

df['Embarked'] = df['Embarked'].fillna('S')

sex_replace = {'female': 0, 'male': 1}
df = df.replace({'Sex': sex_replace})



output_dir = args.output_dir
if not os._exists(output_dir):
    os.mkdir(output_dir)
df.to_csv(os.path.join(args.output_dir,'preprocessed.csv'))


