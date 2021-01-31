import random   #used for Random valurs
import time     #used for Time

#initial Steps to invite Player in the Game

print("\nWelcome to Hangman game by Mukul verma")

name=input("Enter Your Name : ")
print("Hello "+name+"! Best of luck")

time.sleep(2)   #This is used to halt the execution of the program for a few seconds.

print("The Game is about to start!\n Let's Play HANGMAN")

time.sleep(3)


#main() Function
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_" * length
    already_guessed = []
    play_game = ""

#A Loop to re-execute the game when the first round ends

def play_loop():
    global play_loop
    play_game = input("Do You wanna Play again? Y = Yes, N = No\n")
    while play_game not in ["y","Y","n","N"]:
        play_game = input("Do You wanna Play again? Y = Yes, N = No\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks for playing! We expect you back again")
        exit()

#Function for the HangMan Activity

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game

    limit = 5
    guess = input("This is the HangMan word : "+display+" \nEnter your guess : \n")
    guess = guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another Letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   ------ \n"
                  "   |      \n"
                  "   |      \n"
                  "   |      \n"
                  "   |      \n"
                  "   |      \n"
                  "   |      \n"
                  "___|___\n")
            print("Wrong guess."+str(limit - count)+"guess remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   ------ \n"
                  "   |     |\n"
                  "   |      \n"
                  "   |      \n"
                  "   |      \n"
                  "   |      \n"
                  "   |      \n"
                  "___|___\n")
            print("Wrong guess."+str(limit - count)+"guess remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   ------ \n"
                  "   |     |\n"
                  "   |     O\n"
                  "   |      \n"
                  "   |      \n"
                  "   |      \n"
                  "   |      \n"
                  "___|___\n")
            print("Wrong guess."+str(limit - count)+"guess remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   ------ \n"
                  "   |     |\n"
                  "   |     O\n"
                  "   |    /|\ \n"
                  "   |      \n"
                  "   |      \n"
                  "   |      \n"
                  "___|___\n")
            print("Wrong guess." + str(limit - count) + "guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   ------ \n"
                  "   |     |\n"
                  "   |     O\n"
                  "   |    /|\ \n"
                  "   |    / \ \n"
                  "   |      \n"
                  "   |      \n"
                  "___|___\n")
            print("Wrong guess." + str(limit - count) + "guess remaining\n")

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()

main()

hangman()