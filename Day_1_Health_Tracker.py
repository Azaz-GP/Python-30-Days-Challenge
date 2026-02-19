# Day 1: Health Tracker - 4-Week Transformation Forecast
# A simple tool to predict waist circumference reduction based on activity levels.

print("--- Welcome to the Health Tracker Forecast ---")
initial_waist = float(input("Enter starting waist (inches): "))

# 1. Input Validation
while True:
    workout = int(input("Enter workout days per week (0-7): "))
    if 0 <= workout <= 7: 
        break
    print(f"Invalid input! Please enter a number between 0 and 7.")

while True:
    steps = int(input("Enter average daily steps (0-20000): "))
    if 0 <= steps <= 20000: 
        break
    print(f"Invalid input! Please enter a number between 0 and 20000.")

print("\n--- 4-Week Transformation Forecast ---")
waist = initial_waist
week = 1

while week <= 4:
    # Forecast Logic based on activity intensity
    if steps >= 10000 and workout >= 4:
        waist -= 0.25
        status = "Extreme Burn (High Intensity)"
    elif steps >= 7000 or workout >= 3:
        waist -= 0.15
        status = "Steady Progress (Moderate)"
    else:
        waist -= 0.05
        status = "Minimal Change (Low Activity)"
    
    print(f"Week {week}: {status:<30} | Current Waist: {waist:.2f}\"")
    week += 1 

print("-" * 40)

print(f"[RESULT] Final Size: {waist:.2f}\" | Total Loss: {initial_waist - waist:.2f}\"")
