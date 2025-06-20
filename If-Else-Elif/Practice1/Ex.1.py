num = input("กรุณาใส่ตัวเลขมาสามตัว และโปรดเว้นช่องว่างแต่ละตัวเลข : ").split()
number = [int(num[0]) , int(num[1]) , int(num[2])]
number_new = sorted(number)
#หาค่ามัธยฐาน
print (number_new[1])

