n = "YES"
while(n == "YES"):
    import random
    rn = ["0", "0", "0"]
    rn[0] = str(random.randrange(0, 9, 1))
    rn[1] = rn[0]
    rn[2] = rn[0]
    while (rn[0] == rn[1]):
        rn[1] = str(random.randrange(0, 9, 1))
    while (rn[0] == rn[2] or rn[1] == rn[2]):
        rn[2] = str(random.randrange(0, 9, 1))


    t = 0
    s = 0
    b = 0

    print("")
    print("Start")
    while ( s < 3 ):
        num = str(input("3자리 숫자 입력 : "))
        x = num.isdigit()
        d = len(num)
        if(num == "0"):
            print("Exit")
            break
        elif(x == False):
            print("숫자가 아닙니다")
            continue
        elif(d != 3):
            print("숫자가 3개가 아닙니다")
            continue
        elif(num[0] == num[1] or num[1] == num[2] or num[0] == num[2]):
            print("숫자가 중복됩니다")
            continue

        s = 0
        b = 0

        for i in range(0, 3):
            for j in range(0, 3):
                if(num[i] == str(rn[j]) and i == j):
                    s += 1
                elif(num[i] == str(rn[j]) and i != j):
                    b += 1
            print("결과 : Strike :", s, " Ball :", b)

            t += 1
        if(num == "0"):
            break
        print(t, "번 만에 정답을 맞추셨습니다.")
        print("")
        print("Again? YES,NO")

        n = input()
        n= n.upper()
        if(n == "YES"):
            print ("Restart")
        elif(n == "NO"):
            print ("Exit")
            break
        elif(n != "NO"):
            while(n != "NO" or n != "YES"):
                print ("다시 입력")
                n = input()
                n= n.upper()
                if(n == "NO" or n == "YES"):break
            if(n == "NO"):
                print ("Exit")
                break
