import os
import sys

def main():
    os.chdir(os.path.dirname(sys.argv[0]))
    if mode == False:
        print(number("22"))
    if mode == True:
        print()
    
def raiseError(error):
    print("\033[91m    {}\033[00m".format(error))
    sys.exit()

# Define command line arguments.

try:
    if sys.argv[1] == "false" or sys.argv[1] == "False": 
        mode = False
    else: 
        mode = True
except:
    raiseError("Error: Oops! Looks like you didn't supply a mode for us. Could you re-enter the command? If that doesn't help, look on the CatCode Wiki! ()")

try:
    code = str(sys.argv[2])
except:
    raiseError("Error: Oops! Looks like you didn't supply a path to your code for us. Could you re-enter the command? If that doesn't help, look on the CatCode Wiki! ()")

try:
    catec = int(sys.argv[3])
except:
    print("\033[93m    {}\033[00m".format("Warning: Catec is undefined. Default to 0."))

def number(input):
    output = 0

    length = len(input) # Wait, so let me get this straight; passing range() len(input) leads to only one iteration, but feeding it a variable equivelant to len(input) works? *internal development screaming*
    # print(str(length))

    # print(str(range(len(input))))
    # for n in range(len(input)):
    #     print(n)
    # print("123457890"[5])
    for i in range(0, length):
        if input[i] == "1":
            output += 1
        elif input[i]  ==  "2":
          output += 2
        elif input[i]  ==  "3":
          output -= 3
        elif input[i]  ==  "4":
          output -= 4
        elif input[i]  ==  "5":
          output += 5
        elif input[i]  ==  "6":
          output += 6
        elif input[i]  ==  "7":
          output -= 7
        elif input[i]  ==  "8":
          output -= 8
        elif input[i]  ==  "9":
          output -= 9
        elif input[i]  ==  "0":
          if str(output).startswith("-"):
              output = int(str(output[1:]))
          else:
              output = int("-" + str(output))
        elif input[i]  ==  "q":
          output *= 10
        elif input[i]  ==  "w":
          output *= 100
        elif input[i]  ==  "e":
          output *= 1000
        elif input[i]  ==  "r":
          output -= 2
        elif input[i]  ==  "t":
          output -= 2
        elif input[i]  ==  "y":
          output -= 2
        elif input[i]  ==  "u":
          if not input[i] == 0:
              output /= 10
        elif input[i]  ==  "i":
          if not input[i] == 0:
              output /= 100
        elif input[i]  ==  "o":
          if not input[i] == 0:
              output /= 1000
        elif input[i]  ==  "p":
          output -= 100
        elif input[i]  ==  "a":
          output *= 3
        elif input[i]  ==  "s":
          output *= 2
        elif input[i]  ==  "d":
          output += 3
        elif input[i]  ==  "f":
          output += 2
        elif input[i]  ==  "g":
          output += 1
        elif input[i]  ==  "h":
          output -= 1
        elif input[i]  ==  "j":
          output -= 2
        elif input[i]  ==  "k":
          output -= 3
        elif input[i]  ==  "l":
          if not input[i] == 0:
              output /= 2
        elif input[i]  ==  "z":
          output *= 4
        elif input[i]  ==  "x":
          if not input[i] == 0:
              output /= 4
        elif input[i]  ==  "c":
          output += 2
        elif input[i]  ==  "v":
          output += 2
        elif input[i]  ==  "b":
          output += 2
        elif input[i]  ==  "n":
          output += 2
        elif input[i]  ==  "m":
          if not input[i] == 0:
              output /= 3
        # print(str(output))
        # print(str(i))
    return(str(output))

