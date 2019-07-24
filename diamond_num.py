space = ' '
count = 1
count2 = 1
masuk = int(input('berapa :'))
count3 = masuk
for kali in range(masuk):
    print((space*(masuk*2-1)) + ((str(count2)+space)*count))
    print('')
    masuk -= 1
    count += 2
    count2 += 1
    if kali == count3-1:
        count = 3
        for kali in range(count3-1):
            print((space*count) + ((str(count3-1)+space)*((count3-1)*2-1)))
            print('')
            count += 2
            count3 -= 1