# Python Count Intereset Calculator

principle = 0
time = 0
rate = 0

while True:
    principle = float(input("Enter the principle amount: ")) 
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the Interest rate: ")) 
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break

while True:
    time = float(input("Enter the time in year: ")) 
    if time <= 0:
        print("time can't be less than or equal to zero")
    else:
        break
    
total = principle * pow((1 + rate / 100), time)
print(f"The total amount after {time} years will be {total:.2f}")
