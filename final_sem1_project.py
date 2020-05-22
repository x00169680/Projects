""" Name: Simon Brennan
Student Number: X00169680
CA PROJECT - FINAL"""

"""1) MENU"""

# 1) Present Menu
print("*" * 20)
print("       Menu     ")
print("*" * 20)
print("  1)  Examine DNA ")
print("  2)  Play Hangman ")
print("  3)  Exit ")

# 2) Prompt user for selection
menuChoice = int(input("Enter your selection (1) (2) or (3): "))

# 3) Actions for choice & continually display menu on exit
if menuChoice == 1:
    print("You have selected to Examine DNA!")
elif menuChoice == 2:
    print("You have selected to Play Hangman!")
while menuChoice == 3:
    print("*" * 20)
    print("       Menu     ")
    print("*" * 20)
    print("  1)  Examine DNA ")
    print("  2)  Play Hangman ")
    print("  3)  Exit ")
    menuChoice = int(input("Enter your selection (1/2/3): "))


"""2) EXAMINE DNA"""

# 1) Welcome message to Examine DNA
while menuChoice == 1:
    print("Welcome to Examine DNA")

    # 2a) Ask user to provide the first DNA strand
    let1 = 0
    species1 = input("Please Enter first DNA containing('A', 'T', 'C', 'G'): ").upper()

    # (loop over no char in Species --> if char doesn't have A, T, C, G --> ask again or accept)
    while let1 < len(species1):
        if species1[let1] != "A" and species1[let1] != "T" and species1[let1] != "C" and species1[let1] != "G":
            species1 = input("Incorrect, please re-enter any of the following: A, T, C, G: ").upper()		
        else:
            let1 += 1

    # 2b) Ask user to provide the second DNA strand
    let2 = 0
    species2 = input("Now enter second DNA containing('A', 'T', 'C', 'G'): ").upper()

    while let2 < len(species2):
        if species2[let2] != "A" and species2[let2] != "T" and species2[let2] != "C" and species2[let2] != "G":
            species2 = input("Incorrect, please re-enter any of the following: A, T, C, G: ").upper()		
        else:
            let2 += 1

    # 3) Present menu for add/delete indel, score & quit
    print("*" * 30)
    print("            Menu            ")
    print("*" * 30)
    print("  A)  Add an Indel ")
    print("  D)  Delete an Indel ")
    print("  S)  Score Present Alignment ")
    print("  Q)  Quit ")

    # 4) Prompt and take user's selection
    menuDNA = input("Enter your selection ('A', 'D', 'S', 'Q'): ").upper()
    counter = 0

    # 5) Prompts for adding an indel
    while menuDNA == "A":
        dnaChoice = int(input("Select which species to add indel (1) or (2): "))
        indexPos = int(input("Select the index position you would like to change: "))

        if menuDNA == "A" and dnaChoice == 1:
            while indexPos > species1.index(species1[-1]):
                indexPos = int(input("Index position out of range, please select again: "))
            species1 = species1[:indexPos] + "-" + species1[indexPos] + species1[indexPos+1:]  
        if menuDNA == "A" and dnaChoice == 2:
            while indexPos > species2.index(species2[-1]):
                indexPos = int(input("Index position out of range, please select again: "))
            species2 = species2[:indexPos] + "-" + species2[indexPos] + species2[indexPos+1:]
        else:
            pass

    # 6) Prompts for deleting an indel
        print("*" * 30)
        print("            Menu            ")
        print("*" * 30)
        print("  A)  Add an Indel ")
        print("  D)  Delete an Indel ")
        print("  S)  Score Present Alignment ")
        print("  Q)  Quit ")

        menuDNA = input("Enter your selection ('A', 'D', 'S', 'Q'): ").upper()

        while menuDNA == "D":
            dnaChoice = int(input("Select which species to delete indel (1) or (2): "))
            indexPosD = int(input("Select the index position you would like to remove: "))

            if menuDNA == "D" and dnaChoice == 1:
                while species1[indexPosD] != "-":
                    indexPosD = int(input("Please re-select index position of an INDEL to delete: "))
                species1 = species1[:indexPosD] + "" + species1[indexPosD+1:]
            elif menuDNA == "D" and dnaChoice == 2:
                while species2[indexPosD] != "-":
                    indexPosD = int(input("Please re-select index position of an INDEL to delete: "))
                species2 = species2[:indexPosD] + "" + species2[indexPosD+1:]
            else:
                pass

    # 7) Prompts for scoring alignment
            print("*" * 30)
            print("            Menu            ")
            print("*" * 30)
            print("  A)  Add an Indel ")
            print("  D)  Delete an Indel ")
            print("  S)  Score Present Alignment ")
            print("  Q)  Quit ")

            menuDNA = input("Enter your selection ('A', 'D', 'S', 'Q'): ").upper()

            while menuDNA == "S" and counter == 0:
                print("You have selected to score the alignment")

                matches = 0
                mismatches = 0
                loopChoice = ""

                lenDiff = len(species1) - len(species2)
                if lenDiff > 0:
                    species2 = species2 + "-" * lenDiff
                    loopChoice = species1
                elif lenDiff < 0:
                    species1 = species1 + "-" * lenDiff
                    loopChoice = species2
                else:
                    pass

                # loop through longer string
                for i in range(len(loopChoice)):
                    
                    if species1[i] == species2[i] and species1[i] != "-" and species2[i] != "-" :
                        matches += 1
                        species1 = species1[:i].lower() + species1[i].upper() + species1[i+1:].lower()
                        species2 = species2[:i].lower() + species2[i].upper() + species2[i+1:].lower()
                    else:
                        mismatches += 1

                print(f"The number of matches were: {matches}")
                print(f"The number of mis-matches were: {mismatches}")
                print(f"Species 1 is: {species1}")
                print(f"Species 1 is: {species2}")
                counter += 1

                # QUIT GAME

                print("*" * 30)
                print("            Menu            ")
                print("*" * 30)
                print("  A)  Add an Indel ")
                print("  D)  Delete an Indel ")
                print("  S)  Score Present Alignment ")
                print("  Q)  Quit ")

                menuDNA = input("Enter your selection ('A', 'D', 'S', 'Q'): ").upper()

                # RETURN TO MENU
           
                print("You have selected to quit the game and will be returned to the initial menu!")
                print("*" * 20)
                print("       Menu     ")
                print("*" * 20)
                print("  1)  Examine DNA ")
                print("  2)  Play Hangman ")
                print("  3)  Exit ")

                menuChoice = int(input("Enter your selection (1) (2) or (3): "))

        
