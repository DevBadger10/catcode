import os
import sys
import PyInstaller.__main__

import turtle as turt

def main():
    os.chdir(os.path.dirname(sys.argv[0]))

    try:
        cmplbase = """

def main():
    if catec == 0:
        print(number(code, True))
        while True: pass
    elif catec == 1:
        turtle(code)
    elif catec == 2:
        game(code)

def raiseError(error):
    print("\033[91m    {}\033[00m".format(error))
    sys.exit()

def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n

def number(input, prnt):
    output = 0
    length = len(input)

    for i in range(0, length):
        if prnt: print(str(output))
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
              output = float(str(output[1:]))
          else:
              output = float("-" + str(output))
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
        # print(str(i))
    if prnt: print(str(output))
    if prnt: return("\\n\\rFinal number: " + str(output))
    else: return(output)

def turtle(input):
    output = turt.Turtle()
    output.penup()
    lenput = len(input)
    output.hideturtle()
    output.pensize(15)
    output.speed(3)
    turt.colormode(255)
    output.pendown()

    try:
        while True:
            for i in range(lenput):
                if input[i] == "1":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("Cheese.")
                elif input[i]  ==  "2":
                    output.up()
                elif input[i]  ==  "3":
                    output.down()
                elif input[i]  ==  "4":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "5":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("Cheese.")
                elif input[i]  ==  "6":
                    output.down()
                elif input[i]  ==  "7":
                    output.down()
                elif input[i]  ==  "8":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "9":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("    Cheese.")
                elif input[i]  ==  "0":
                    output.down()
                elif input[i]  ==  "q":
                    output.down()
                elif input[i]  ==  "w":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "e":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("    Cheese.")
                elif input[i]  ==  "r":
                    output.down()
                elif input[i]  ==  "t":
                    output.down()
                elif input[i]  ==  "y":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "u":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("Cheese.")
                elif input[i]  ==  "i":
                    output.down()
                elif input[i]  ==  "o":
                    output.down()
                elif input[i]  ==  "p":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "a":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("    Cheese.")
                elif input[i]  ==  "s":
                    output.down()
                elif input[i]  ==  "d":
                    output.down()
                elif input[i]  ==  "f":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "g":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("Cheese.")
                elif input[i]  ==  "h":
                    output.down()
                elif input[i]  ==  "j":
                    output.down()
                elif input[i]  ==  "k":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "l":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("Cheese.")
                elif input[i]  ==  "z":
                    output.down()
                elif input[i]  ==  "x":
                    output.down()
                elif input[i]  ==  "c":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "v":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("    Cheese.")
                elif input[i]  ==  "b":
                    output.down()
                elif input[i]  ==  "n":
                    output.up()
                elif input[i]  ==  "m":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
    except:
        raiseError("Shredded Cheese.")

def game(input):
    gtype = False
    gspeed = 5
    gcol1 = colour("gg", False)
    gcol2 = colour("gh", False)
    gcol3 = colour("hg", False)
    gcol4 = colour("hh", False)
    gcol5 = colour("yg", False)

    i = 0
    if input[i]  ==  "2":
        gtype = True
    elif input[i]  ==  "4":
        gtype = True
    elif input[i]  ==  "6":
        gtype = True
    elif input[i]  ==  "8":
        gtype = True
    elif input[i]  ==  "0":
        gtype = True
    elif input[i]  ==  "w":
        gtype = True
    elif input[i]  ==  "r":
        gtype = True
    elif input[i]  ==  "y":
        gtype = True
    elif input[i]  ==  "i":
        gtype = True
    elif input[i]  ==  "p":
        gtype = True
    elif input[i]  ==  "s":
        gtype = True
    elif input[i]  ==  "f":
        gtype = True
    elif input[i]  ==  "h":
        gtype = True
    elif input[i]  ==  "k":
        gtype = True
    elif input[i]  ==  "z":
        gtype = True
    elif input[i]  ==  "c":
        gtype = True
    elif input[i]  ==  "b":
        gtype = True
    elif input[i]  ==  "m":
        gtype = True

    i = 1

    if input[i] == "1":
        gspeed = 50
    elif input[i]  ==  "2":
        gspeed = 40
    elif input[i]  ==  "3":
        gspeed = 30
    elif input[i]  ==  "4":
        gspeed = 15
    elif input[i]  ==  "5":
        gspeed = 15
    elif input[i]  ==  "6":
        gspeed = 15
    elif input[i]  ==  "7":
        gspeed = 15
    elif input[i]  ==  "8":
        gspeed = 30
    elif input[i]  ==  "9":
        gspeed = 40
    elif input[i]  ==  "0":
        gspeed = 50
    elif input[i]  ==  "q":
        gspeed = 10
    elif input[i]  ==  "w":
        gspeed = 10
    elif input[i]  ==  "e":
        gspeed = 10
    elif input[i]  ==  "r":
        gspeed = 5
    elif input[i]  ==  "t":
        gspeed = 5
    elif input[i]  ==  "y":
        gspeed = 5
    elif input[i]  ==  "u":
        gspeed = 10
    elif input[i]  ==  "i":
        gspeed = 10
    elif input[i]  ==  "o":
        gspeed = 10
    elif input[i]  ==  "p":
        gspeed = 10
    elif input[i]  ==  "a":
        gspeed = 10
    elif input[i]  ==  "s":
        gspeed = 10
    elif input[i]  ==  "d":
        gspeed = 5
    elif input[i]  ==  "f":
        gspeed = 5
    elif input[i]  ==  "g":
        gspeed = 5
    elif input[i]  ==  "h":
        gspeed = 5
    elif input[i]  ==  "j":
        gspeed = 5
    elif input[i]  ==  "k":
        gspeed = 10
    elif input[i]  ==  "l":
        gspeed = 10
    elif input[i]  ==  "z":
        gspeed = 100
    elif input[i]  ==  "x":
        gspeed = 10
    elif input[i]  ==  "c":
        gspeed = 5
    elif input[i]  ==  "v":
        gspeed = 5
    elif input[i]  ==  "b":
        gspeed = 5
    elif input[i]  ==  "n":
        gspeed = 5
    elif input[i]  ==  "m":
        gspeed = 100

    if input[2] and input[3]:
        gcol1 = colour(input[2] + input[3], False)
    
    if input[4] and input[5]:
        gcol2 = colour(input[4] + input[5], False)
    
    if input[6] and input[7]:
        gcol3 = colour(input[6] + input[7], False)
    
    if input[8] and input[9]:
        gcol4 = colour(input[8] + input[9], False)
    
    if input[10] and input[11]:
        gcol5 = colour(input[10] + input[11], False)

    if gtype == False:
        execPong(gspeed, gcol1, gcol2)
    if gtype == True:
        execSnake(gspeed, gcol1, gcol2, gcol3, gcol4, gcol5)

def execPong(speed, col1, col2):
    toExec = \"\"\"
# Import the pygame library and initialise the game engine
import pygame
from random import * # This is created by https://www.101computing.net/pong-tutorial-using-pygame-adding-a-scoring-system/ I simply brought it into one file and made the speed customizeable. 
from random import randint
import random
speed = \"\"\" + str(speed) + \"\"\"
pygame.init()
class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    def __init__(self, color, width, height):
        import pygame
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass in the color of the Paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color(\"\"\" + str(col1[0]) + \"\"\",\"\"\" + str(col1[1]) + \"\"\",\"\"\" + str(col1[2]) + \"\"\"))
        self.image.set_colorkey(pygame.Color(\"\"\" + str(col1[0]) + \"\"\",\"\"\" + str(col1[1]) + \"\"\",\"\"\" + str(col1[2]) + \"\"\"))
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
    def moveUp(self, pixels):
        self.rect.y -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y < 0:
          self.rect.y = 0
    def moveDown(self, pixels):
        self.rect.y += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y > 400:
          self.rect.y = 400
class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    def __init__(self, color, width, height):
        import pygame
        from random import randint
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color(\"\"\" + str(col1[0]) + \"\"\",\"\"\" + str(col1[1]) + \"\"\",\"\"\" + str(col1[2]) + \"\"\"))
        self.image.set_colorkey(pygame.Color(\"\"\" + str(col1[0]) + \"\"\",\"\"\" + str(col1[1]) + \"\"\",\"\"\" + str(col1[2]) + \"\"\"))
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4,8),randint(-8,8)]
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
    def update(self):
        from random import randint
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    def bounce(self):
        from random import randint
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
pygame.init()
# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
paddleA = Paddle(pygame.Color(\"\"\" + str(col2[0]) + \"\"\",\"\"\" + str(col2[1]) + \"\"\",\"\"\" + str(col2[2]) + \"\"\"), 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
paddleB = Paddle(pygame.Color(\"\"\" + str(col2[0]) + \"\"\",\"\"\" + str(col2[1]) + \"\"\",\"\"\" + str(col2[2]) + \"\"\"), 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200
ball = Ball(pygame.Color(\"\"\" + str(col2[0]) + \"\"\",\"\"\" + str(col2[1]) + \"\"\",\"\"\" + str(col2[2]) + \"\"\"),10,10)
ball.rect.x = 345
ball.rect.y = 195
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
# Add the 2 paddles and the ball to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
#Initialise player scores
scoreA = 0
scoreB = 0
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False
    #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(speed)
    if keys[pygame.K_s]:
        paddleA.moveDown(speed)
    if keys[pygame.K_UP]:
        paddleB.moveUp(speed)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(speed)    
    # --- Game logic should go here
    all_sprites_list.update()
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=690:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]     
    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()
    # --- Drawing code should go here
    # First, clear the screen to black. 
    screen.fill(pygame.Color(\"\"\" + str(col1[0]) + \"\"\",\"\"\" + str(col1[1]) + \"\"\",\"\"\" + str(col1[2]) + \"\"\"))
    #Draw the net
    pygame.draw.line(screen, pygame.Color(\"\"\" + str(col2[0]) + \"\"\",\"\"\" + str(col2[1]) + \"\"\",\"\"\" + str(col2[2]) + \"\"\"), [349, 0], [349, 500], 5)
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen) 
    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, pygame.Color(\"\"\" + str(col2[0]) + \"\"\",\"\"\" + str(col2[1]) + \"\"\",\"\"\" + str(col2[2]) + \"\"\"))
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, pygame.Color(\"\"\" + str(col2[0]) + \"\"\",\"\"\" + str(col2[1]) + \"\"\",\"\"\" + str(col2[2]) + \"\"\"))
    screen.blit(text, (420,10))
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()\"\"\"

    # print(toExec)
    print("Game starting...")
    exec(toExec)

def execSnake(speed, col1, col2, col3, col4, col5):
    toExec = \"\"\"
# importing libraries
import pygame
import time
import random
 
snake_speed = \"\"\" + str(speed) + \"\"\"
 
# Window size
window_x = 720 # Originally made by https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
window_y = 480
 
# defining colors
black = pygame.Color(\"\"\" + str(col1[0]) + \"\"\",\"\"\" + str(col1[1]) + \"\"\",\"\"\" + str(col1[2]) + \"\"\")
white = pygame.Color(\"\"\" + str(col2[0]) + \"\"\",\"\"\" + str(col2[1]) + \"\"\",\"\"\" + str(col2[2]) + \"\"\")
red = pygame.Color(\"\"\" + str(col3[0]) + \"\"\",\"\"\" + str(col3[1]) + \"\"\",\"\"\" + str(col3[2]) + \"\"\")
green = pygame.Color(\"\"\" + str(col4[0]) + \"\"\",\"\"\" + str(col4[1]) + \"\"\",\"\"\" + str(col4[2]) + \"\"\")
blue = pygame.Color(\"\"\" + str(col5[0]) + \"\"\",\"\"\" + str(col5[1]) + \"\"\",\"\"\" + str(col5[2]) + \"\"\")
 
# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
 
# initial score
score = 0
 
# displaying Score function
def show_score(choice, color, font, size, score, game_window):
    import pygame
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)
 
# game over function
def game_over(score, game_window):
    import pygame
    import pygame
    import time
    import random
    black = pygame.Color(\"\"\" + str(col1[0]) + \"\"\",\"\"\" + str(col1[1]) + \"\"\",\"\"\" + str(col1[2]) + \"\"\")
    white = pygame.Color(\"\"\" + str(col2[0]) + \"\"\",\"\"\" + str(col2[1]) + \"\"\",\"\"\" + str(col2[2]) + \"\"\")
    red = pygame.Color(\"\"\" + str(col3[0]) + \"\"\",\"\"\" + str(col3[1]) + \"\"\",\"\"\" + str(col3[2]) + \"\"\")
    green = pygame.Color(\"\"\" + str(col4[0]) + \"\"\",\"\"\" + str(col4[1]) + \"\"\",\"\"\" + str(col4[2]) + \"\"\")
    blue = pygame.Color(\"\"\" + str(col5[0]) + \"\"\",\"\"\" + str(col5[1]) + \"\"\",\"\"\" + str(col5[2]) + \"\"\")
    window_x = 720 # Originally made by https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
    window_y = 480
   
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, blue)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
 
 
# Main Function
while True:
    import pygame
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over(score, game_window)
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over(score, game_window)
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over(score, game_window)
 
    # displaying score countinuously
    show_score(1, white, 'times new roman', 20, score, game_window)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
    \"\"\"
    # print(toExec)
    print("Game starting...")
    exec(toExec)
    return(True)

def colour(input, prnt, type=False):
    output = s_colour(input[0])
    length = len(input)
    for i in range(0, length - 1):
        if prnt: print("RGB value: " + str(output[0]) + ", " + str(output[1]) + ", " + str(output[2]))
        if input[i + 1] == "1":
            output = l_colour(output, [10, 0, 0])
        elif input[i+ 1]  ==  "2":
            output = l_colour(output, [0, 20, 0])
        elif input[i + 1]  ==  "3":
            output = l_colour(output, [0, 0, 30])
        elif input[i + 1]  ==  "4":
            output = l_colour(output, [40, 0, 0])
        elif input[i + 1]  ==  "5":
            output = l_colour(output, [0, 50, 0])
        elif input[i + 1]  ==  "6":
            output = l_colour(output, [60, 0, 0])
        elif input[i + 1]  ==  "7":
            output = l_colour(output, [0, 70, 0])
        elif input[i + 1]  ==  "8":
            output = l_colour(output, [0, 0, 80])
        elif input[i + 1]  ==  "9":
            output = l_colour(output, [90, 0, 0])
        elif input[i + 1]  ==  "0":
            output = l_colour(output, [47, 156, 8])
        elif input[i + 1]  ==  "q":
            output = l_colour(output, [123, 123, 123])
        elif input[i + 1]  ==  "w":
            output = l_colour(output, [255, 128, 0])
        elif input[i + 1]  ==  "e":
            output = l_colour(output, [0, 128, 255])
        elif input[i + 1]  ==  "r":
            output = l_colour(output, [255, 0, 0])
        elif input[i + 1]  ==  "t":
            output = l_colour(output, [0, 255, 0])
        elif input[i + 1]  ==  "y":
            output = l_colour(output, [0, 0, 255])
        elif input[i + 1]  ==  "u":
            output = l_colour(output, [2, 184, 127])
        elif input[i + 1]  ==  "i":
            output = l_colour(output, [127, 255, 11])
        elif input[i + 1]  ==  "o":
            output = l_colour(output, [195, 125, 91])
        elif input[i + 1]  ==  "p":
            output = l_colour(output, [17, 218, 123])
        elif input[i + 1]  ==  "a":
            output = l_colour(output, [127, 118, 12])
        elif input[i + 1]  ==  "s":
            output = l_colour(output, [153, 173, 134])
        elif input[i + 1]  ==  "d":
            output = l_colour(output, [255, 255, 255])
        elif input[i + 1]  ==  "f":
            output = l_colour(output, [130, 165, 216])
        elif input[i + 1]  ==  "g":
            output = l_colour(output, [55, 55, 55])
        elif input[i + 1]  ==  "h":
            output = l_colour(output, [255, 165, 164])
        elif input[i + 1]  ==  "j":
            output = l_colour(output, [0, 0, 0])
        elif input[i + 1]  ==  "k":
            output = l_colour(output, [0, 255, 3])
        elif input[i + 1]  ==  "l":
            output = l_colour(output, [155, 246, 19])
        elif input[i + 1]  ==  "z":
            output = l_colour(output, [135, 212, 181])
        elif input[i + 1]  ==  "x":
            output = l_colour(output, [255, 0, 128])
        elif input[i + 1]  ==  "c":
            output = l_colour(output, [128, 0, 255])
        elif input[i + 1]  ==  "v":
            output = l_colour(output, [0, 0, 255])
        elif input[i + 1]  ==  "b":
            output = l_colour(output, [0, 255, 0])
        elif input[i + 1]  ==  "n":
            output = l_colour(output, [255, 0, 0])
        elif input[i + 1]  ==  "m":
            output = l_colour(output, [255, 78, 113]) 
    if prnt: print("RGB value: " + str(output[0]) + ", " + str(output[1]) + ", " + str(output[2]))
    if prnt: return("\\n\\rFinal Answer (RGB Value): " + str(output[0]) + ", " + str(output[1]) + ", " + str(output[2]))
    elif not prnt: 
        if not type: return(output)
        if type: return(tuple(output))

def l_colour(initial, goal): # Lerp Colour
    work0 = initial[0] + goal [0]
    ret0 = round(work0 / 2)
    # print(ret0)

    work1 = initial[1] + goal [1]
    ret1 = round(work1 / 2)

    work2 = initial[2] + goal[2]
    ret2 = round(work2 / 2)

    return([ret0, ret1, ret2])
    
def s_colour(input): # Solve Colour
    if input == "1":
        return([10, 0, 0])
    elif input ==  "2":
        return([0, 20, 0])
    elif input  ==  "3":
        return([0, 0, 30])
    elif input  ==  "4":
        return([40, 0, 0])
    elif input  ==  "5":
        return([0, 50, 0])
    elif input  ==  "6":
        return([60, 0, 0])
    elif input  ==  "7":
        return([0, 70, 0])
    elif input  ==  "8":
        return([0, 0, 80])
    elif input  ==  "9":
        return([90, 0, 0])
    elif input  ==  "0":
        return([47, 156, 8])
    elif input  ==  "q":
        return([123, 123, 123])
    elif input  ==  "w":
        return([255, 128, 0])
    elif input  ==  "e":
        return([0, 128, 255])
    elif input  ==  "r":
        return([255, 0, 0])
    elif input  ==  "t":
        return([0, 255, 0])
    elif input  ==  "y":
        return([0, 0, 255])
    elif input  ==  "u":
        return([2, 184, 127])
    elif input  ==  "i":
        return([127, 255, 11])
    elif input  ==  "o":
        return([195, 125, 91])
    elif input  ==  "p":
        return([17, 218, 123])
    elif input  ==  "a":
        return([127, 118, 12])
    elif input  ==  "s":
        return([153, 173, 134])
    elif input  ==  "d":
        return([255, 255, 255])
    elif input  ==  "f":
        return([130, 165, 216])
    elif input  ==  "g":
        return([55, 55, 55])
    elif input  ==  "h":
        return([255, 165, 164])
    elif input  ==  "j":
        return([0, 0, 0])
    elif input  ==  "k":
        return([0, 255, 3])
    elif input  ==  "l":
        return([155, 246, 19])
    elif input  ==  "z":
        return([135, 212, 181])
    elif input  ==  "x":
        return([255, 0, 128])
    elif input  ==  "c":
        return([128, 0, 255])
    elif input  ==  "v":
        return([0, 0, 255])
    elif input  ==  "b":
        return([0, 255, 0])
    elif input  ==  "n":
        return([255, 0, 0])
    elif input  ==  "m":
        return([255, 78, 113])
    else:
        return([55, 55, 55])

main()
        """
    except:
        pass

    # Define command line arguments.

    try:
        if sys.argv[1] == "false" or sys.argv[1] == "False": 
            mode = False
        else: 
            mode = True
    except:
        raiseError("Error: Oops! Looks like you didn't supply a mode for us. Could you re-enter the command? If that doesn't help, look on the CatCode Wiki! (https://github.com/DevBadger10/catcode/wiki)")

    try:
        code = str(sys.argv[2])
    except:
        raiseError("Error: Oops! Looks like you didn't supply a path to your code for us. Could you re-enter the command? If that doesn't help, look on the CatCode Wiki! (https://github.com/DevBadger10/catcode/wiki)")

    try:
        catec = int(sys.argv[3])
    except:
        print("\033[93m    {}\033[00m".format("Warning: Catec is undefined. Default to 0."))

    try:
        if not code.endswith(".cc"): raiseError("Error: Oops! Seems you put the wrong extension in there. Could you try changing it to .cc?")
        
        file = open(code, "r")
        code = file.read()
        file.close()
    except:
        # print("\033[93m    {}\033[00m".format("Warning: Read code failed, but bypass was active."))
        raiseError("Error: We either couldn't find or didn't have access to your code. Could you make sure you wrote the path correctly? If that doesn't help, look on the CatCode Wiki! (https://github.com/DevBadger10/catcode/wiki)")

    if mode == False:
        if catec == 0:
            print(number(code, True))
        elif catec == 1:
            turtle(code)
        elif catec == 2:
            game(code)  
        elif catec == 3:
            print(colour(code, True)) 
        else:
            raiseError("Error: Catec is undefined.")
    if mode == True:
        toexport = "import os\n\rimport sys\n\rimport turtle as turt\n\rimport pygame\n\rcode = \"" + code + "\"\n\rcatec = " + str(catec) + "\n\r" + cmplbase + "# END"
        export = open("./TMP", "w")
        export.writelines(toexport)
        export.close()
        if catec == 0:
            PyInstaller.__main__.run([
                'TMP',
                '--onefile',
                '--windowed',
                '-n CatCode Executable',
                '-c'
            ])
        else: 
            PyInstaller.__main__.run([
                'TMP',
                '--onefile',
                '--windowed',
                '-n CatCode Executable'
            ])
    
