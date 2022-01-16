import random
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

range = 0

while True:
    try:
        range = int(input("Type number range: "))
        break
    except:
        continue

gotit = random.randint(1, range)
attempts = 0

while True:
    try:
        clearConsole()
        print("Guess the number!")
        guess = int(input("input: "))
        
        if guess != gotit:
            attempts+=1
            continue
        else:
            attempts+=1
            break
    except:
        continue

clearConsole()
print(f"""
You've guessed the number!

attempts: {attempts}
""")
