file = open('devices.txt', 'a')

while True:
    item = input('Enter device name (type "exit" to finish): ')
    if (item == 'exit'):
        break
    file.write('\n' + item)
file.close()

print('file saved successfully!')