def raiseError(error):
    print("\033[91m    {}\033[00m".format(error))
    sys.exit()

def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n

def number(input, prnt):
    output = 0
    length = len(input)

    for i in range(0, length):
        if prnt: print(str(output))
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
              output = float(str(output[1:]))
          else:
              output = float("-" + str(output))
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
        # print(str(i))
    if prnt: print(str(output))
    if prnt: return("\n\rFinal number: " + str(output))
    else: return(output)

def turtle(input):
    output = turt.Turtle()
    output.penup()
    lenput = len(input)
    output.hideturtle()
    output.pensize(15)
    output.speed(3)
    turt.colormode(255)
    output.pendown()

    try:
        while True:
            for i in range(lenput):
                if input[i] == "1":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("Cheese.")
                elif input[i]  ==  "2":
                    output.up()
                elif input[i]  ==  "3":
                    output.down()
                elif input[i]  ==  "4":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "5":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("Cheese.")
                elif input[i]  ==  "6":
                    output.down()
                elif input[i]  ==  "7":
                    output.down()
                elif input[i]  ==  "8":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "9":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("    Cheese.")
                elif input[i]  ==  "0":
                    output.down()
                elif input[i]  ==  "q":
                    output.down()
                elif input[i]  ==  "w":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "e":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("    Cheese.")
                elif input[i]  ==  "r":
                    output.down()
                elif input[i]  ==  "t":
                    output.down()
                elif input[i]  ==  "y":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "u":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("Cheese.")
                elif input[i]  ==  "i":
                    output.down()
                elif input[i]  ==  "o":
                    output.down()
                elif input[i]  ==  "p":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "a":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("    Cheese.")
                elif input[i]  ==  "s":
                    output.down()
                elif input[i]  ==  "d":
                    output.down()
                elif input[i]  ==  "f":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "g":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("Cheese.")
                elif input[i]  ==  "h":
                    output.down()
                elif input[i]  ==  "j":
                    output.down()
                elif input[i]  ==  "k":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "l":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("Cheese.")
                elif input[i]  ==  "z":
                    output.down()
                elif input[i]  ==  "x":
                    output.down()
                elif input[i]  ==  "c":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
                elif input[i]  ==  "v":
                    try:
                        output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2] + input[i +3], False), -250, 250)))
                        i += 3
                    except:
                        try:
                            output.goto(int(clamp(number(input[i] + input[i + 1], False), -250, 250)), int(clamp(number(input[i + 2], False), -250, 250)))
                            i += 2
                        except:
                            try:
                                output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i + 1], False), -250, 250)))
                                i += 1
                            except:
                                try:
                                    output.goto(int(clamp(number(input[i], False), -250, 250)), int(clamp(number(input[i], False), -250, 250)))
                                except:
                                    raiseError("    Cheese.")
                elif input[i]  ==  "b":
                    output.down()
                elif input[i]  ==  "n":
                    output.up()
                elif input[i]  ==  "m":
                    try:
                        output.pencolor(colour(input[i] + input[i + 1], False, True))
                        i += 1
                    except: 
                        try:
                            output.pencolor(colour(input[i], False, True))
                        except:
                            output.pencolor(colour("g", False, True))
    except:
        raiseError("Shredded Cheese.")

