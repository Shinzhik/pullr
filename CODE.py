elif Vopros == 1:
    print("Enter Private Key")
    d = int(input("d = "))
    n = int(input("n = "))
    c = int(input("Enter what need to decrypt  = "))  # ie % F = 1 !@! id = 1 (mod F)
    M = (c ** d) % n
    print("Decrypt message = ",M)