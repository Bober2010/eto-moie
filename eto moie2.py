z = 1342
while True:
    print("я создал пароль угадай его!")
    x = int(input("ваша догадка"))
    if x == z:
        print("ты угадал")
        break
    elif x > z:
        print("не угадал")
    elif x < z:
        print("не угадал")