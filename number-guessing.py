import random

print("Number guessing is a simple game to beat.\nAll you have to do is guessing the number.\nIt's easy, isn't it?\nPS: Random number range: 0-99")
number = random.randint(0,99)
print(number)
while True:
    guess = int(input("Type the number please: "))
    if guess == number:
        print("You won!")
    else:
        if guess > number:
            print("Hmm, maybe try lowering the number?")
        else:
            print("Hmm, maybe try highering the number?")
