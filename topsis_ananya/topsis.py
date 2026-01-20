import sys
import pandas as pd
import numpy as np
import os

def main():
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <inputFile> <weights> <impacts> <outputFile>")
        sys.exit(1)

    inputFile = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    outputFile = sys.argv[4]

    if not os.path.isfile(inputFile):
        print("Error: Input file not found")
        sys.exit(1)

    try:
        df = pd.read_csv(inputFile)
    except:
        print("Error: File must be CSV")
        sys.exit(1)

    if df.shape[1] < 3:
        print("Error: Input file must have at least 3 columns")
        sys.exit(1)

    for col in df.columns[1:]:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            print(f"Error: Column {col} must be numeric")
            sys.exit(1)

    weights = weights.split(',')
    impacts = impacts.split(',')

    if len(weights) != (df.shape[1] - 1):
        print("Error: Number of weights must match number of parameters")
        sys.exit(1)

    if len(impacts) != (df.shape[1] - 1):
        print("Error: Number of impacts must match number of parameters")
        sys.exit(1)

    for imp in impacts:
        if imp not in ['+', '-']:
            print("Error: Impacts must be + or - only")
            sys.exit(1)

    try:
        weights = [float(i) for i in weights]
    except:
        print("Error: Weights must be numeric")
        sys.exit(1)

    data = df.iloc[:,1:].values
    rows, cols = data.shape

    norm = np.sqrt((data**2).sum(axis=0))
    norm_matrix = data / norm

    weighted_matrix = norm_matrix * weights

    ideal_best = []
    ideal_worst = []

    for j in range(cols):
        if impacts[j] == '+':
            ideal_best.append(weighted_matrix[:,j].max())
            ideal_worst.append(weighted_matrix[:,j].min())
        else:
            ideal_best.append(weighted_matrix[:,j].min())
            ideal_worst.append(weighted_matrix[:,j].max())

    s_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    s_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

    score = s_worst / (s_best + s_worst)

    df['Topsis Score'] = score
    df['Rank'] = df['Topsis Score'].rank(ascending=False).astype(int)

    df.to_csv(outputFile, index=False)
    print(f"Result saved to {outputFile}")

def run():
    print("Topsis package running…")

