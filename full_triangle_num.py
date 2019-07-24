space = ' '
count = 1
count2 = 1
masuk = int(input('berapa :'))
for kali in range(masuk):
    print((space*(masuk*2-1)) + ((str(count2)+space)*count))
    print('')
    masuk -= 1
    count += 2
    count2 += 1