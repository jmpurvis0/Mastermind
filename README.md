# Mastermind
 
A Python-programmed version of the game Mastermind. Players attempt to guess a secret code randomly generated using any combination of these 6 colors: red, green, blue, yellow, orange, and white. After each guess, the game will tell the player how many letters are in the correct and incorrect position. Players have up to 10 attempts to guess the code.

# Notes

The most challenging part of this project by far was figuring out what to do when a guessed letter was in the incorrect position. I tried several (unsuccessful) approaches: comparing the number of correct and incorrect positions, comparing how many of a letter was in the guess vs. in the secret code.

The key was when I stepped back and realized that I had been checking for correct and incorrect positions simultaneously (by stacking if/elif/else statements), when I could have been trying to do these two tasks separately. This led me to try finding the number of matches (correct position) first, creating a list of those matches, then using that list to remove letters from the guess and a copy of the secret code. Now that matches have been accounted for, I could then just check to see if each guessed letter was in the secret code.
