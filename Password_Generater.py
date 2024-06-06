
k = "0123456789qwertyuıopğüişlkjhgfdsazxcvbnmöçQWERTYUIOPĞÜİŞLKJHGFDSAZXCVBNMÖÇ~`!@#£€$¢¥§%°^&*()-_+={]}[|\"/:;\'><,.\\?"

ths = open("3Letter.txt","w")
for bas1 in k:
    for bas2 in k:
        for bas3 in k:
            password = (bas1+bas2+bas3)
            print(password)
            ths.write(password+"\n")

ths.close
