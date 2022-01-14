def proverka1(a):
    for i in range(4):
     if a[i]>9 or a[i]<0:
        print('Число Первого игрока под номером:',i+1,' является двузначным.Введите вместо него однозначное.')
        a[i] = int(input('нужно ввести число от 1 до 9:'))
def proverka12(a): 
    while (a[0] == a[1] or a[0] == a[2] or a[0] == a[3] or a[1] == a[0] or a[1] == a[2] or a[1] == a[3] or a[2] == a[0] or a[2] == a[1] or a[2] == a[3] or a[3] == a[0] or a[3] == a[1] or a[3] == a[2]):
        if a[0] == a[1] or a[0] == a[2] or a[0] == a[3]:
            print('Игрок1.Нужно ввести цифры,которые не повторяются,перевведите первое число на неповторяющееся: ')
            a[0] = int(input())
            print()       
        elif a[1] == a[0] or a[1] == a[2] or a[1] == a[3]:      
            print('Игрок1.Нужно ввести цифры,которые не повторяются,перевведите второе число на неповторяющееся: ')
            a[1] = int(input())
            print()
        elif a[2] == a[0] or a[2] == a[1] or a[2] == a[3]:
            print('Игрок1.Нужно ввести цифры,которые не повторяются,перевведите третье число на неповторяющееся: ')
            a[2] = int(input())
            print()
        elif a[3] == a[0] or a[3] == a[1] or a[2] == a[2]:
            print('Игрок1.Нужно ввести цифры,которые не повторяются,перевведите четвертое число на неповторяющееся: ')
            a[3] = int(input())
            print()
def proverka2(b):
     while (b[0] == b[1] or b[0] == b[2] or b[0] == b[3] or b[1] == b[0] or b[1] == b[2] or b[1] == b[3] or b[2] == b[0] or b[2] == b[1] or b[2] == b[3] or b[3] == b[0] or b[3] == b[1] or b[3] == b[2]):
        if b[0] == b[1] or b[0] == b[2] or b[0] == b[3]:
            print('Игрок2.Нужно ввести цифры,которые не повторяются,перевведите первое число на неповторяющееся: ')
            b[0] = int(input())
            print()
        elif b[1] == b[0] or b[1] == b[2] or b[1] == b[3]:    
            print('Игрок2.Нужно ввести цифры,которые не повторяются,перевведите второе число на неповторяющееся: ')
            b[1] = int(input())
            print()
        elif b[2] == b[0] or b[2] == b[1] or b[2] == b[3]:
            print('Игрок2.Нужно ввести цифры,которые не повторяются,перевведите третье число на неповторяющееся: ')
            b[2] = int(input())
            print()
        elif b[3] == b[0] or b[3] == b[1] or b[2] == b[2]:
            print('Игрок2.Нужно ввести цифры,которые не повторяются,перевведите четвертое число на неповторяющееся: ')
            b[3] = int(input())
            print()

def proverka21(b):
    for i in range(4):
        if b[i]>9 or b[i]<0:
            print('Число Второго игрока под номером:',i+1,' является двузначным.Введите вместо него однозначное.')
            b[i] = int(input('нужно ввести число от 1 до 9: '))
def proverka3(c):
    for i in range(4):
        if c[i]>9 or c[i]<0:
            print('Число Первого игрока,которое он пытается угадать, под номером:',i+1,' является двузначным.Введите вместо него однозначное.')
            c[i] = int(input('нужно ввести число от 1 до 9:')) 
def proverka4(d):
     for i in range(4):
         if d[i]>9 or d[i]<0:
            print('Число Первого игрока,которое он пытается угадать, под номером:',i+1,' является двузначным.Введите вместо него однозначное.')
            d[i] = int(input('нужно ввести число от 1 до 9:'))  
    
