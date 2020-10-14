# Guess the word
# By Lewis Taylor
# Student ID: 18027909
import turtle # used to manipulate pixels on window 
import threading # used to access timer function 

# used to count the number of elements (in our case characters) in a list
def count_chars(txt):
    result = 0
    for char in txt:
        result += 1  # same as result = result + 1
    return result

# used to return whether the number that is inputted is a integer or not. This does this in the form of True/False statements. 
def player_2_num(player):
    #iterating over 'player_2'
    for character in player:
        if character.isdigit() is True:
            # Test for digit
            contains_digit = True
        else:
            contains_digit = False
        return contains_digit

#  used to count if the number of characters exceeds 1. 
def num_of_chars(player):
    player_chosen_letter = []
    player_chosen_letter.append(player)
    player = list(player_chosen_letter[0])
    if count_chars(player) > 1:
        return True
    else:
        return False

# used to create an animation effect for the ambulancs light
# gives the impression that the ambulance light is blinking
def flash():
    for i in range(5):
        pen_draw_8 = turtle.Turtle()
        pen_draw_8.penup()
        pen_draw_8.width(5)
        pen_draw_8.speed(0)
        pen_draw_8.goto(10, 110)
        pen_draw_8.pendown()
        pen_draw_8.color("red")
        pen_draw_8.left(90) 
        pen_draw_8.forward(20)
        pen_draw_8.penup()
        pen_draw_8.goto(20, 110)
        pen_draw_8.pendown()
        pen_draw_8.right(45)
        pen_draw_8.forward(20)
        pen_draw_8.penup()
        pen_draw_8.goto(0, 110)
        pen_draw_8.pendown()
        pen_draw_8.left(90)
        pen_draw_8.forward(20)
        pen_draw_8.clear()
        pen_draw_8.hideturtle()


def ambulance_windscreen(drawing_counter, pen_draw_1, attempts):
    #  Ambulance body and windscreen
    pen_draw_1.penup() 
    pen_draw_1.goto(-120,-100)
    pen_draw_1.width(5)
    pen_draw_1.speed(0) 
    pen_draw_1.pendown()
    pen_draw_1.color("Blue")
    pen_draw_1.begin_fill()
    pen_draw_1.fillcolor("White")
    pen_draw_1.forward(10)
    pen_draw_1.right(90)
    pen_draw_1.circle(20, -180)
    pen_draw_1.right(90) 
    pen_draw_1.forward(130)
    pen_draw_1.right(90)
    pen_draw_1.circle(20, -180)
    pen_draw_1.right(90)
    pen_draw_1.forward(10)
    pen_draw_1.right(-90)
    pen_draw_1.forward(75)
    pen_draw_1.right(-90)
    pen_draw_1.forward(80)
    pen_draw_1.right(90)
    pen_draw_1.forward(65)
    pen_draw_1.right(-90)
    pen_draw_1.forward(150)
    pen_draw_1.right(-90)
    pen_draw_1.forward(140)
    pen_draw_1.end_fill()
    pen_draw_1.penup()
    pen_draw_1.goto(-120, 40)
    pen_draw_1.pendown()
    pen_draw_1.color("blue")
    pen_draw_1.begin_fill()
    pen_draw_1.fillcolor("White")
    pen_draw_1.right(225) 
    pen_draw_1.forward(60)
    pen_draw_1.right(45)
    pen_draw_1.forward(145)
    pen_draw_1.right(130)
    pen_draw_1.forward(55)
    pen_draw_1.right(50)
    pen_draw_1.forward(150)
    pen_draw_1.end_fill()
    pen_draw_1.penup()
    pen_draw_1.goto(30,-25)
    pen_draw_1.pendown()
    pen_draw_1.begin_fill()
    pen_draw_1.fillcolor("Black")
    pen_draw_1.right(130) 
    pen_draw_1.forward(60)
    pen_draw_1.left(40)
    pen_draw_1.forward(60)
    pen_draw_1.left(140)
    pen_draw_1.forward(60)
    pen_draw_1.left(40)
    pen_draw_1.forward(60) 
    pen_draw_1.end_fill()
    pen_draw_1.penup()
    pen_draw_1.goto(30,-25)
    pen_draw_1.pendown()
    pen_draw_1.begin_fill()
    pen_draw_1.fillcolor("White")
    pen_draw_1.left(90)
    pen_draw_1.forward(80)
    pen_draw_1.left(50)
    pen_draw_1.forward(60)
    pen_draw_1.left(130)
    pen_draw_1.forward(80)
    pen_draw_1.left(50)
    pen_draw_1.forward(60)
    pen_draw_1.left(130)
    pen_draw_1.forward(80)
    pen_draw_1.end_fill()
    pen_draw_1.penup()
    pen_draw_1.pendown()
    pen_draw_1.begin_fill()
    pen_draw_1.fillcolor("White")
    pen_draw_1.right(90)
    pen_draw_1.forward(75)
    pen_draw_1.left(140)
    pen_draw_1.forward(60)
    pen_draw_1.left(40)
    pen_draw_1.forward(75)
    pen_draw_1.left(140)
    pen_draw_1.forward(55) 
    pen_draw_1.end_fill()
    pen_draw_1.penup()
    pen_draw_1.hideturtle()
    attempts.pendown()
    attempts.clear()
    attempts.penup()
    attempts.speed(0)
    attempts.goto(150, -200)
    attempts.pendown() 
    attempts.color('White')
    attempts.write('You have ' + str(drawing_counter) + ' attempts left', False, align="center", font = ('ariel', 10, 'bold'))
    attempts.penup() 
    attempts.hideturtle()


