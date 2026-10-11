import numpy as np
import pandas as pd


def main():
  # Step 1: Load student dataset from the external CSV file
  csv_path = 'data/students.csv'
  print(f'Loading student dataset from {csv_path}...')

  try:
    df = pd.read_csv(csv_path)
  except FileNotFoundError:
    print(f"Error: The file '{csv_path}' was not found. Please place your CSV file inside the 'data/' folder.")
    return

  # Step 2: Data Cleaning & Handling Missing/Invalid Values
  initial_row_count = len(df)

  # Remove duplicate records
  df = df.drop_duplicates()

  # Coerce score columns to numeric (turning invalid text like 'abc' into NaN)[cite: 5]
  df['quiz_score'] = pd.to_numeric(df['quiz_score'], errors='coerce')
  df['assignment_score'] = pd.to_numeric(df['assignment_score'], errors='coerce')
  df['exam_score'] = pd.to_numeric(df['exam_score'], errors='coerce')

  # Impute missing score values with column medians[cite: 5]
  df['quiz_score'] = df['quiz_score'].fillna(df['quiz_score'].median())
  df['assignment_score'] = df['assignment_score'].fillna(df['assignment_score'].median())
  df['exam_score'] = df['exam_score'].fillna(df['exam_score'].median())

  print(f'Data Cleaned: Processed {initial_row_count} rows, handled missing' ' values and duplicates.')

  # Step 3: NumPy Descriptive Statistics
  # Compute Final Mark (Weighted average: Quiz 20%, Assignment 30%, Exam 50%)[cite: 5]
  df['final_mark'] = ((df['quiz_score'] * 0.20) + (df['assignment_score'] * 0.30) + (df['exam_score'] * 0.50))

  # Convert columns into NumPy arrays for class-wide statistical computations[cite: 5]
  final_marks_np = df['final_mark'].to_numpy()

  class_mean = np.mean(final_marks_np)
  class_std = np.std(final_marks_np)
  class_median = np.median(final_marks_np)
  class_min = np.min(final_marks_np)
  class_max = np.max(final_marks_np)

  # Step 4: Performance Filtering & Grouping
  # Filter students with exam scores >= 80[cite: 5]
  high_performers = df[df['exam_score'] >= 80]

  # Group by subject to compare average performance and find strongest/weakest subjects[cite: 5]
  subject_summary = (df.groupby('subject')['final_mark'].mean().reset_index())
  subject_summary = subject_summary.sort_values(by='final_mark', ascending=False)

  strongest_subject = ( subject_summary.iloc[0]['subject'] if not subject_summary.empty else 'N/A')
  weakest_subject = (subject_summary.iloc[-1]['subject'] if not subject_summary.empty else 'N/A')

  # Section-wise performance grouping[cite: 5]
  section_summary = (df.groupby('section')['final_mark'].mean().reset_index())

  # Top performing students list[cite: 5]
  top_students = df.sort_values(by='final_mark', ascending=False).head(3)

  # Step 5: Clean Console Summary Report[cite: 5]
  print('\n' + '=' * 60)
  print('  Student Performance Explorer - Summary Report  ')
  print('=' * 60)
  print(f'Total Students Evaluated : {len(df)}')
  print(f'Class Mean Final Mark    : {class_mean:.2f}')
  print(f'Class Median Mark        : {class_median:.2f}')
  print(f'Standard Deviation       : {class_std:.2f}')
  print(f'Lowest Mark              : {class_min:.2f}')
  print(f'Highest Mark             : {class_max:.2f}')
  print(f'Strongest Subject        : {strongest_subject}')
  print(f'Weakest Subject          : {weakest_subject}')
  print('-' * 60)

  print('\n[Subject-wise Average Rankings]')
  print(subject_summary.to_string(index=False))

  print('\n[Section-wise Average Performance]')
  print(section_summary.to_string(index=False))

  print('\n[Top 3 Performing Students]')
  print(top_students[['student_id', 'name', 'section', 'subject', 'final_mark']].to_string(index=False))
  print('=' * 60)


if __name__ == '__main__':
  main()