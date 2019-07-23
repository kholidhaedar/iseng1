space = ' '
count = 1
masuk = int(input('berapa :'))
for kali in range(masuk):
    print((space*(masuk*2-1)) + ((str(count)+space)*count))
    count += 1
    masuk -= 1