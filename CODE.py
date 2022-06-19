    F = (p - 1) * (q - 1)
    for i in range(2, F):
        if (gcd(i, F) == 1):
            e = i
            break
i = 0
    while (i * e % F != 1):
        i += 1
        d = i
        if i == e:
            i += 1
    C = M ** e % n
    print("crypt message: ",C)
    print(e)
    print(d)
    print(n)
elif Vopros == 1:
    print("Enter Private Key")
    d = int(input("d = "))
    n = int(input("n = "))
    c = int(input("Enter what need to decrypt  = "))  # ie % F = 1 !@! id = 1 (mod F)
    M = (c ** d) % n
    print("Decrypt message = ",M)