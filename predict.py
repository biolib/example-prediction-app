import argparse
import pandas as pd
from Bio import SeqIO
import pickle
from sklearn import tree
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--fasta', default='input.csv')
args = parser.parse_args()

X = [str(record.seq) for record in list(SeqIO.parse(args.fasta, "fasta"))]

print(f"Running prediction on {len(X)} sequences")

# Load model
with open('model.pickle', 'rb') as model_file:
    model: tree.DecisionTreeRegressor = pickle.load(model_file)
vectorize_on_length = np.vectorize(len)
X_vectorized = np.reshape(vectorize_on_length(X), (-1, 1))
predictions = model.predict(X_vectorized)

# Save predictions to file
df_predictions = pd.DataFrame({'prediction': predictions})
df_predictions.to_csv('predictions.csv', index=False)

print(f'{len(predictions)} predictions saved to a csv file')