"""PLAY HANGMAN"""
# Menu Selection
while menuChoice == 2:
    print("Welcome to Hangman")

    # 1) Declared Variables
    import random
    lives = 9
    randomWords =  ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']

    # 2) Computer to select random word
    randomWord = random.choice(randomWords)

    # 3) Display Length Of Word to User
    # (loop over no. characters in word & append "_" for each character)
    blanks = []
    for i in range(len(randomWord)):
        blanks.append("_")
        
    # 4) While User has lives & word is not fully guessed
    while lives > 0 and "_" in blanks:
        print(f"You have {lives} lives to guess the following word: {blanks}")
        
        # 5) Take user's guess
        guess = input("Enter your guess (1 letter): ").lower()

        # 6) If guess is correct, retrieve the index pos.
        guessedLetters = []
        # a) Loop over no. char in randomWord
        for i in range(len(randomWord)):
        # b) if value at 0, 1, 2, etc. matches the guess --> 
            if randomWord[i] == guess:
        # add index position to guessedLetters
                guessedLetters += [i]

        # 7) If guess is incorrect in this iteration, reduce no. lives 
        if len(guessedLetters) == 0:
            lives -= 1
            print("You have lost 1 life")

        # 8) Fill in the guess at the correct place
        # (loop over guessedLetters, make blanks = blanks up to index + guess + everything else after)
        for i in guessedLetters:
            blanks = blanks[:i] + [guess] + blanks[i+1:]

        # 9) End of Game
        if lives == 0:
            print("You have ran out of lives. Game Lost!")
        elif lives > 0 and "_" not in blanks:
            print("Congratulations. Game Won!")
        else:
            pass

    # 10) Return to Menu (code from menu step at start of file)
    print("*" * 20)
    print("       Menu     ")
    print("*" * 20)
    print("  1)  Examine DNA ")
    print("  2)  Play Hangman ")
    print("  3)  Exit ")

    menuChoice = int(input("Enter your selection (1) (2) or (3): "))

    