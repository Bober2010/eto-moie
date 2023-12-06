z = 1342
c = 0000
while True:
    print("напишите свой логин")
    x = int(input("логин"))
    if x == c:
        print("правильно")
        break
    elif x > c:
        print("логин неверен")
    elif x < c:
        print("логин неверен")
while True:
    print("напишите свой пароль")
    x = int(input("пароль"))
    if x == z:
        print("правильно")
        print(" вы вошли в акк")
        break
    elif x > z:
        print("пароль неверен")
    elif x < z:
        print("пароль неверен")