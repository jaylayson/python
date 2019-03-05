
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 09823239
#    Student name: John Layson
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  FOUR PIECE JIGSAW PUZZLE
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_attempt".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a jigsaw puzzle whose
#  state of completion is determined by data stored in a list which
#  specifies the locations of the pieces.  You are also required to
#  provide a solution to your particular puzzle.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

size_of_pieces = 300 # pixels (excluding any protruding "tabs")
half_piece_size = size_of_pieces / 2
max_tab_size = 100 # pixels
box_size = size_of_pieces + (max_tab_size * 2)
half_box_size = box_size / 2
left_border = max_tab_size
gap = max_tab_size
top_bottom_border = max_tab_size
canvas_height = (top_bottom_border + size_of_pieces) * 2
canvas_width = (size_of_pieces * 2 + left_border) * 2
template_centres = [[-(size_of_pieces + half_piece_size), -half_piece_size], # bottom left
                    [-half_piece_size, -half_piece_size], # bottom right
                    [-(size_of_pieces + half_piece_size), half_piece_size], # top left
                    [-half_piece_size, half_piece_size]] # top right
box_centre = [gap + (box_size / 2), 0]

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background for the puzzle, i.e., the template for the
# pieces and the box they're kept in.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up and at its standard width and colour.
#


# Draw the box that contains unused puzzle pieces.  (The box is
# larger than the puzzle pieces to allow for tabs sticking out on
# any of their four sides.)
def draw_box():

    # Determine the position of the box's bottom-left corner
    bottom_left = [box_centre[0] - half_box_size,
                   box_centre[1] - half_box_size]

    # Go to the bottom-left corner and get ready to draw
    penup()
    goto(bottom_left)
    width(5)
    color('black')
    pendown()
    
    # Walk around the box's perimeter
    setheading(0) # point east
    for side in [1, 2, 3, 4]:
        forward(box_size)
        left(90)

    # Reset the pen
    width(1)
    penup()
 

# Draw the individual squares of the jigsaw's template
def draw_template(show_template = False):

    # Only draw if the argument is True
    if show_template:

        # Set up the pen
        width(3)
        color('grey')

        # Draw a box for each centre coordinate
        for centre_x, centre_y in template_centres:
            
            # Determine the position of this square's bottom-left corner
            bottom_left = [centre_x - half_piece_size,
                           centre_y - half_piece_size]

            # Go to the bottom-left corner and get ready to draw
            penup()
            goto(bottom_left)
            pendown()
        
            # Walk around the square's perimeter
            setheading(0) # point east
            for side in [1, 2, 3, 4]:
                forward(size_of_pieces)
                left(90)

        # Reset the pen
        width(1)
        color('black')
        penup()


# As a debugging aid, mark the coordinates of the centres of
# the template squares and the box
def mark_coords(show_coords = False):

    # Only mark the coordinates if the argument is True
    if show_coords:

        # Don't draw lines between the coordinates
        penup()

        # Go to each coordinate, draw a dot and print the coordinate
        color('black')
        for x_coord, y_coord in template_centres + [box_centre]:
            goto(x_coord, y_coord)
            dot(4)
            write(str(x_coord) + ', ' + str(y_coord),
                  font = ('Arial', 12, 'normal'))

    # Reset the pen
    width(1)
    penup()
               
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# jigsaw puzzle pieces:
#
# 1. The name of the piece, from 'Piece A' to 'Piece D'
# 2. The place to put the piece, either in the template, denoted
#    'Top left', 'Top right', 'Bottom left' or 'Bottom right', or
#    in the unused pieces box, denoted 'In box'
# 3. An optional mystery value, 'X', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily mention all pieces.  Also notice
# that several pieces may be in the box at the same time, in which
# case they should just be drawn on top of each other.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Most importantly, you must write your own data set at the end
# to provide the correct solution to your puzzle.
#

# The following data set doesn't require drawing any jigsaw pieces
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

