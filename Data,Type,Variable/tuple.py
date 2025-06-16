#tuple-เป็นการเก็บข้อมูลคล้ายลิสต์แต่จะไม่สามารถเปลี่ยนแปลงค่าของข้อมูลในลิสต์ได้

#Ex1
shape_tuple1 = ["square","heart","circle","star"]
color_tuple2 = ["black","pink","blue","green"]

lenght = len(shape_tuple1)
print("shape_tuple1=",lenght)
print("shape_tuple1[0]",shape_tuple1[0])
print("shape_tuple1[3]",shape_tuple1[3])
print("shape_tuple1[-1]",shape_tuple1[-1])
print("shape_tuple1[0:2]",shape_tuple1[0:2])
print("shape_tuple1[-2:]",shape_tuple1[-2:])
print("shape_tuple1[:3]",shape_tuple1[:3])

shape_color=shape_tuple1+color_tuple2
print(shape_color)
print(type(shape_tuple1))

