def calculate_bmi(height_cm, weight_kg):
  if height_cm <= 0 or weight_kg <= 0:
    return "Invalid input."
  height_m = height_cm / 100
  return weight_kg / (height_m * height_m)

def interpret_bmi(bmi):
  if bmi <= 0:
    return "Invalid BMI value."
  elif bmi <= 16:
    return "Severely underweight"
  elif bmi <= 18.5:
    return "Underweight"
  elif bmi <= 25:
    return "Healthy"
  elif bmi <= 30:
    return "Overweight"
  else:
    return "Severely overweight"

height_cm = float(input("Enter your height in centimeters: "))
weight_kg = float(input("Enter your weight in kilograms: "))

bmi = calculate_bmi(height_cm, weight_kg)

if isinstance(bmi, str):
  print(bmi)
else:
  print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")
  print(f"BMI Interpretation: {interpret_bmi(bmi)}")