import sys

RATE_PER_UNIT = 5.0  

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    units = float(sys.argv[1])
    print("User provided input units:")
else:
    script_name = sys.argv[0]
    units = 100.0
    print("No input given - using default units (100):")

bill_amount = units * RATE_PER_UNIT

print("Script Name:", script_name)
print("Units consumed:", units)
print("Rate per unit (Rs):", RATE_PER_UNIT)  
print("Total electricity bill (Rs):", bill_amount) 
