# réaliser un pendu


word = "python"
wordln = len(word)
chances = 9

WordListe = list(word)
print(chances, "chances ")

hiddenWord = "*"*len(word)

hiddenWordList = list(hiddenWord)

hiddenWordstr = "-".join(hiddenWordList)
print("le nombre de lettre à découvrir est de  :"+ str(wordln))

print(hiddenWord)

print("bonne chance")


while chances != 0 and hiddenWordList != WordListe:
    letter = input("Veuillez entrer une lettre :" )
    if letter in word:
        print("bien joué")
        isHere = word.index(letter)
        hiddenWordList[isHere] = letter
        print(hiddenWordList)
    
    else:
        print("réessaye")
        print("il vous reste ", chances, "chances")
        chances = chances - 1
        if chances == 0:
            print("vous n'avez plus de chances")
            break

    
            
               

        






