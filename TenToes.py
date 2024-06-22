import sys
import time
from time import sleep

def print_lirik(): #function
    baris = [
        ("these memories, end in tragedy", 0.1),
        ("And all of these places, all of these faces", 0.07),
        ("I didn't wanna let you down", 0.09),
        ("And all these mistakes of mine, I can't replace it", 0.05),
        ("I gotta move on somehow", 0.09),
        ("Healing energy on me", 0.09),
        ("Baby, all I really need's one thing", 0.09),
        ("Healing energy on me", 0.09),
        ("Baby, can you make a wish for me?", 0.09)
    ]

    jeda = [1.2, 0.9, 0.8, 0.5, 1.0, 1.0, 0.7, 1.2, 1.2]  #array jeda baris

    for i, (line, char_jeda) in enumerate(baris): #loop bwt output
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_jeda) #var buat 
        print('')
        sleep(jeda[i])  #make array jeda baris (idk why this line has traceback)

print_lirik() #manggil function
