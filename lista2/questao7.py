def lista_primos():
    yield 2
    p = 2
    while True:
        p += 1
        for i in range(2,p+1,1):
            if p % i == 0 and i != p:
                break
            if i == p:
                yield p

#gen = lista_primos()
#for i in range(15):
#    print(next(gen))
