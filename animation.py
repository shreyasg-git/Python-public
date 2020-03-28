import os
import time
os.system('cls')
filenames = ['1.txt', '2.txt', '3.txt', '4.txt', ' 5.txt', '6.txt', '7.txt', '8.txt', '9.txt', '10.txt']
# filenames=['01.txt','02.txt','03.txt','04.txt']
frames = []
for name in filenames:
    with open(name, 'r', encoding='utf8') as f:
        frames.append(f.readlines())

for frame in frames:
    print(''.join(frame))
    time.sleep(0.1)
    os.system('cls')
