#Dictionay Method

WORDS = {"tone": 4,
        "torn": 4,
         "note": 4,
         "later": 5,
         "alert": 5,
         "talon": 5 
         }
words_left = WORDS.copy()

def main():
    print(f"""========WELCOME TO THE NATIONAL SPELLING BEE!==========""")
    print("Your letters are: R T O N A E L ")

    while len(WORDS) > 0:
        print(f"{len(WORDS) } words left!")
        guess = input("Guess a word:").lower()

        

        if guess in WORDS.keys():
               points = WORDS.pop(guess)
               print(f"Good job! You scored {points } points")
               del words_left[guess]

        
        if guess == "rental":
             WORDS.clear
             print  (F"🎉 You found the 7-letter word 'rental' → YOU WIN!")
             break
        else:
             print(f"Wrong guess, please try again")
             


    print("Thats the game")
main()


  



