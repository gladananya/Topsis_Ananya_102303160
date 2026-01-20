# TOPSIS Implementation in Python
**Author:** Ananya  
**Roll No:** 102303160

This repository contains a Python implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** algorithm for multi-criteria decision-making. The project supports both a CLI tool and a simple web service interface to rank alternatives based on criteria, weights, and impacts.

---

## What is TOPSIS?

TOPSIS is a quantitative decision-making approach that ranks options by comparing how close they are to:

✔ the **ideal best** solution  
✖ and how far they are from the **ideal worst**

This method is widely used in:

- product evaluation
- performance assessment
- engineering and management decisions
- multi-criteria analysis

---

## How the Method Works (Brief Overview)

The workflow of the algorithm is:

1. Read data from a CSV decision matrix
2. Normalize values so different criteria are comparable
3. Apply user-defined weights to each criterion
4. Determine the ideal best and ideal worst values based on impacts
5. Compute Euclidean distance from both ideal solutions
6. Calculate the TOPSIS score
7. Rank alternatives based on the score (higher is better)

---

## Project Structure

Topsis_Ananya_102303160/
├── topsis_ananya_102303160/ # Core TOPSIS implementation (Python package)
├── topsis-web-service/ # Flask web API interface
│ └── app.py
├── data.csv # Sample input dataset
├── result.csv # Sample output result file
├── setup.py
├── requirements.txt
└── README.md


---

## Input Format

The input CSV file must contain:

- **Column 1:** names of alternatives (e.g., models, products, candidates)
- **Remaining columns:** numeric values corresponding to criteria

Example header:

Model, Price, Performance, Weight

Weights and impacts are provided separately as comma-separated strings:

Weights: 1,2,3
Impacts: +,-,+


Where:

- `+` indicates beneficial (higher is better)
- `-` indicates non-beneficial (lower is better)

---

## Command Line Usage

### Install Dependencies

### Run TOPSIS from CLI

### Optional: Save Output to a File


The output file contains TOPSIS scores and final rankings for each alternative.

---

## Web Service (Flask API)

A lightweight web API is provided to enable integration into web systems.  
The user can:

- upload CSV data
- specify weights & impacts
- receive scored and ranked outputs

Useful for embedding TOPSIS in dashboards or backend decision systems.

---

## Output Details

Final results include:

- original input criteria
- computed TOPSIS score
- rank assigned to each alternative

> Higher TOPSIS score → better ranked option

---

## Validation & Error Handling

The implementation verifies:

✔ equal number of weights and criteria  
✔ valid `+`/`-` impact symbols  
✔ numeric data entries  
✔ proper CSV format  

---

## Dependencies

- Python 3.x
- pandas
- numpy
- flask (for API functionality)

---

## Conclusion

This project provides a clean and practical implementation of the TOPSIS method with both CLI and web capabilities. It is suitable for academic use, experimentation, and real decision-making scenarios.