def game(input):
    gtype = False
    gspeed = 5
    gcol1 = colour("gg", False)
    gcol2 = colour("gh", False)
    gcol3 = colour("hg", False)
    gcol4 = colour("hh", False)
    gcol5 = colour("yg", False)

    i = 0
    if input[i]  ==  "2":
        gtype = True
    elif input[i]  ==  "4":
        gtype = True
    elif input[i]  ==  "6":
        gtype = True
    elif input[i]  ==  "8":
        gtype = True
    elif input[i]  ==  "0":
        gtype = True
    elif input[i]  ==  "w":
        gtype = True
    elif input[i]  ==  "r":
        gtype = True
    elif input[i]  ==  "y":
        gtype = True
    elif input[i]  ==  "i":
        gtype = True
    elif input[i]  ==  "p":
        gtype = True
    elif input[i]  ==  "s":
        gtype = True
    elif input[i]  ==  "f":
        gtype = True
    elif input[i]  ==  "h":
        gtype = True
    elif input[i]  ==  "k":
        gtype = True
    elif input[i]  ==  "z":
        gtype = True
    elif input[i]  ==  "c":
        gtype = True
    elif input[i]  ==  "b":
        gtype = True
    elif input[i]  ==  "m":
        gtype = True

    i = 1

    if input[i] == "1":
        gspeed = 50
    elif input[i]  ==  "2":
        gspeed = 40
    elif input[i]  ==  "3":
        gspeed = 30
    elif input[i]  ==  "4":
        gspeed = 15
    elif input[i]  ==  "5":
        gspeed = 15
    elif input[i]  ==  "6":
        gspeed = 15
    elif input[i]  ==  "7":
        gspeed = 15
    elif input[i]  ==  "8":
        gspeed = 30
    elif input[i]  ==  "9":
        gspeed = 40
    elif input[i]  ==  "0":
        gspeed = 50
    elif input[i]  ==  "q":
        gspeed = 10
    elif input[i]  ==  "w":
        gspeed = 10
    elif input[i]  ==  "e":
        gspeed = 10
    elif input[i]  ==  "r":
        gspeed = 5
    elif input[i]  ==  "t":
        gspeed = 5
    elif input[i]  ==  "y":
        gspeed = 5
    elif input[i]  ==  "u":
        gspeed = 10
    elif input[i]  ==  "i":
        gspeed = 10
    elif input[i]  ==  "o":
        gspeed = 10
    elif input[i]  ==  "p":
        gspeed = 10
    elif input[i]  ==  "a":
        gspeed = 10
    elif input[i]  ==  "s":
        gspeed = 10
    elif input[i]  ==  "d":
        gspeed = 5
    elif input[i]  ==  "f":
        gspeed = 5
    elif input[i]  ==  "g":
        gspeed = 5
    elif input[i]  ==  "h":
        gspeed = 5
    elif input[i]  ==  "j":
        gspeed = 5
    elif input[i]  ==  "k":
        gspeed = 10
    elif input[i]  ==  "l":
        gspeed = 10
    elif input[i]  ==  "z":
        gspeed = 100
    elif input[i]  ==  "x":
        gspeed = 10
    elif input[i]  ==  "c":
        gspeed = 5
    elif input[i]  ==  "v":
        gspeed = 5
    elif input[i]  ==  "b":
        gspeed = 5
    elif input[i]  ==  "n":
        gspeed = 5
    elif input[i]  ==  "m":
        gspeed = 100

    if input[2] and input[3]:
        gcol1 = colour(input[2] + input[3], False)
    
    if input[4] and input[5]:
        gcol2 = colour(input[4] + input[5], False)
    
    if input[6] and input[7]:
        gcol3 = colour(input[6] + input[7], False)
    
    if input[8] and input[9]:
        gcol4 = colour(input[8] + input[9], False)
    
    if input[10] and input[11]:
        gcol5 = colour(input[10] + input[11], False)

    if gtype == False:
        execPong(gspeed, gcol1, gcol2)
    if gtype == True:
        execSnake(gspeed, gcol1, gcol2, gcol3, gcol4, gcol5)

