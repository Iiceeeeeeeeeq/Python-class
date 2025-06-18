Interested = input()
words = input() 
s = ' '
for i in words :
    if i in ['"','(',')',',','.',"'"]:
        s += ' '
        print(s)
    else :
        s += i
# print(s) 
i = 0
for w in s.split():
    if w == Interested :
        i += 1
print(i)




