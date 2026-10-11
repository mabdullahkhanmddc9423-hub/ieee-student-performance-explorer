# Student Performance Explorer
### IEEE LGU AI/ML Cohort One - Fall 2026
**Week 3 Assignment:** Data Analysis with NumPy & Pandas
**AI/ML Leads:** Abdullah Faisal & Alina Irshad
## 1. Project Overview
This project processes academic assessment records across multiple subjects and sections. The analysis cleans missing test scores, computes final student grades, uses NumPy for class-wide statistical computations, and groups data by subject to rank performance.
## 2. Key Concepts Implemented
- [x] Pandas DataFrame Loading & Cleaning (`read_csv`, `fillna`, `dropna`, `drop_duplicates`)
- [x] NumPy Statistical Calculations (Mean, Median, Standard Deviation, Sums)
- [x] Data Grouping & Aggregation (`groupby`)
- [x] Conditional Filtering & Indexing
- [x] Dataset Merging / Time-Series Resampling (if applicable)
## 3. How to Run the Program
python main.py
## 4. Dataset Information & Cleaning DecisionsData 
Source: Custom student assessment CSV dataset containing 25-30 records with intentional missing score entries and duplicate rows, stored in data/students.csv.   Missing Values & Cleaning: Removed duplicate student rows to ensure unique records.
Coerced non-numeric marks to numeric values and imputed missing quiz, assignment, and exam scores using class median values to avoid skewing statistical outputs.
## 5. Console Output Screenshots
