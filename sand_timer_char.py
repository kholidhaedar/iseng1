space = ' '
chara = '#'
count = 0
masuk = int(input('berapa :'))
count2 = masuk
for kali in range(count2):
    print((space*count) + (chara*(count2*2-1)))
    count += 1
    count2 -= 1
    if kali == masuk-1:
        count = 3
        for kali in range(masuk-1):
            print((space*(masuk-2)) + (chara*count))
            count += 2
            masuk -= 1