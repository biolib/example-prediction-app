import argparse
import os

import pandas as pd
from Bio import SeqIO

# Input args
#parser = argparse.ArgumentParser()
#parser.add_argument("--fasta", default="sample.fasta")
#parser.add_argument("--outfile", default="predictions.tsv")
#parser.add_argument("--model", default="model1")
#args = parser.parse_args()
#print(args)

# Functions
def count_alanines(seq):
    return list(seq).count("A")


def main():

    # Load data
    if os.path.exists("sample.fasta"):
        seq_dict = SeqIO.to_dict(SeqIO.parse("sample.fasta", "fasta"))
    else:
        raise Exception(f"File not found: sample.fasta")

    # Predict
    ids = list(seq_dict.keys())
    predictions = []
    for _id in ids:
        seq = seq_dict[_id]
        pred = count_alanines(seq)
        predictions.append(pred)

    # Output CSV
    df_csv = pd.DataFrame(
        {
            "sample": ids,
            "prediction": predictions,
        }
    )

    # Save predictions to file
    print(f"Writing {len(df_csv)} predictions to predictions.tsv")
    df_csv.to_csv("predictions.tsv", sep="\t", index=False)

if __name__ == "__main__":
    main()
