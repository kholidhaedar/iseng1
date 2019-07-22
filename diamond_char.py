space = ' '
chara = '#'
count = 1
masuk = int(input('berapa :'))
count2 = masuk
for kali in range(count2):
    print((space*(count2-1)) + (chara*count))
    count += 2
    count2 -= 1
    if kali == masuk-1:
        count = 1
        for kali in range(masuk-1):
            print((space*count) + (chara*((masuk-1)*2-1)))
            count += 1
            masuk -= 1