def execPong(speed, col1, col2):
    toExec = """
# Import the pygame library and initialise the game engine
import pygame
from random import * # This is created by https://www.101computing.net/pong-tutorial-using-pygame-adding-a-scoring-system/ I simply brought it into one file and made the speed customizeable. 
from random import randint
import random
speed = """ + str(speed) + """
pygame.init()
class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    def __init__(self, color, width, height):
        import pygame
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass in the color of the Paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color(""" + str(col1[0]) + """,""" + str(col1[1]) + """,""" + str(col1[2]) + """))
        self.image.set_colorkey(pygame.Color(""" + str(col1[0]) + """,""" + str(col1[1]) + """,""" + str(col1[2]) + """))
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
    def moveUp(self, pixels):
        self.rect.y -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y < 0:
          self.rect.y = 0
    def moveDown(self, pixels):
        self.rect.y += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y > 400:
          self.rect.y = 400
class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    def __init__(self, color, width, height):
        import pygame
        from random import randint
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color(""" + str(col1[0]) + """,""" + str(col1[1]) + """,""" + str(col1[2]) + """))
        self.image.set_colorkey(pygame.Color(""" + str(col1[0]) + """,""" + str(col1[1]) + """,""" + str(col1[2]) + """))
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4,8),randint(-8,8)]
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
    def update(self):
        from random import randint
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    def bounce(self):
        from random import randint
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
pygame.init()
# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
paddleA = Paddle(pygame.Color(""" + str(col2[0]) + """,""" + str(col2[1]) + """,""" + str(col2[2]) + """), 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
paddleB = Paddle(pygame.Color(""" + str(col2[0]) + """,""" + str(col2[1]) + """,""" + str(col2[2]) + """), 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200
ball = Ball(pygame.Color(""" + str(col2[0]) + """,""" + str(col2[1]) + """,""" + str(col2[2]) + """),10,10)
ball.rect.x = 345
ball.rect.y = 195
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
# Add the 2 paddles and the ball to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
#Initialise player scores
scoreA = 0
scoreB = 0
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False
    #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(speed)
    if keys[pygame.K_s]:
        paddleA.moveDown(speed)
    if keys[pygame.K_UP]:
        paddleB.moveUp(speed)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(speed)    
    # --- Game logic should go here
    all_sprites_list.update()
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=690:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]     
    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()
    # --- Drawing code should go here
    # First, clear the screen to black. 
    screen.fill(pygame.Color(""" + str(col1[0]) + """,""" + str(col1[1]) + """,""" + str(col1[2]) + """))
    #Draw the net
    pygame.draw.line(screen, pygame.Color(""" + str(col2[0]) + """,""" + str(col2[1]) + """,""" + str(col2[2]) + """), [349, 0], [349, 500], 5)
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen) 
    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, pygame.Color(""" + str(col2[0]) + """,""" + str(col2[1]) + """,""" + str(col2[2]) + """))
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, pygame.Color(""" + str(col2[0]) + """,""" + str(col2[1]) + """,""" + str(col2[2]) + """))
    screen.blit(text, (420,10))
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()"""

    # print(toExec)
    print("Game starting...")
    exec(toExec)

