path = r'C:\Users\HP\OneDrive\python.jpg'
key = int(input('Enter Key for encryption of Image : '))
print('The path of file : ', path)
print('Key for encryption : ', key)
fin = open(path, 'rb')
image = fin.read()
fin.close()
image = bytearray(image)
for index, values in enumerate(image):
        image[index] = values ^ key
fin = open(path, 'wb')
fin.write(image)
fin.close()
print('Encryption Done...')

	