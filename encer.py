import enigma
import base64

def ReadBytes(filename, nBytes):
    with open(filename,'rb') as file:
        while True:
            byte = file.read(1)
            if byte:
                yield byte
            else:
                break

            if nBytes > 0:
                nBytes -= 1 
                if nBytes == 0:
                    break

for b in ReadBytes('myimage.jpg',5):
    i = int.from_bytes(b,byteorder='big')
    print(f"raw({b}) - int({i}) - binary({bin(i)})")