def compute_bmi(weight, height):
    """
    Computes the Body Mass Index (BMI) using the standard formula.
    The weight parameter represents the user's weight in kilograms.
    The height parameter represents the user's height in meters.
    The function returns the calculated BMI as a floating-point number.
    Ensure that both parameters are positive real numbers.
    Handle cases where the input is not valid, such as negative values or non-numeric input.
    """
    if weight <=  0 or height <=  0:
        raise ValueError("Weight and height must be positive real numbers.")
    else:
        bmi_index = weight / (height **  2)
        bmi_index =  round(bmi_index, 1)
        return bmi_index


def category_bmi(bmi_index):
    """
    Determines the BMI category based on the given BMI index.
    The bmi_index parameter is the computed BMI value.
    The function uses predefined BMI ranges to assign categories.
    Returns the category as a string (e.g., "Underweight", "Normal", "Overweight").
    Ensure that the bmi_index is a valid positive real number.
    """
    
    if bmi_index <=  18.5:
        return "Underweight"
    elif  18.5 < bmi_index <=  24.9:
        return "Normal"
    elif  24.9 < bmi_index <=  29.9:
        return "Overweight"
    else:
        return "Obese"


def display_bmi(category, bmi_index):
    """
    Displays the BMI result to the user in a clear and friendly format.
    The category parameter is the determined BMI category.
    Uses f-strings for formatting the output message.
    Prints the result to the console.
    Ensures that the category is a valid string value.
    """
    print('\nRESULTS')
    print('_'*100)
    print(f"Your BMI is: {bmi_index} ")
    print(f"Your BMI category is: {category}")


def main():
    while True:
        try:
            user_weight = float(input("Enter your weight in kilograms: "))
            user_height = float(input("Enter your height in meters: "))
            
            if user_weight <=  0 or user_height <=  0:
                print("Invalid input. Please enter a positive real number for both weight and height.")
                print()
            else:
                break
                
        except ValueError:
            print("Invalid input. Please enter a positive real number for both weight and height.")

    bmi_index = compute_bmi(user_weight, user_height)
    category = category_bmi(bmi_index)
    display_bmi(category, bmi_index)


if __name__ == "__main__":
    main()