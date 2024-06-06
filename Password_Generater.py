#All 112 character in the down 

k = "0123456789qwertyuıopğüişlkjhgfdsazxcvbnmöçQWERTYUIOPĞÜİŞLKJHGFDSAZXCVBNMÖÇ~`!@#£€$¢¥§%°^&*()-_+={]}[|\"/:;\'><,.\\?"

#This simple code make the 3 character password combinations
#Code make a .txt file and write all combinations 

ths = open("3Letter.txt","w")
for bas1 in k:
    for bas2 in k:
        for bas3 in k:
            password = (bas1+bas2+bas3)
            print(password)
            ths.write(password+"\n")

ths.close