def turtle(input):
    for i in len(input):
        if input[i] == "1":
            print()
        elif input[i]  ==  "2":
            print()
        elif input[i]  ==  "3":
            print()
        elif input[i]  ==  "4":
            print()
        elif input[i]  ==  "5":
            print()
        elif input[i]  ==  "6":
            print()
        elif input[i]  ==  "7":
            print()
        elif input[i]  ==  "8":
            print()
        elif input[i]  ==  "9":
            print()
        elif input[i]  ==  "0":
            print()
        elif input[i]  ==  "q":
            print()
        elif input[i]  ==  "w":
            print()
        elif input[i]  ==  "e":
            print()
        elif input[i]  ==  "r":
            print()
        elif input[i]  ==  "t":
            print()
        elif input[i]  ==  "y":
            print()
        elif input[i]  ==  "u":
            print()
        elif input[i]  ==  "i":
            print()
        elif input[i]  ==  "o":
            print()
        elif input[i]  ==  "p":
            print()
        elif input[i]  ==  "a":
            print()
        elif input[i]  ==  "s":
            print()
        elif input[i]  ==  "d":
            print()
        elif input[i]  ==  "f":
            print()
        elif input[i]  ==  "g":
            print()
        elif input[i]  ==  "h":
            print()
        elif input[i]  ==  "j":
            print()
        elif input[i]  ==  "k":
            print()
        elif input[i]  ==  "l":
            print()
        elif input[i]  ==  "z":
            print()
        elif input[i]  ==  "x":
            print()
        elif input[i]  ==  "c":
            print()
        elif input[i]  ==  "v":
            print()
        elif input[i]  ==  "b":
            print()
        elif input[i]  ==  "n":
            print()
        elif input[i]  ==  "m":
            print()

def game(input):
    for i in len(input):
        if input[i] == "1":
            print()
        elif input[i]  ==  "2":
            print()
        elif input[i]  ==  "3":
            print()
        elif input[i]  ==  "4":
            print()
        elif input[i]  ==  "5":
            print()
        elif input[i]  ==  "6":
            print()
        elif input[i]  ==  "7":
            print()
        elif input[i]  ==  "8":
            print()
        elif input[i]  ==  "9":
            print()
        elif input[i]  ==  "0":
            print()
        elif input[i]  ==  "q":
            print()
        elif input[i]  ==  "w":
            print()
        elif input[i]  ==  "e":
            print()
        elif input[i]  ==  "r":
            print()
        elif input[i]  ==  "t":
            print()
        elif input[i]  ==  "y":
            print()
        elif input[i]  ==  "u":
            print()
        elif input[i]  ==  "i":
            print()
        elif input[i]  ==  "o":
            print()
        elif input[i]  ==  "p":
            print()
        elif input[i]  ==  "a":
            print()
        elif input[i]  ==  "s":
            print()
        elif input[i]  ==  "d":
            print()
        elif input[i]  ==  "f":
            print()
        elif input[i]  ==  "g":
            print()
        elif input[i]  ==  "h":
            print()
        elif input[i]  ==  "j":
            print()
        elif input[i]  ==  "k":
            print()
        elif input[i]  ==  "l":
            print()
        elif input[i]  ==  "z":
            print()
        elif input[i]  ==  "x":
            print()
        elif input[i]  ==  "c":
            print()
        elif input[i]  ==  "v":
            print()
        elif input[i]  ==  "b":
            print()
        elif input[i]  ==  "n":
            print()
        elif input[i]  ==  "m":
            print()

def colour(input):
    for i in len(input):
        if input[i] == "1":
            print()
        elif input[i]  ==  "2":
            print()
        elif input[i]  ==  "3":
            print()
        elif input[i]  ==  "4":
            print()
        elif input[i]  ==  "5":
            print()
        elif input[i]  ==  "6":
            print()
        elif input[i]  ==  "7":
            print()
        elif input[i]  ==  "8":
            print()
        elif input[i]  ==  "9":
            print()
        elif input[i]  ==  "0":
            print()
        elif input[i]  ==  "q":
            print()
        elif input[i]  ==  "w":
            print()
        elif input[i]  ==  "e":
            print()
        elif input[i]  ==  "r":
            print()
        elif input[i]  ==  "t":
            print()
        elif input[i]  ==  "y":
            print()
        elif input[i]  ==  "u":
            print()
        elif input[i]  ==  "i":
            print()
        elif input[i]  ==  "o":
            print()
        elif input[i]  ==  "p":
            print()
        elif input[i]  ==  "a":
            print()
        elif input[i]  ==  "s":
            print()
        elif input[i]  ==  "d":
            print()
        elif input[i]  ==  "f":
            print()
        elif input[i]  ==  "g":
            print()
        elif input[i]  ==  "h":
            print()
        elif input[i]  ==  "j":
            print()
        elif input[i]  ==  "k":
            print()
        elif input[i]  ==  "l":
            print()
        elif input[i]  ==  "z":
            print()
        elif input[i]  ==  "x":
            print()
        elif input[i]  ==  "c":
            print()
        elif input[i]  ==  "v":
            print()
        elif input[i]  ==  "b":
            print()
        elif input[i]  ==  "n":
            print()
        elif input[i]  ==  "m":
            print()

main()