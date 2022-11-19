'''from random import randint

a = 0
b = 0

nnpode = [[a + 200, b + 200],[a + 300, b + 400],[a+400, b+50],[a+700, b+50],[a+900, b+350]]


nnpode2 = {
    "tio juca":((a + 200, b + 200)),
    "vo jose paulino": ((a + 300, b + 400)),
    "tia maria":((a+400, b+50)),
    "tia sinhazinha":((a+700, b+50)),
    "primos":((a+900, b+350))
}

posicoesx = []
posicoesy = []
while True:
    #x_marrom=randint(40,1100)
    #y_marrom=randint(50,550)
    x_marrom = randint(40, 1100)
    for c in nnpode:
        #print(c[0])
        posicoesx.append(c[0])

    print(posicoesx)
    if x_marrom in posicoesx:
        print("valor igual")
        posicoesx = []
    else:
        print("passou: ",x_marrom)
        break


while True:
    y_marrom = randint(50, 550)
    for c in nnpode:
        posicoesy.append(c[1])
    
    print(posicoesy)
    if y_marrom in posicoesy:
        print("valor igual")
        posicoesy = []
    else:
        print("passou(y): ",y_marrom)
        break
'''
tst = {
    "pessoa1": "Douglas",
    "pessoa2": "Bernardo"

}

tst["pessoa3"] = "Nicolas"
print(tst)

