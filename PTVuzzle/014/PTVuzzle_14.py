def main():
    puzzleQuestion(14)


def puzzleQuestion(puzzleNumber):
    print("===========================================================================================================")
    print("Welcome to PTVuzzle - ", puzzleNumber)
    print("===========================================================================================================")
    print("You are on a grid of integers NxN in the position (0,0) and you have to go to the position (N,N).\n"
          "Only steps toward North and East  directions are allowed. How many different paths you can build that live\n"
          "totally above the diagonal connecting (0,0) with (N,N)? Can you design an efficient (in time and space)\n"
          "algorithm to fully enumerate all those paths?")
    print("===========================================================================================================")


if __name__ == "__main__":
    main()
