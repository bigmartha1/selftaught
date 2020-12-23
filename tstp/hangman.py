def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
    
        if char in rletters:
            word_index = rletters.index(char)
            board[word_index] = char
            rletters[word_index] = '$'
        
        else:
            wrong += 1
            
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
    
        if "__" not in board:
            print("You win! It was: ")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

hangman("cat")
