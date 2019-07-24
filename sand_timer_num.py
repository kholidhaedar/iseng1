space = ' '
count = 0
masuk = int(input('berapa :'))
count2 = masuk
for kali in range(masuk):
    print((space*count) + ((str(masuk)+space)*(masuk*2-1)))
    print('')
    masuk -= 1
    count += 2
    if kali == count2-1:
        count = 3
        count3 = 2
        for kali in range(count2-1):
            print((space*((count2-2)*2)) + (str(count3)+space)*count)
            print('')
            count += 2
            count2 -= 1
            count3 += 1