def prog():
    try:
        import random as r

        play = int(input('Если хотите играть с игроком,введите 1,иначе 2: '))

        if play == 1:
            flag3 = bool(True)
            b1 = int()
            b2 = int()
            kor1 = int()
            kor2 = int()
            bilo1 =[]
            bilo2 =[]
            a = []
            b = []
            c = []
            c2 =[]
            for i in range(4):
                c2.append(int(0))
            d = []
            d2=[]
            for i in range(4):
                d2.append(int(0))

            for i in range(4):
                a.append(int(input('Первый игрок вводит число от 1 до 9(по одной цифре за раз): ')))

            for i in range(4):
                b.append(int(input('Второй игрок вводит число(по одной цифре за раз): ')))

            proverka1(a)
            proverka12(b)
            proverka2(a)
            proverka21(b)

            while flag3 == True:
                b1 = 0
                b2 = 0
                c = []
                d = []

                for i in range(4):
                    c.append(int(input('Первый игрок пытается угадать число второго(по одной цифре от 1 до 9 за раз): ')))
            
                for i in range(4):
                    d.append(int(input('Второй игрок вводит число от 1 до 9(по одной цифре за раз): ')))

                proverka3(c)
                proverka4(c)
                for i in range(4):
                    if c[i] == b[i]:
                        b1 = b1 +1
                        c2[i] = b[i]
                print('Быки первого игрока: ',b1)

                for i in range(4):
                    if d[i] == a[i]:
                        b2 = b2 + 1
                        d2[i] = a[i]
                print('Быки второго игрока: ',b2)


                for i in range(4):
                    if c[i]!=b[i] and c[i] in b:
                        if c[i] in bilo1:
                            kor1=kor1
                        else:
                            kor1 = kor1 +1
                            bilo1.append(c[i])
                print('Коровы первого игрока',kor1)
                print(bilo1)

                for i in range(4):
                    if d[i]!=a[i] and d[i] in a:
                        if d[i] in bilo2:
                            kor2=kor2
                        else:
                            kor2=kor2+1
                            bilo2.append(d[i])
                print('Коровы второго игрока',kor2)
                print(bilo2)

                print('Числа, которые угадал Первый игрок: ',c2)
                print('Числа, которые угадал Второй игрок: ',d2)
                

                if b1 == 4 and b2 ==4:
                    print('Ничья')
                    flag3=False
                elif b1==4:
                    print('Победа первого игрока')
                    flag3=False
                elif b2==4:
                    print('Победа второго игрока')
                    flag3=False


        elif play ==2:
            scht = int()
            a = []
            b = []
            d1 =[]
            flag = bool(True)
            for i in range(4):
                d1.append(int(0))
            b1 = int()
            b2 = int()
            kor1 = int()
            kor2 = int()
            c = []
            c1 =[]
            for i in range(4):
                c1.append(int(0))
            d = []
            bilo1 = []
            bilo2 = []

            for i in range(4):
                a.append(int(input('Игрок вводит число для компьютера(по одной цифре за раз): ')))
            proverka2(a)
            proverka1(a)
           
            for i in range(4):
                b.append(int(r.uniform(1,9)))
            while (b[0] == b[1] or b[0] == b[2] or b[0] == b[3] or b[1] == b[0] or b[1] == b[2] or b[1] == b[3] or b[2] == b[0] or b[2] == b[1] or b[2] == b[3] or b[3] == b[0] or b[3] == b[1] or b[3] == b[2]):
                    if b[0] == b[1] or b[0] == b[2] or b[0] == b[3]:
                        b[0] = int(r.uniform(1,9))
                    elif b[1] == b[0] or b[1] == b[2] or b[1] == b[3]:
                        b[1] = int(r.uniform(1,9))
                    elif b[2] == b[0] or b[2] == b[1] or b[2] == b[3]:
                        b[2] = int(r.uniform(1,9))
                    elif b[3] == b[0] or b[3] == b[1] or b[2] == b[2]:
                        b[3] = int(r.uniform(1,9))
            print('Число игрока: ',a)

            while flag == True:
                d = []
                c = []
                b1 = 0
                b2 = 0


                for i in range(4):
                    c.append(int(input('Игрок пытается угадать число компьютера(по одной цифре за раз): ')))
                proverka3(c)

                for i in range(4):
                    d.append(int(r.uniform(1,9)))

                if scht == 4 and (d1[0] == 0 or d1[1] == 0 or d1[2] == 0 or d1[3] ==0):
                    if d1[0] == 0:
                        d[0] = r.choice(bilo2)
                    if d1[1] == 0:
                        d[1] = r.choice(bilo2)
                    if d1[2] == 0:
                        d[2] = r.choice(bilo2)
                    if d1[3] == 0:
                        d[3] = r.choice(bilo2)

                for i in range(4):
                    if c[i] == b[i]:
                        b1 = b1 + 1
                        c1[i] = b[i]
                print('Быки первого игрока:',b1)
                print('Числа,которые игрок угадал',c1)
                

                for i in range(4):
                    if d[i] == a[i]:
                        d1[i] = d[i]
                    if d1[i]!=0:
                        b2=b2+1
                    
                print('Быки компьютера:',b2)
                print(d1)

                for i in range(4):
                    if c[i]!=b[i] and c[i] in b:
                        if c[i] in bilo1:
                            kor1=kor1
                        else:
                            kor1=kor1+1
                            bilo1.append(c[i])
                print('Коровы игрока',kor1)
                print(bilo1)

                for i in range(4):
                    if d[i]!=a[i] and d[i] in a:
                        if d[i] in bilo2:
                            kor2=kor2
                        else:
                            kor2=kor2+1
                            bilo2.append(d[i])
                            scht = scht + 1
                print('Коровы компьютера',kor2)
                print(bilo2)

                if b1 == 4 and b2 ==4:
                    print('Ничья')
                    flag = False
                elif b1==4:
                    print('Победа игрока')
                    flag = False
                elif b2==4:
                    print('Роботы скоро захватят мир...')
                    flag = False
            
    except ValueError:
        print('нужно вводить только цифры')
        prog()
prog()
        
