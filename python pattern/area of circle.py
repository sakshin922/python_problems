import math

def calculate_circle_area(radius):
 
  if radius < 0:
    return "Radius cannot be negative."
  
  area = math.pi * (radius ** 2)
  return area

# Get input from the user
try:
  radius_input = float(input("Enter the radius of the circle: "))
  
  # Calculate and print the area
  area_of_circle = calculate_circle_area(radius_input)
  
  if isinstance(area_of_circle, str):
    print(area_of_circle)
  else:
    print(f"The area of the circle with radius {radius_input} is: {area_of_circle:.2f}")

except ValueError:
  print("Invalid input. Please enter a valid number for the radius.")