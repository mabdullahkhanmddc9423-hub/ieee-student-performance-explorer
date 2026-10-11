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
## 4. Dataset Information & Cleaning Decisions
Data Source: Custom student assessment CSV dataset containing 25-30 records with intentional missing score entries and duplicate rows, stored in data/students.csv. Missing Values & Cleaning: Removed duplicate student rows to ensure unique records.
Coerced non-numeric marks to numeric values and imputed missing quiz, assignment, and exam scores using class median values to avoid skewing statistical outputs.
## 5. Console Output Screenshots
### Terminal Output and Summary Report
<img width="712" height="57" alt="Program1" src="https://github.com/user-attachments/assets/6ac1317e-854e-4acb-adbb-14f1eb463d94" />
<img width="802" height="637" alt="summary_report" src="https://github.com/user-attachments/assets/5fd767aa-8a25-45c7-9149-4db46ae8c71a" />

### Description
Class Statistics: The overall evaluation shows a Class Mean Final Mark of 78.97, a Median Mark of 81.10, and a Standard Deviation of 11.56, with marks ranging from a lowest of 51.00 to a peak of 94.90.   
Subject & Section Rankings: Computer Science emerged as the strongest performing subject (average mark of 80.21), followed closely by Physics (80.05) and Mathematics (76.90). Additionally, Section A outperformed Section B with a class average of 84.75.   
Top Performers: The top three students overall were Rabia (Section A, Computer Science, 94.9), Hina (Section A, Physics, 94.6), and Fatima (Section A, Mathematics, 90.5).
