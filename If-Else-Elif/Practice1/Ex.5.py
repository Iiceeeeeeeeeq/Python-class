num1,num2,num3,num4 = map(int,input("โปรดใส่จำนวนเต็ม 4 จำนวน : ").split())
list_num = [num1,num2,num3,num4]

list_num.remove(max(list_num))
list_num.remove(min(list_num))

total = list_num[0] + list_num[1]
print (total)