def side_window(drawing_counter, pen_draw_2, attempts):
     # Ambulance side window
     pen_draw_2.penup()
     pen_draw_2.goto(20,-20)
     pen_draw_2.width(5)
     pen_draw_2.speed(0)
     pen_draw_2.pendown()
     pen_draw_2.color("Blue")
     pen_draw_2.begin_fill()
     pen_draw_2.fillcolor("Black")
     pen_draw_2.left(90)
     pen_draw_2.forward(50)
     pen_draw_2.left(90)
     pen_draw_2.forward(110)
     pen_draw_2.left(90)
     pen_draw_2.forward(50)
     pen_draw_2.left(90)
     pen_draw_2.forward(110)
     pen_draw_2.end_fill()
     pen_draw_2.penup()
     pen_draw_2.hideturtle()
     attempts.pendown()
     attempts.clear()
     attempts.penup()
     attempts.speed(0)
     attempts.goto(150, -200)
     attempts.pendown() 
     attempts.color('White')
     attempts.write('You have ' + str(drawing_counter) + ' attempts left', False, align="center", font = ('ariel', 10, 'bold'))
     attempts.penup() 
     attempts.hideturtle()


def left_wheel(drawing_counter, pen_draw_3, attempts):
    # left wheel 
    pen_draw_3.penup()
    pen_draw_3.goto(-90,-115)
    pen_draw_3.width(5)
    pen_draw_3.speed(0)
    pen_draw_3.pendown()
    pen_draw_3.color("Black")
    pen_draw_3.begin_fill()
    pen_draw_3.fillcolor("Black")
    pen_draw_3.circle(15, 360)
    pen_draw_3.end_fill()
    pen_draw_3.penup()
    pen_draw_3.hideturtle()
    attempts.pendown()
    attempts.clear()
    attempts.penup()
    attempts.speed(0)
    attempts.goto(150, -200)
    attempts.pendown()
    attempts.color('White')
    attempts.write('You have  ' + str(drawing_counter) + ' attempts left', False, align="center", font = ('ariel', 10, 'bold'))
    attempts.hideturtle()

def right_wheel(drawing_counter, pen_draw_4, attempts):
    # right wheel 
    pen_draw_4.penup()
    pen_draw_4.goto(80, -115)
    pen_draw_4.width(5)
    pen_draw_4.speed(0)
    pen_draw_4.pendown()
    pen_draw_4.color("Black")
    pen_draw_4.begin_fill()
    pen_draw_4.fillcolor("Black")
    pen_draw_4.circle(15, 360)
    pen_draw_4.end_fill()
    pen_draw_4.penup()    
    pen_draw_4.hideturtle()
    attempts.pendown()
    attempts.clear()
    attempts.penup()
    attempts.speed(0)
    attempts.goto(150, -200)
    attempts.pendown() 
    attempts.color('White')
    attempts.write('You have ' + str(drawing_counter) + ' attempts left', False, align="center", font = ('ariel', 10, 'bold'))
    attempts.penup() 
    attempts.hideturtle()