def execSnake(speed, col1, col2, col3, col4, col5):
    toExec = """
# importing libraries
import pygame
import time
import random
 
snake_speed = """ + str(speed) + """
 
# Window size
window_x = 720 # Originally made by https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
window_y = 480
 
# defining colors
black = pygame.Color(""" + str(col1[0]) + """,""" + str(col1[1]) + """,""" + str(col1[2]) + """)
white = pygame.Color(""" + str(col2[0]) + """,""" + str(col2[1]) + """,""" + str(col2[2]) + """)
red = pygame.Color(""" + str(col3[0]) + """,""" + str(col3[1]) + """,""" + str(col3[2]) + """)
green = pygame.Color(""" + str(col4[0]) + """,""" + str(col4[1]) + """,""" + str(col4[2]) + """)
blue = pygame.Color(""" + str(col5[0]) + """,""" + str(col5[1]) + """,""" + str(col5[2]) + """)
 
# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
 
# initial score
score = 0
 
# displaying Score function
def show_score(choice, color, font, size, score, game_window):
    import pygame
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)
 
# game over function
def game_over(score, game_window):
    import pygame
    import pygame
    import time
    import random
    black = pygame.Color(""" + str(col1[0]) + """,""" + str(col1[1]) + """,""" + str(col1[2]) + """)
    white = pygame.Color(""" + str(col2[0]) + """,""" + str(col2[1]) + """,""" + str(col2[2]) + """)
    red = pygame.Color(""" + str(col3[0]) + """,""" + str(col3[1]) + """,""" + str(col3[2]) + """)
    green = pygame.Color(""" + str(col4[0]) + """,""" + str(col4[1]) + """,""" + str(col4[2]) + """)
    blue = pygame.Color(""" + str(col5[0]) + """,""" + str(col5[1]) + """,""" + str(col5[2]) + """)
    window_x = 720 # Originally made by https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
    window_y = 480
   
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, blue)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
 
 
# Main Function
while True:
    import pygame
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over(score, game_window)
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over(score, game_window)
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over(score, game_window)
 
    # displaying score countinuously
    show_score(1, white, 'times new roman', 20, score, game_window)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
    """
    # print(toExec)
    print("Game starting...")
    exec(toExec)
    return(True)

