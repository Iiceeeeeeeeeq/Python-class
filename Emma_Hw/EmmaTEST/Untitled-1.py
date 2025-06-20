print("guess a correct number 1-10")
number = 0 #ต้องประกาศไว้ก่อนเพื่อให้เงื่อนไขของลูปทำงานได้

while number != 8:
    number = int(input("guess the number : "))
    if number > 8:
        print("incorrect, try lower number")
    elif number < 8:
        print("incorrect, try higher number")
    else:
<<<<<<< HEAD
        print("CORRECT!")
=======
        print("CORRECT!")
>>>>>>> 15661a26b27b32f87a1a822ad5977d622c6b2b0a
