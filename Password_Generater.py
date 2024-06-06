
k = "0123456789qwertyuıopğüişlkjhgfdsazxcvbnmöçQWERTYUIOPĞÜİŞLKJHGFDSAZXCVBNMÖÇ~`!@#£€$¢¥§%°^&*()-_+={]}[|\"/:;\'><,.\\?"

for bas1 in k:
    for bas2 in k:
        for bas3 in k:
            for bas4 in k:
                password = (bas1+bas2+bas3+bas4)
                print(password)