def colour(input, prnt, type=False):
    output = s_colour(input[0])
    length = len(input)
    for i in range(0, length - 1):
        if prnt: print("RGB value: " + str(output[0]) + ", " + str(output[1]) + ", " + str(output[2]))
        if input[i + 1] == "1":
            output = l_colour(output, [10, 0, 0])
        elif input[i+ 1]  ==  "2":
            output = l_colour(output, [0, 20, 0])
        elif input[i + 1]  ==  "3":
            output = l_colour(output, [0, 0, 30])
        elif input[i + 1]  ==  "4":
            output = l_colour(output, [40, 0, 0])
        elif input[i + 1]  ==  "5":
            output = l_colour(output, [0, 50, 0])
        elif input[i + 1]  ==  "6":
            output = l_colour(output, [60, 0, 0])
        elif input[i + 1]  ==  "7":
            output = l_colour(output, [0, 70, 0])
        elif input[i + 1]  ==  "8":
            output = l_colour(output, [0, 0, 80])
        elif input[i + 1]  ==  "9":
            output = l_colour(output, [90, 0, 0])
        elif input[i + 1]  ==  "0":
            output = l_colour(output, [47, 156, 8])
        elif input[i + 1]  ==  "q":
            output = l_colour(output, [123, 123, 123])
        elif input[i + 1]  ==  "w":
            output = l_colour(output, [255, 128, 0])
        elif input[i + 1]  ==  "e":
            output = l_colour(output, [0, 128, 255])
        elif input[i + 1]  ==  "r":
            output = l_colour(output, [255, 0, 0])
        elif input[i + 1]  ==  "t":
            output = l_colour(output, [0, 255, 0])
        elif input[i + 1]  ==  "y":
            output = l_colour(output, [0, 0, 255])
        elif input[i + 1]  ==  "u":
            output = l_colour(output, [2, 184, 127])
        elif input[i + 1]  ==  "i":
            output = l_colour(output, [127, 255, 11])
        elif input[i + 1]  ==  "o":
            output = l_colour(output, [195, 125, 91])
        elif input[i + 1]  ==  "p":
            output = l_colour(output, [17, 218, 123])
        elif input[i + 1]  ==  "a":
            output = l_colour(output, [127, 118, 12])
        elif input[i + 1]  ==  "s":
            output = l_colour(output, [153, 173, 134])
        elif input[i + 1]  ==  "d":
            output = l_colour(output, [255, 255, 255])
        elif input[i + 1]  ==  "f":
            output = l_colour(output, [130, 165, 216])
        elif input[i + 1]  ==  "g":
            output = l_colour(output, [55, 55, 55])
        elif input[i + 1]  ==  "h":
            output = l_colour(output, [255, 165, 164])
        elif input[i + 1]  ==  "j":
            output = l_colour(output, [0, 0, 0])
        elif input[i + 1]  ==  "k":
            output = l_colour(output, [0, 255, 3])
        elif input[i + 1]  ==  "l":
            output = l_colour(output, [155, 246, 19])
        elif input[i + 1]  ==  "z":
            output = l_colour(output, [135, 212, 181])
        elif input[i + 1]  ==  "x":
            output = l_colour(output, [255, 0, 128])
        elif input[i + 1]  ==  "c":
            output = l_colour(output, [128, 0, 255])
        elif input[i + 1]  ==  "v":
            output = l_colour(output, [0, 0, 255])
        elif input[i + 1]  ==  "b":
            output = l_colour(output, [0, 255, 0])
        elif input[i + 1]  ==  "n":
            output = l_colour(output, [255, 0, 0])
        elif input[i + 1]  ==  "m":
            output = l_colour(output, [255, 78, 113]) 
    if prnt: print("RGB value: " + str(output[0]) + ", " + str(output[1]) + ", " + str(output[2]))
    if prnt: return("\n\rFinal Answer (RGB Value): " + str(output[0]) + ", " + str(output[1]) + ", " + str(output[2]))
    elif not prnt: 
        if not type: return(output)
        if type: return(tuple(output))

