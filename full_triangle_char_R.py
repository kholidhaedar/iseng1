space = ' '
chara = '#'
count = 0
masuk = int(input('berapa :'))
for kali in range(masuk):
    print((space*count) + (chara*(masuk*2-1)))
    count += 1
    masuk -= 1