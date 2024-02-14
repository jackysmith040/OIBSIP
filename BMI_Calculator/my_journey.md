# My Journey in Building a BMI Calculator

## Thought Process and Algorithm

My journey in building a BMI calculator started with a clear understanding of the problem domain. I identified the inputs required (weight and height), the desired outputs (BMI and category), and the format for presenting the results. I planned to handle errors gracefully and ensure that the application could handle both numeric and non-numeric inputs.

The algorithm for calculating BMI is straightforward:

1. Prompt the user for their weight in kilograms and height in meters.
2. Validate the inputs to ensure they are positive real numbers.
3. Calculate the BMI using the formula: `weight / (height * height)`.
4. Determine the BMI category based on the calculated index.
5. Display the results to the user in a user-friendly format.

## Simple Documentation for BMI Calculator

The `bmi_calculator.py` script implements a simple BMI calculator with the following key components:

### Input Validation
The script prompts the user for their weight and height and validates the inputs to ensure they are positive real numbers.

### BMI Calculation
The `compute_bmi` function takes the weight and height as arguments and calculates the BMI using the standard formula.

### BMI Category Determination
The `category_bmi` function categorizes the BMI index into one of four categories: Underweight, Normal, Overweight, or Obese.

### Result Presentation
The `display_bmi` function presents the calculated BMI and its category to the user in a clear and friendly format.

### Main Execution
The `main` function orchestrates the execution of the above components, ensuring a logical flow from input collection to result presentation.
