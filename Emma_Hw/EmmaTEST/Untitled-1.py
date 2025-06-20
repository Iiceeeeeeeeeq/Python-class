print("guess a correct number 1-10")
number = 0 #ต้องประกาศไว้ก่อนเพื่อให้เงื่อนไขของลูปทำงานได้

while number != 8:
    number = int(input("guess the number : "))
    if number > 8:
        print("incorrect, try lower number")
    elif number < 8:
        print("incorrect, try higher number")
    else:
        print("CORRECT!")
