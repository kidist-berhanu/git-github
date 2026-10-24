# Interactive BMI Calculator and CSV Data Logger

**A Python project for calculating Body Mass Index (BMI) and recording results in a CSV file.**

## 1. Overview

The Interactive BMI Calculator is a Python application that accepts a user's weight and height, calculates their Body Mass Index (BMI), classifies the result into a standard adult BMI category and records the calculation in a CSV file.


## 2. Features

- **Interactive input:** Accepts weight in kilograms and height in meters.
- **BMI calculation:** Computes BMI using the standard mathematical formula.
- **BMI classification:** Categorizes results as Underweight, Normal, Overweight or Obesity range.
- **CSV data logging:** Saves each successful calculation in `sample_data.csv`.
- **Record preservation:** Appends new results to the existing CSV file rather than replacing previous records.
- **Input validation:** Rejects non-positive weight or height values.

## 3. Technologies Used

| Python 3 | Program logic and BMI calculations |
| CSV module | Writing structured data to a CSV file |
| OS module | Checking whether the output file exists |
| Git | Tracking project changes |
| GitHub | Hosting the project repository |

The CSV and OS modules are included in Python's standard library, so no additional Python packages are required.

## 4. Project Structure

git_github_assignment/
├── sample_data.py
├── sample_data.csv
└── README.md

## 5. BMI Calculation and Classification

BMI is calculated using the following formula:

**BMI = Weight (kg) / Height (m)²**

The program uses these general adult BMI categories:

| Below 18.5 | Underweight |
| 18.5 to below 25 | Normal |
| 25 to below 30 | Overweight |
| 30 and above | Obesity range |


## 6. Example Execution

Enter your weight in kg: 60
Enter your height in meters: 1.65

Your BMI is: 22.04
Conclusion: Normal
Your results have been saved to sample_data.csv.

## 7. Output Dataset

The program creates or updates sample_data.csv with the following columns:

Weight (kg)  Height (m)  BMI   Conclusion

60           1.65        22.04   Normal

Each successful calculation is added as a new row, allowing multiple results to be recorded in the same file.

The CSV file is created automatically when the program runs. If it already exists, new results are appended to it.

## Conclusion 

This project demonstrates the practical application of Python for interactive calculations and structured data storage. It also provides experience with CSV file handling, input validation, version control and publishing source code through GitHub.

## Author

**Name:** Kidist Berhanu

**Project:** Git and GitHub 

