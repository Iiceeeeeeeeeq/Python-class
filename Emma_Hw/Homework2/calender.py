print("Please enter the date by using number.")
D = input("Day: ")
M = int(input("Mouth: "))
Y = input("Year: ")

M_dic = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}

print(f"{M_dic[M]}  {D} , {Y}")