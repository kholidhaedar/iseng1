space = ' '
count = 0
masuk = int(input('berapa :'))
for kali in range(masuk):
    print((space*count) + ((str(masuk)+space)*(masuk*2-1)))
    print('')
    masuk -= 1
    count += 2