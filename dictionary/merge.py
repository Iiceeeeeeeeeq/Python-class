#Merge - รวมข้อมูลในดิกเข้าด้วยกัน โดยใช้เครื่องหมาย | (ทับข้อมูลตาม key)
#Update - ใช้เครื่องหมาย |=
a= {
    "A" : "ant",
    "B" : "bird",
    "C" : "cat"
}
b = {
    "A" : "and",
    "B" : "boy",
}
c = {
    "A" : 1,
    "D" : 2
}

x=a|b
print (x)
y=b|c
print (y)
z= a|b|c
print (z)