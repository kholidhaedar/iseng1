space = ' '
count = 0
masuk = int(input('berapa :'))
for kali in range(masuk):
    print((space*count) + ((str(masuk)+space)*masuk))
    count += 2
    masuk -= 1