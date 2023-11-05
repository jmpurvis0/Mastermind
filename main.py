import random, copy


def generate_color_code():
    global available_colors, secret_code
    available_colors = ['R', 'G', 'B', 'Y', 'O', 'W']
    rand_indxs = [random.randrange(0, 6) for num in range(0, 4)]
    secret_code = [available_colors[index] for index in rand_indxs]


def guess_is_valid(guessed_letters):
    """Checks if guess uses 4 letters from the available colors. Returns True or False."""
    if len(guessed_letters) != 4:
        print("You entered an invalid code. Please enter a 4-character code")
        return False
    
    for letter in guessed_letters:
        if letter not in available_colors:
            print(f"You did not choose from the available colors {available_colors}. Please try again")
            return False
        else:
            return True





generate_color_code()

#print(secret_code)

print(f"""
Welcome to Mastermind. Try to guess the 4-color secret code 
generated from these colors: {available_colors}
You will have 10 tries to guess it. Good luck!
""")


game_on = True
current_turn = 1

while game_on:

    correct_position = 0
    incorrect_position = 0
    copy_secret = copy.deepcopy(secret_code)
    to_remove = []

    guess = input(f"#{current_turn}. Guess a code: ")
    
    guessed_letters = guess.split(" ")

    if not guess_is_valid(guessed_letters):
        continue
    
    i = 0

    for letter in guessed_letters:
        #print(f"Does {letter} match with {copy_secret[i]}?")
        if letter == copy_secret[i]:
            #print("yes it matches!")
            correct_position += 1
            to_remove.append(letter)
        i += 1

    for letter in to_remove:
        guessed_letters.remove(letter)
        copy_secret.remove(letter)
   

    for letter in guessed_letters:
        if letter in copy_secret:
            incorrect_position += 1
            copy_secret.remove(letter)
        

    print(f"Correct: {correct_position} || Incorrect: {incorrect_position}")
    
    if correct_position == 4:
        print(f"You win! You guessed it in {current_turn} tries.")
        game_on = False
        break

    current_turn += 1

    if current_turn > 10:
        print(f"Sorry, you lose. The secret code was: {secret_code}")
        game_on = False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~








# for letter in guessed_letters:
    #     if letter == color_code[i]:
    #         correct_position += 1
    #         matched.append(letter)
    #     i += 1

    # for matched_letter in matched:
    #     color_code.remove(matched_letter)
    #     guessed_letters.remove(matched_letter)
    
    # for guess in guessed_letters:
    #     if guess in color_code:
    #         incorrect_position += 1
    #         color_code.remove(guess)


            # available_spots.remove(letter)
            

                # if guessed_letters.count(letter) > color_code.count(letter):
                #     if color_code.count(letter) == 1:
                #         incorrect_position -= 2
                #     else:
                #         incorrect_position -= 1
            # else:
            #     not_in += 1

    