def first_cross(drawing_counter, pen_draw_5, attempts):
    # First half of cross
    pen_draw_5.penup()
    pen_draw_5.width(5)
    pen_draw_5.speed(0)
    pen_draw_5.goto(-30, -50)
    pen_draw_5.pendown()
    pen_draw_5.begin_fill()
    pen_draw_5.fillcolor("red")
    pen_draw_5.forward(50)
    pen_draw_5.right(90)
    pen_draw_5.forward(10)
    pen_draw_5.right(90)
    pen_draw_5.forward(50)
    pen_draw_5.right(90)
    pen_draw_5.forward(10)
    pen_draw_5.end_fill() 
    pen_draw_5.penup()
    pen_draw_5.hideturtle()
    attempts.pendown()
    attempts.clear()
    attempts.penup()
    attempts.speed(0)
    attempts.goto(150, -200)
    attempts.pendown() 
    attempts.color('White')
    attempts.write('You have ' + str(drawing_counter) + ' attempts left', False, align="center", font = ('ariel', 10, 'bold'))
    attempts.penup() 
    attempts.hideturtle()


def second_cross(drawing_counter, pen_draw_6, attempts):
    # Second half of cross
    pen_draw_6.penup() 
    pen_draw_6.width(5)
    pen_draw_6.speed(0)
    pen_draw_6.goto(0, -30)
    pen_draw_6.pendown()
    pen_draw_6.begin_fill()
    pen_draw_6.fillcolor("red")
    pen_draw_6.right(90) 
    pen_draw_6.forward(50)
    pen_draw_6.right(90)
    pen_draw_6.forward(10)
    pen_draw_6.right(90)
    pen_draw_6.forward(50)
    pen_draw_6.right(90)
    pen_draw_6.forward(10)
    pen_draw_6.end_fill() 
    pen_draw_6.penup()
    pen_draw_6.hideturtle()
    attempts.pendown()
    attempts.clear()
    attempts.penup()
    attempts.speed(0)
    attempts.goto(150, -200)
    attempts.pendown() 
    attempts.color('White')
    attempts.write('You have ' + str(drawing_counter) + ' attempts left', False, align="center", font = ('ariel', 10, 'bold'))
    attempts.penup() 
    attempts.hideturtle()


def ambulance_light(drawing_counter, pen_draw_7, attempts):
    #  Ambulance light
    pen_draw_7.penup()
    pen_draw_7.width(5)
    pen_draw_7.speed(0)
    pen_draw_7.goto(-10, 60)
    pen_draw_7.pendown()
    pen_draw_7.begin_fill()
    pen_draw_7.fillcolor("red")
    pen_draw_7.left(90)
    pen_draw_7.forward(20)
    pen_draw_7.right(45)
    pen_draw_7.forward(20)
    pen_draw_7.right(45)
    pen_draw_7.forward(20)
    pen_draw_7.right(130)
    pen_draw_7.forward(20)
    pen_draw_7.right(50)
    pen_draw_7.forward(20)
    pen_draw_7.left(90)
    pen_draw_7.forward(20)
    pen_draw_7.left(90)
    pen_draw_7.forward(20)
    pen_draw_7.left(90)
    pen_draw_7.forward(20)
    pen_draw_7.left(90)
    pen_draw_7.forward(20)
    pen_draw_7.backward(20)
    pen_draw_7.right(135)
    pen_draw_7.forward(20)
    pen_draw_7.right(135)
    pen_draw_7.forward(20)
    pen_draw_7.right(45)
    pen_draw_7.forward(20)
    pen_draw_7.right(135)
    pen_draw_7.forward(20)
    pen_draw_7.left(90)
    pen_draw_7.forward(20)
    pen_draw_7.end_fill() 
    pen_draw_7.penup()
    pen_draw_7.hideturtle()
    attempts.pendown()
    attempts.clear()
    attempts.penup()
    attempts.speed(0)
    attempts.goto(150, -200)
    attempts.pendown() 
    attempts.color('White')
    attempts.write('You have ' + str(drawing_counter) + ' attempts left', False, align="center", font = ('ariel', 10, 'bold'))
    attempts.penup() 
    attempts.hideturtle()