def l_colour(initial, goal): # Lerp Colour
    work0 = initial[0] + goal [0]
    ret0 = round(work0 / 2)
    # print(ret0)

    work1 = initial[1] + goal [1]
    ret1 = round(work1 / 2)

    work2 = initial[2] + goal[2]
    ret2 = round(work2 / 2)

    return([ret0, ret1, ret2])
    
def s_colour(input): # Solve Colour
    if input == "1":
        return([10, 0, 0])
    elif input ==  "2":
        return([0, 20, 0])
    elif input  ==  "3":
        return([0, 0, 30])
    elif input  ==  "4":
        return([40, 0, 0])
    elif input  ==  "5":
        return([0, 50, 0])
    elif input  ==  "6":
        return([60, 0, 0])
    elif input  ==  "7":
        return([0, 70, 0])
    elif input  ==  "8":
        return([0, 0, 80])
    elif input  ==  "9":
        return([90, 0, 0])
    elif input  ==  "0":
        return([47, 156, 8])
    elif input  ==  "q":
        return([123, 123, 123])
    elif input  ==  "w":
        return([255, 128, 0])
    elif input  ==  "e":
        return([0, 128, 255])
    elif input  ==  "r":
        return([255, 0, 0])
    elif input  ==  "t":
        return([0, 255, 0])
    elif input  ==  "y":
        return([0, 0, 255])
    elif input  ==  "u":
        return([2, 184, 127])
    elif input  ==  "i":
        return([127, 255, 11])
    elif input  ==  "o":
        return([195, 125, 91])
    elif input  ==  "p":
        return([17, 218, 123])
    elif input  ==  "a":
        return([127, 118, 12])
    elif input  ==  "s":
        return([153, 173, 134])
    elif input  ==  "d":
        return([255, 255, 255])
    elif input  ==  "f":
        return([130, 165, 216])
    elif input  ==  "g":
        return([55, 55, 55])
    elif input  ==  "h":
        return([255, 165, 164])
    elif input  ==  "j":
        return([0, 0, 0])
    elif input  ==  "k":
        return([0, 255, 3])
    elif input  ==  "l":
        return([155, 246, 19])
    elif input  ==  "z":
        return([135, 212, 181])
    elif input  ==  "x":
        return([255, 0, 128])
    elif input  ==  "c":
        return([128, 0, 255])
    elif input  ==  "v":
        return([0, 0, 255])
    elif input  ==  "b":
        return([0, 255, 0])
    elif input  ==  "n":
        return([255, 0, 0])
    elif input  ==  "m":
        return([255, 78, 113])
    else:
        return([55, 55, 55])

main()