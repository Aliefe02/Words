import random
import subprocess
import time

word_list = 'qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ .,:;-_*?[]=()/&%+^!"é<>|1234567890'

word = input()
subprocess.run('cls',shell=True)
new_word = ''
temp = ''
for i in word:
    for j in word_list:
        time.sleep(0.0001)
        temp = new_word
        if j == i:
            new_word = new_word+j
            print(new_word)
            break
        temp = temp + j
        print(temp)
input()