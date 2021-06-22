print("Please think of a number between 0 and 100!")
l = 0
h = 100
ans = ''
while True:
    print("Is your secret number " + str((l + h) // 2) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans == 'h':
        h = (l + h) // 2
    elif ans == 'l':
        l = (l + h) // 2
    elif ans == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: " + str((l + h) // 2))