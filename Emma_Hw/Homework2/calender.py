print("Please enter the date by using number.")
D = input("Day: ")
M = int(input("Mouth: "))
Y = input("Year: ")

MONTH = [
    "","January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"
]

print(f"{MONTH[M]}  {D} , {Y}")