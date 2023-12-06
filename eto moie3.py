z = 1342
с = 'чоч'

while True:
    print("напишите свой логин")
    x = str(input(" логин"))
    if x == с:
        print("правильно")
  

    print("напишите свой пароль")
    x = int(input("пароль"))
    if x == z:
        print("правильно")
        print("вы вощли в акк")
        break
    elif x > z:
        print("неправильный логин или пароль")
    elif x < z:
        print("неправильный логин или пароль")