def light_rays(drawing_counter, attempts, counter):
     #  Ambulance light rays 
     print("Game Over!")
     attempts.pendown()
     attempts.clear()
     attempts.penup()
     attempts.speed(0)
     attempts.goto(150, -200)
     attempts.pendown() 
     attempts.color('White')
     attempts.write('You have ' + str(drawing_counter) + ' attempts left', False, align="center", font = ('ariel', 10, 'bold'))
     attempts.clear() 
     attempts.penup()
     attempts.speed(0)
     attempts.goto(150, -200)
     attempts.pendown() 
     attempts.color('Red')
     attempts.write('You lose!!!', False, align="center", font = ('ariel', 18, 'bold'))
     attempts.penup()
     attempts.hideturtle()
     while counter == 8:
         timer = threading.Timer(10.0, flash(), args=None, kwargs=None) # used to run the flash() funtion for a given period of time 
         timer.start()
         timer.cancel()
         input("Please press enter to restart game") # restarts the program
         break
     

            
def main():
    player_1_chosen_word = [] # empty list created to append the word typed in by player_1
    player_2_chosen_word = [] # empty list created to append the character typed in by player_2
    hidden_word = []
    player_2_append = []
    drawing_counter = 8 
    CONST_empty_string = "" # used to show that player_1 is an empty string
    counter = 0
    drawing_counter = 8
    window = turtle.Screen()
    window.title("Guess the word")
    window.bgcolor("grey")
    window.setup(width=500, height=500)


    while counter == 0:
        print("\n\nPlease give 3-5 seconds everytime you input your guess to allow the value to be properly processed.", end = " ")
        print("Otherwise, you will experience issues with the animation being incorrectly displayed on the screen and the number of attempts that you have left.") 
        #  Player 1
        print("\n\n\n---------- PLAYER 1 ----------")
        print("Make sure player 2 is not peaking")
        
        player_1 = input("Enter your word (if it has a space, use '-' e.g. 'ice cream'): ").lower()

        while player_1 == "":
            # while player_1 is equal to an empty string, re-insert "Enter your word"
            print("Please enter a character")
            player_1 = input("Enter your word (if it has a space, use '-' e.g. 'ice cream'): ").lower()
                

        while player_2_num(player_1) is True:
            print("Please enter a character") 
            player_1 = input("Enter your word (if it has a space, use '-' e.g. 'ice cream'): ").lower()  

                   
        player_1_chosen_word.append(player_1)
        player_1 = list(player_1_chosen_word[0]) # 0 is the index of the list storing the entire string as index of 0 i.e. 'python'.
                                                 # Where as here, it has been placed within the list function to split apart the characters into individual indexes.
                                                 # Now we can convert each of the letters to stars to display on the window to hide the characters.                                      


        for i in range(count_chars(player_1)):
            hidden_word.extend("*")              #  adds each character to the empty list in correspondence to the length of the hidden word
        


        #  "Guess the word" text
        pen_txt_1 = turtle.Turtle()
        pen_txt_1.penup()
        pen_txt_1.goto(-220, 180)
        pen_txt_1.pendown()
        pen_txt_1.color("White")
        pen_txt_1.write('Guess the word:\n ' + str(' '.join(hidden_word)), False, 'left', font=('Cooper Black', 18, 'bold'))
        pen_txt_1.penup() 
        pen_txt_1.hideturtle()


        # assigning Turtle() function to variables relevant to each drawing of the ambulance.
        pen_txt_2 = turtle.Turtle() 
        pen_txt_2.hideturtle()
        pen_draw_1 = turtle.Turtle()
        pen_draw_1.hideturtle()
        pen_draw_2 = turtle.Turtle()
        pen_draw_2.hideturtle()
        pen_draw_3 = turtle.Turtle()
        pen_draw_3.hideturtle()
        pen_draw_4 = turtle.Turtle()
        pen_draw_4.hideturtle()
        pen_draw_5 = turtle.Turtle()
        pen_draw_5.hideturtle()
        pen_draw_6 = turtle.Turtle()
        pen_draw_6.hideturtle()
        pen_draw_7 = turtle.Turtle()
        pen_draw_7.hideturtle()

        
        # Multiple backslashes have been used so that you cannot see player_1's inputted word
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n---------- PLAYER 2 ----------")
         

        # Used for text relating to the number of attempts player_2 has left.
        # Also used to display win/lose on screen. 
        attempts = turtle.Turtle()
        attempts.penup()
        attempts.goto(150, -200)
        attempts.pendown() 
        attempts.color('White')
        attempts.write('You have ' + str(drawing_counter) + ' attempts left', False, align="center", font = ('ariel', 10, 'bold'))
        attempts.penup() 
        attempts.hideturtle()

            
        # keeps user to be continuously asked "Guess the letter" unless the word has been guessed or the number of attempts has run out.
        while counter != 9:
            if hidden_word == player_1:
                print("You Win")
                attempts.penup() 
                attempts.goto(150, -200)
                attempts.pendown() 
                attempts.color('Blue')
                attempts.clear() 
                attempts.write('You Win!!!', False, align="center", font = ('ariel', 18, 'bold'))
                attempts.penup()
                attempts.hideturtle()
                input("Press enter to restart game")
                pen_txt_1.clear() 
                pen_txt_2.clear()
                pen_draw_1.clear()
                pen_draw_2.clear()
                pen_draw_3.clear()
                pen_draw_4.clear()
                pen_draw_5.clear()
                pen_draw_6.clear() 
                pen_draw_7.clear()
                attempts.clear()
                player_1_chosen_word = []
                player_2_chosen_word = []
                hidden_word = []
                player_2_append = []
                drawing_counter = 8
                counter = 0
                break

            
            player_2 = input("Guess a letter:").lower()
            if player_2 in player_1:
                for i in range(count_chars(player_1)): 
                    char = player_1[i]
                    if char == player_2:  # if the character in player_1 is in player_2, then the star which masks the character within the given index is replaced by the correct letter. 
                        hidden_word[i] = player_1[i]
                        print(hidden_word)
                        pen_txt_1.penup()
                        pen_txt_1.goto(-220, 180)
                        pen_txt_1.pendown() 
                        pen_txt_1.clear()
                        pen_txt_1.write('Guess the word:\n ' + str(' '.join(hidden_word)), False, 'left', font=('ariel', 18, 'bold'))
                        pen_txt_1.penup() 
                        pen_txt_1.hideturtle()
            elif player_2 not in player_1[i] and player_2_num(player_2) is False and num_of_chars(player_2) is False: # player_2 not in player_1 and player_2 is not greater than 1 character
                    counter += 1
                    drawing_counter -= 1
                    print("You Guess wrong!")
                    player_2_append.append(player_2)
                    pen_txt_2.penup()
                    pen_txt_2.goto(-220,-220)
                    pen_txt_2.pendown()
                    pen_txt_2.color("White")
                    pen_txt_2.write('Wrong guesses:\n' + str(' '.join(player_2_append)), False, 'left', font=('Arial', 18, 'bold'))
                    pen_txt_2.penup()
                    pen_txt_2.hideturtle()
                    if counter == 1:
                        ambulance_windscreen(drawing_counter, pen_draw_1, attempts) 
                    if counter == 2:
                        side_window(drawing_counter, pen_draw_2, attempts) 
                    if counter == 3:
                        left_wheel(drawing_counter, pen_draw_3, attempts)
                    if counter == 4:
                        right_wheel(drawing_counter, pen_draw_4, attempts) 
                    if counter == 5:
                        first_cross(drawing_counter, pen_draw_5, attempts)
                    if counter == 6:
                        second_cross(drawing_counter, pen_draw_6, attempts)
                    if counter == 7:
                        ambulance_light(drawing_counter, pen_draw_7, attempts)
                    if counter == 8:
                        light_rays(drawing_counter, attempts, counter)
                        counter += 1
                    # when counter hits 9, it'll clear everything on the screen other than the grey background of the application window        
                    if counter == 9:
                        pen_txt_1.clear() 
                        pen_txt_2.clear()
                        pen_draw_1.clear()
                        pen_draw_2.clear()
                        pen_draw_3.clear()
                        pen_draw_4.clear()
                        pen_draw_5.clear()
                        pen_draw_6.clear() 
                        pen_draw_7.clear()
                        attempts.clear()
                        player_1_chosen_word = []
                        player_2_chosen_word = []
                        hidden_word = []
                        player_2_append = []
                        drawing_counter = 8
                        counter = 0
                        break
            elif player_2_num(player_2) is True and num_of_chars(player_2) is False:  #  if player_2 contains a number, but is only 1 character
                print("Please enter a character")
                counter = counter - 1
            elif player_2_num(player_2) is True and num_of_chars(player_2) is True:  #  if player_2 contains a number and contains more than one of any given character
                print("Please enter a single character")
                counter = counter - 1
            elif num_of_chars(player_2) is True and player_2_num(player_2) is False:  #  if player_2 doesn't contain a number, but does contains more than one character
                print("Enter only one character")
                counter = counter - 1
            elif player_2 == CONST_empty_string:  # if player 2 is equal to an empty string i.e. when the user enters an empty space by accident 
                 print("Please enter a character")


main()

          

                        

                        
                        
                        
                           
