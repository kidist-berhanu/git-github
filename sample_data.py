
import csv
import os

# Create the CSV file and write the column headings
file_exists = os.path.exists("sample_data.csv")

with open("sample_data.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    if not file_exists or os.path.getsize("sample_data.csv") == 0:
        writer.writerow(["#", "Weight (kg)", "Height (m)", "BMI", "Conclusion"])

    # Ask the user for input
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    # Validate the input
    if weight <= 0 or height <= 0:
        print("Weight and height must be greater than zero.")
    else:
        # Calculate BMI
        bmi = weight / (height ** 2)

        # Determine the conclusion
        if bmi < 18.5:
            conclusion = "Underweight"
        elif bmi < 25:
            conclusion = "Normal"
        elif bmi < 30:
            conclusion = "Overweight"
        else:
            conclusion = "Obesity range"

        # Display the result
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Conclusion: {conclusion}")

        # Save the results in the CSV file
        writer.writerow([
            sum(1 for _ in open("sample_data.csv", encoding="utf-8")),
            weight,
            height,
            round(bmi, 2),
            conclusion
        ])

        print("Your results have been saved to sample_data.csv.")
