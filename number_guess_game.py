import random
guess = 0
while guess < 4:
    guess += 1
    rand_num = random.randrange(10)
    guessed_num = int(input("Enter the chosen number : "))
    if guessed_num != rand_num:
        print("You have " + str(4-guess) + " left in your hand")
    else:
        print("\n🎉🎉🎉 you got me 🎉🎉🎉")
        break
print("\n\t 👏👏👏 We had a great play 👏👏👏")
print("Happy playing")