attempt_00 = []

# Each of the following data sets put just one piece in the box.
# You may find them useful when creating your individual pieces.

attempt_01 = [['Piece A', 'In box']]
attempt_02 = [['Piece B', 'In box']]
attempt_03 = [['Piece C', 'In box']]
attempt_04 = [['Piece D', 'In box']]

# Each of the following data sets put just one piece in a
# location in the template.

attempt_05 = [['Piece A', 'Top left']]
attempt_06 = [['Piece B', 'Bottom right']]
attempt_07 = [['Piece C', 'Top right']]
attempt_08 = [['Piece D', 'Bottom left']]
attempt_09 = [['Piece A', 'Bottom left']]
attempt_10 = [['Piece B', 'Top left']]
attempt_11 = [['Piece C', 'Bottom right']]
attempt_12 = [['Piece D', 'Top right']]

# Each of the following data sets put all four pieces in the
# box, but in different orders.

attempt_13 = [['Piece A', 'In box'], ['Piece B', 'In box'],
              ['Piece C', 'In box'], ['Piece D', 'In box']]
attempt_14 = [['Piece D', 'In box'], ['Piece C', 'In box'],
              ['Piece B', 'In box'], ['Piece A', 'In box']]
attempt_15 = [['Piece C', 'In box'], ['Piece D', 'In box'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]

# Each of the following data sets uses between two and four pieces,
# either in the template or in the box

attempt_16 = [['Piece A', 'Top right'], ['Piece B', 'Bottom left']]
attempt_17 = [['Piece D', 'Bottom right'], ['Piece C', 'In box']]
attempt_18 = [['Piece C', 'Bottom right'], ['Piece A', 'Bottom right']]
attempt_19 = [['Piece B', 'In box'], ['Piece D', 'Top left'],
              ['Piece C', 'In box']]
attempt_20 = [['Piece C', 'Top left'], ['Piece D', 'Top right'],
              ['Piece A', 'Bottom left']]
attempt_21 = [['Piece A', 'In box'], ['Piece D', 'Bottom left'],
              ['Piece C', 'Top right']]
attempt_22 = [['Piece A', 'Bottom left'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom right'], ['Piece D', 'In box']]
attempt_23 = [['Piece D', 'Bottom right'], ['Piece C', 'In box'],
              ['Piece B', 'Top right'], ['Piece A', 'Top left']]
attempt_24 = [['Piece C', 'Bottom right'], ['Piece D', 'Top left'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]
attempt_25 = [['Piece D', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece C', 'Bottom right'], ['Piece A', 'Top right']]
attempt_26 = [['Piece C', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece A', 'Bottom right'], ['Piece D', 'Top right']]
attempt_27 = [['Piece C', 'Bottom left'], ['Piece D', 'In box'],
              ['Piece A', 'Top left'], ['Piece B', 'Top right']]

# Each of the following data sets is a complete attempt at solving
# the puzzle using all four pieces (so there are no pieces left in the box)

attempt_28 = [['Piece A', 'Bottom left'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Top right']]
attempt_29 = [['Piece A', 'Top right'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left']]
attempt_30 = [['Piece A', 'Bottom left'], ['Piece B', 'Top left', 'X'],
              ['Piece C', 'Bottom right'], ['Piece D', 'Top right']]
attempt_31 = [['Piece A', 'Bottom right'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom left', 'X'], ['Piece D', 'Top left']]
attempt_32 = [['Piece D', 'Top right', 'X'], ['Piece A', 'Bottom left', 'X'],
              ['Piece B', 'Top left'], ['Piece C', 'Bottom right']]
attempt_33 = [['Piece A', 'Top right', 'X'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left', 'X']]

# Here you must provide a list which is the correct solution to
# your puzzle.

# ***** Put the solution to your puzzle in this list
solution = [['Piece A', 'Top left'], ['Piece B', 'Top right'],
            ['Piece C', 'Bottom left'], ['Piece D', 'Bottom right']]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_attempt" function.
#

# Draw the jigsaw pieces as per the provided data set
def draw_attempt(puzzle_pieces):
    for text in puzzle_pieces:
        if text[-1] == 'X':
            draw_piece_X(text[1])
        elif text[0] == 'Piece A':
            draw_piece_A(text[1])
        elif text[0] == 'Piece B':
            draw_piece_B(text[1])
        elif text[0] == 'Piece C':
            draw_piece_C(text[1])
        elif text[0] == 'Piece D':
            draw_piece_D(text[1])


##########------------START OF MY CODE-----------############

showturtle()
colormode(255)      #Enable RGB values to 255 each

##Draw Piece A - Border

def draw_piece_A(location):

    if location == 'Top left':
        x = -599
        y = 300
    elif location == 'Top right':
        x = -297
        y = 300
    elif location == 'Bottom left':
        x = -599
        y = -1
    elif location == 'Bottom right':
        x = -297
        y = -2
    elif location == 'In box':
        x = 200
        y = 150

    width(2)        #Change turtle's width
    penup()
    goto(x, y)      #Start at top left corner
    setheading(270) 
    pendown()
    color('black', 'Firebrick')
    begin_fill()
    forward(300)
    setheading(0) 
    forward(125)
    setheading(90) 
    forward(50)
    setheading(0)
    forward(50)
    setheading(270)
    forward(50) 
    setheading(0)
    forward(125)
    setheading(90)
    forward(125)
    setheading(0) 
    forward(50)
    setheading(90)
    forward(50)
    setheading(180)
    forward(50)
    setheading(90)
    forward(125)
    setheading(180)
    forward(300)
    end_fill()
    penup()
    
##Piece A - Quarter Circle - First Layer
    
    color(255, 140, 0)      # Dark Orange
    width(0)
    number_of_reps = 117    #Number of repetitions
    list_of_reps = range(number_of_reps)
    angle = 0
    goto(x + 164, y - 248)  #Desired starting spot
    pendown()
    begin_fill()

    for each_rep in list_of_reps:
        setheading(75)
        right(angle)
        angle = angle + 0.80 #Change angle's value every loop
        forward(2)
    width(3)
    setheading(270)
    forward(24)
    setheading(180)
    forward(50)
    setheading(270)
    forward(124)
    setheading(180)
    forward(120)
    setheading(90)
    forward(49)
    setheading(180)
    forward(12)
    end_fill()
    penup()

##Piece A - Quarter Circle - Second Layer
    
    color(255, 165, 0)      #Orange
    width(0)
    number_of_reps = 112    #Number of repetitions
    list_of_reps = range(number_of_reps)
    angle = 0
    goto(x + 169, y - 248)  #Desired starting spot
    pendown()
    begin_fill()

    for each_rep in list_of_reps:
        setheading(72.4)
        right(angle)
        angle = angle + 0.80 #Change angle's value every loop
        forward(2)
    width(2)
    setheading(270)
    forward(20)
    setheading(180)
    forward(50)
    setheading(270)
    forward(125)
    setheading(180)
    forward(120)
    setheading(90)
    forward(51)
    setheading(180)
    forward(9)
    end_fill()
    penup()

##Piece A - Star
    
    num_of_stars = range(1)     #Number of Stars
    for each_star in num_of_stars: 
        length = 12             #Length of lines
        setheading(-72)         #Opposite of 72 which is 288
        color(255, 140, 0)      #Dark Orange
        goto(x + 249, y - 225)
        pendown()
        begin_fill()
        five_spikes = range(5)  #Repetition
        for each_spike in five_spikes:
            forward(length)
            left(72)            #Angle 
            forward(length)
            right(144)          #Angle
        end_fill()
        penup()

##Draw Piece B - Border

def draw_piece_B(location):

    if location == 'Top left':
        x = -599
        y = 300
    elif location == 'Top right':
        x = -297
        y = 300
    elif location == 'Bottom left':
        x = -599
        y = -1
    elif location == 'Bottom right':
        x = -297
        y = -2
    elif location == 'In box':
        x = 200
        y = 150

    width(2)        #Change turtle's width
    goto(x, y) #Start at top left corner of Top right box
    pendown()
    setheading(270)
    color('black', 'Firebrick')
    begin_fill()
    forward(123)
    setheading(0)
    forward(50)
    setheading(270)
    forward(54)
    setheading(180)
    forward(50)
    setheading(270)
    forward(123)
    setheading(0)
    forward(123)
    setheading(90)
    forward(50)
    setheading(0)
    forward(50)
    setheading(270)
    forward(50)
    setheading(0)
    forward(124)
    setheading(90)
    forward(300)
    setheading(180)
    forward(298)
    end_fill()
    penup()

##Piece B - Quarter Circle - First layer
         
    color(255, 140, 0)      #Dark Orange
    width(0)
    number_of_reps = 69     #Number of repetitions
    list_of_reps = range(number_of_reps)
    angle = 0
    goto(x + 50, y - 150)   #Starting spot
    pendown()
    begin_fill()

    for each_rep in list_of_reps:
        setheading(340)
        right(angle)
        angle = angle + 0.80 #Change angle's value every loop
        forward(2)
    width(3)
    setheading(180)
    forward(21)
    setheading(270)
    forward(49)
    setheading(180)
    forward(117)
    setheading(90)
    forward(117)
    setheading(0)
    forward(50)
    setheading(90)
    forward(12)
    end_fill()      

##Piece B - Quarter Circle - Second Layer

    color(255, 165, 0)      #Orange
    width(0)
    number_of_reps = 63     #Number of repetitions
    list_of_reps = range(number_of_reps)
    angle = 0
    goto(x + 52, y - 157)   #Starting spot
    pendown()
    begin_fill()

    for each_rep in list_of_reps:
        setheading(337)
        right(angle)
        angle = angle + 0.80 #Change angle's value every loop
        forward(2)
    width(3)
    setheading(180)
    forward(14)
    setheading(270)
    forward(50)
    setheading(180)
    forward(118)
    setheading(90)
    forward(117)
    setheading(0)
    forward(50)
    setheading(90)
    forward(22)
    end_fill()
    penup()

##Piece B - Star

    num_of_stars = range(1)        #Number of stars
    for each_star in num_of_stars: 
        length = 12                #Length of lines
        setheading(-72)            #Opposite of 72 which is 288
        color(255, 140, 0)         #Dark Orange
        goto(x + 47, y - 225)
        pendown()
        begin_fill()
        five_spikes = range(5)  #Repetition
        for each_spike in five_spikes:
            forward(length)
            left(72)            #Angle 
            forward(length)
            right(144)          #Angle
        end_fill()
        penup()


##Draw Piece C - Border

def draw_piece_C(location):

    if location == 'Top left':
        x = -599
        y = 300
    elif location == 'Top right':
        x = -297
        y = 300
    elif location == 'Bottom left':
        x = -599
        y = -1
    elif location == 'Bottom right':
        x = -297
        y = -2
    elif location == 'In box':
        x = 200
        y = 150
        
    width(2)        #Change turtle's width
    goto(x, y)      #Start at top left corner of bottom left box
    pendown()
    setheading(270)
    color('black', 'Firebrick')
    begin_fill()
    forward(300)
    setheading(0)
    forward(300)
    setheading(90)
    forward(125)
    setheading(180)
    forward(50)
    setheading(90)
    forward(50)
    setheading(0)
    forward(50)
    setheading(90)
    forward(124)
    setheading(180)
    forward(127)
    setheading(90)
    forward(50)
    setheading(180)
    forward(47)
    setheading(270)
    forward(50)
    setheading(180)
    forward(125)
    end_fill()
    penup()

##Piece C - Quarter Circle - First layer

    color(255, 140, 0)      #Dark Orange
    width(0)
    number_of_reps = 105    #Number of repetitions
    list_of_reps = range(number_of_reps)
    angle = 0
    goto(x + 164, y + 48)   #Starting spot
    pendown()
    begin_fill()

    for each_rep in list_of_reps:
        setheading(256)
        left(angle)
        angle = angle + 0.80 #Change angle's value every loop
        forward(2)
    width(3)
    setheading(0)
    forward(44)
    setheading(90)
    forward(119)
    setheading(180)
    forward(127)
    setheading(90)
    forward(50)
    setheading(180)
    forward(5)
    end_fill()

##Piece C - Quarter Circle - Second layer

    color(255, 165, 0)      #Orange
    width(0)
    number_of_reps = 110    #Number of Repetitions
    list_of_reps = range(number_of_reps)
    angle = 0
    goto(x + 168, y + 48)   #Starting spot
    pendown()
    begin_fill()

    for each_rep in list_of_reps:
        setheading(258)
        left(angle)
        angle = angle + 0.79 #Change angle's value every loop
        forward(2)
    width(2)
    setheading(0)
    forward(26)
    setheading(90)
    forward(119)
    setheading(180)
    forward(127)
    setheading(90)
    forward(50)
    end_fill()
    penup()
    
##Draw Piece C - Star

    num_of_stars = range(1)     #Number of stars
    for each_star in num_of_stars: 
        length = 12             #Length of lines
        setheading(-72)         #Opposite of 72 which is 288
        color(255, 140, 0)      #Dark Orange
        goto(x + 249, y - 24)
        pendown()
        begin_fill()
        five_spikes = range(5) #Repetition
        for each_spike in five_spikes:
            forward(length)
            left(72)            #Angle 
            forward(length)
            right(144)          #Angle
        end_fill()
        penup()


##Draw Piece D - Border

def draw_piece_D(location):

    if location == 'Top left':
        x = -599
        y = 300
    elif location == 'Top right':
        x = -297
        y = 300
    elif location == 'Bottom left':
        x = -599
        y = -1
    elif location == 'Bottom right':
        x = -297
        y = -2
    elif location == 'In box':
        x = 200
        y = 150
        
    width(2)        #Change turtle's width
    goto(x, y)  #Start  at top left corner of bottom right box
    pendown()
    setheading(270)
    color('black', 'Firebrick')
    begin_fill()
    forward(126)
    setheading(180)
    forward(50)
    setheading(270)
    forward(46)
    setheading(0)
    forward(50)
    setheading(270)
    forward(126)
    setheading(0)
    forward(297)
    setheading(90)
    forward(298)
    setheading(180)
    forward(126)
    setheading(90)
    forward(50)
    setheading(180)
    forward(46)
    setheading(270)
    forward(50)
    setheading(180)
    forward(125)
    end_fill()
    penup()

##Piece D - Quarter Circle - First Layer

    color(255, 140, 0)      #Dark Orange
    width(0)
    number_of_reps = 154    #Number of repititions
    list_of_reps = range(number_of_reps)
    angle = 0
    goto(x - 42 , y - 127)        #Starting spot
    pendown()
    begin_fill()

    for each_rep in list_of_reps:
        setheading(343)
        left(angle)
        angle = angle + 0.79 #Change angle's value every loop
        forward(2)

    width(3)
    setheading(180)
    forward(15)
    setheading(270)
    forward(50)
    setheading(180)
    forward(125)
    setheading(270)
    forward(125)
    setheading(180)
    width(2)
    forward(40)
    end_fill()
    penup()

##Piece D - Quarter Circle - Second layer

    color(255, 165, 0)      #Orange
    width(0)
    number_of_reps = 143    #Number of repititions
    list_of_reps = range(number_of_reps)
    angle = 0
    goto(x - 31, y - 127)        #Starting spot
    pendown()
    begin_fill()

    for each_rep in list_of_reps:
        setheading(350)
        left(angle)
        angle = angle + 0.79 ##Change angle's value every loop
        forward(2)
    width(3)
    setheading(180)
    forward(10)
    setheading(270)
    forward(50)
    setheading(180)
    forward(124)
    setheading(270)
    forward(124)
    setheading(180)
    width(0)
    forward(35)
    end_fill()
    penup()

##Draw Piece D - Star

    num_of_stars = range(1) #Number of stars
    for each_star in num_of_stars: 
        length = 12     #Length of lines
        setheading(-72) #Opposite of 72 which is 288
        color(255, 140, 0)
        goto(x + 47, y - 23)
        pendown()
        begin_fill()
        five_spikes = range(5) #Repetition
        for each_spike in five_spikes:
            forward(length)
            left(72)            #Angle 
            forward(length)
            right(144)          #Angle
        end_fill()
        penup()


##Draw Missing Image
def draw_piece_X(location):

    if location == 'Top left':
        x = -515
        y = 225
    elif location == 'Top right':
        x = -215
        y = 225
    elif location == 'Bottom left':
        x = -515
        y = -75
    elif location == 'Bottom right':
        x = -215
        y = -75

##TOP half
    width(4)
    penup()
    goto(x, y)
    setheading(270)
    pendown()
    color('black', 'white')
    begin_fill()
    forward(55)

    num_of_spikes = range(4)
    for each_spike in num_of_spikes:
        length = 25
        setheading(-45)
        forward(length)
        left(90)
        forward(length)
    setheading(90)
    forward(35)
    left(45)
    forward(27)
    setheading(180)
    forward(122)
    end_fill()
    penup()
    goto(x+120,y)
    setheading(270)
    pendown()
    forward(23)
    setheading(0)
    forward(20)
    penup()
##Top X
        
    goto(x+60, y-60)
    setheading(125)
    color('red')
    begin_fill()
    pendown()
    forward(50)
    setheading(0)
    forward(18)
    setheading(-55)
    forward(40)
    setheading(55)
    forward(40)
    setheading(0)
    forward(18)
    setheading(-125)
    forward(52)
    setheading(135)
    forward(17)
    setheading(-135)
    forward(15)
    end_fill()
    penup()
##BOTTOM half
    goto(x, y-65)
    pendown()
    color('black', 'white')
    begin_fill()
    setheading(270)
    forward(90)
    setheading(0)
    forward(142)
    setheading(90)
    forward(90)
    num_of_spikes = range(4)
    for each_spike in num_of_spikes:
        length = 25
        setheading(-135)
        forward(length)
        right(90)
        forward(length)
    end_fill()
    penup()

##Bottom X
    goto(x+60, y-82)
    setheading(-125)
    color('red')
    begin_fill()
    pendown()
    forward(50)
    setheading(0)
    forward(18)
    setheading(55)
    forward(40)
    setheading(-55)
    forward(40)
    setheading(0)
    forward(18)
    setheading(125)
    forward(43)
    setheading(136)
    forward(5)
    width(3)
    forward(20)
    setheading(-132)
    forward(15)
    end_fill()
    penup()


#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing canvas
setup(canvas_width, canvas_height)

# Give the canvas a neutral background colour
# ***** You can change the background colour if necessary to ensure
# ***** good contrast with your puzzle pieces
bgcolor('light grey')

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by solving your puzzle
title('Four Piece Jigsaw Puzzle - Four Star Dragonball')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Draw the box that holds unused jigsaw puzzle pieces
draw_box()

# Draw the template that holds the jigsaw pieces
# ***** If you don't want to display the template change the
# ***** argument below to False
draw_template(True)

# Mark the centres of the places where jigsaw puzzle pieces must
# be drawn
# ***** If you don't want to display the coordinates change the
# ***** argument below to False
mark_coords(True)

# Call the student's function to display the attempted solution
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_attempt(attempt_30)


# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()


#
#--------------------------------------------------------------------#

