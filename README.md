# TOPSIS Implementation in Python
**Author:** Ananya  
**Roll No:** 102303160  

This repository provides a Python-based implementation of the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method for multi-criteria decision making.  
It includes both a command-line interface and a simple Flask web API for ranking alternatives.

---

##  What is TOPSIS?

TOPSIS ranks alternatives by comparing their distance from:

- **Ideal Best** → highest desirable value
- **Ideal Worst** → least desirable value

Used in:

- product comparison
- performance evaluation
- decision making with multiple criteria

---

##  Method Steps

1. Read decision matrix from CSV
2. Normalize criteria values
3. Apply weights
4. Determine ideal best & worst based on impacts
5. Compute Euclidean distances
6. Calculate TOPSIS score
7. Rank alternatives

---

##  Project Structure

Topsis_Ananya_102303160/
├── topsis_ananya_102303160/ # Core TOPSIS logic (Python package)
├── topsis-web-service/ # Flask API for web-based ranking
│ └── app.py
├── data.csv # Sample input data
├── result.csv # Sample output ranking
├── setup.py
├── requirements.txt
└── README.md


---

##  Input Format

The input CSV must include:

- **First column:** alternative names
- **Remaining columns:** numeric criteria values

Example:

| Model | Price | Performance | Weight |
|-------|-------|-------------|--------|
| M1    | 0.61  | 0.37        | 6.9    |
| M2    | 0.68  | 0.46        | 4.5    |
| M3    | 0.74  | 0.55        | 3.8    |

Weights & impacts are provided as comma-separated lists:

Weights: 1,2,3
Impacts: +,-,+


---

##  Example

### **Input**

| Fund Name | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|
| M1 | 0.61 | 0.37 | 6.9 | 60.7 | 17.15 |
| M2 | 0.68 | 0.46 | 4.5 | 66.1 | 17.94 |
| M3 | 0.74 | 0.55 | 3.8 | 59.6 | 16.17 |
| M4 | 0.71 | 0.50 | 6.1 | 44.2 | 12.88 |
| M5 | 0.80 | 0.64 | 4.8 | 31.2 | 9.36 |
| M6 | 0.69 | 0.48 | 5.5 | 52.7 | 14.84 |
| M7 | 0.60 | 0.36 | 4.1 | 69.2 | 18.57 |
| M8 | 0.91 | 0.83 | 6.3 | 35.9 | 10.99 |

---

### **Output**

| Fund Name | P1 | P2 | P3 | P4 | P5 | Score | Rank |
|---|---|---|---|---|---|---|---|
| M1 | 0.61 | 0.37 | 6.9 | 60.7 | 17.15 | 0.52 | 2 |
| M2 | 0.68 | 0.46 | 4.5 | 66.1 | 17.94 | 0.52 | 3 |
| M3 | 0.74 | 0.55 | 3.8 | 59.6 | 16.17 | 0.50 | 4 |
| M4 | 0.71 | 0.50 | 6.1 | 44.2 | 12.88 | 0.45 | 7 |
| M5 | 0.80 | 0.64 | 4.8 | 31.2 | 9.36  | 0.41 | 8 |
| M6 | 0.69 | 0.48 | 5.5 | 52.7 | 14.84 | 0.47 | 6 |
| M7 | 0.60 | 0.36 | 4.1 | 69.2 | 18.57 | 0.48 | 5 |
| M8 | 0.91 | 0.83 | 6.3 | 35.9 | 10.99 | 0.55 | 1 |

---

##  Command Line Usage

### Install Dependencies

pip install -r requirements.txt

### Run Through CLI

topsis data.csv "1,2,3" "+,-,+"

### Optional Output File

topsis data.csv "1,2,3" "+,-,+" result.csv


---

##  Web Service

A Flask API is included for programmatic access.

Users can:

1.upload CSV  
2.specify weights & impacts  
3. receive ranked output  

---

##  Dependencies

- Python 3.x
- numpy
- pandas
- flask

---

##  Conclusion

This project provides a clean and ready-to-use TOPSIS implementation supporting both CLI and web modes, suitable for real-world academic and analytical use.


