from enigma import enigma
import base64

eni = enigma()

def ReadBytes(filename):
    with open(filename,'rb') as file:
        while True:
            byte = file.read(1)
            if byte:
                yield byte
            else:
                break

plain = ''
for b in ReadBytes('asset/myimage.jpg'):
    # i = int.from_bytes(b,byteorder='big')
    bhex = b.hex()
    for i in bhex:
        for index in range(1):
            #print(bhex[index],end="")
            plain += bhex[index]
    #print(eni.run(bhex))
    # print(f"raw({b}) - int({i}) - binary({bin(i)})")
eni.run(plain)