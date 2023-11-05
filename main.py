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


def check_answer():
    
    i = 0
    correct_position = 0
    incorrect_position = 0

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
    
    results = {
        "correct position" : correct_position,
        "incorrect position" : incorrect_position
    }

    return results


generate_color_code()

print(secret_code)

print(f"""
Welcome to Mastermind. Try to guess the 4-color secret code 
generated from these colors: {available_colors}
You will have 10 tries to guess it. Good luck!
""")

game_on = True
current_turn = 1

while game_on:

    copy_secret = copy.deepcopy(secret_code)
    to_remove = []

    guess = input(f"#{current_turn}. Guess a code: ")
    
    guessed_letters = guess.split(" ")

    if not guess_is_valid(guessed_letters):
        continue
    
    results = check_answer()
        
    print(f"Correct: {results['correct position']} || Incorrect: {results['incorrect position']}")
    
    if results['correct position'] == 4:
        print(f"You win! You guessed it in {current_turn} tries.")
        game_on = False
        break

    current_turn += 1

    if current_turn > 10:
        print(f"Sorry, you lose. The secret code was: {secret_code}")
        game_on = False

