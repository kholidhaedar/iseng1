space = ' '
chara = '#'
count = 1
masuk = int(input('berapa :'))
for kali in range(masuk):
    print((space*(masuk-1)) + (chara*count))
    count += 1
    masuk -= 1