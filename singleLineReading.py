# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:35:47 2016

@author: yifanli
"""

import turtle

def main():
    
    #filename = input("Please enter drawing filename: ")
    filename = "drawingSingle.txt"
    
    t = turtle.Turtle()
    screen = t.getscreen()
    
    file = open(filename,"r")
    
    for line in file:
        """ first, purify each line of records of the drawing file used """
        text = line.strip()
        """ second, make all records of each line an array of strings """
        commandList = text.split(",")
        """ third, select the first string argument as the command"""
        command = commandList[0]
        
        """Examine the command and execute it"""
        if command == "goto":
            x=float(commandList[1])
            y=float(commandList[2])
            width=float(commandList[3])
            color=commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else :
            print "Unknown command found in file",command
            
    file.close()
    
    """Hide the turtle that we used to draw"""
    t.ht()
    """This causes the program to hold the turtle graphics window open 
    until the mouse is clicked."""
    screen.exitonclick()
    print("Program execution completed.")
    
"""if _name_ == "_main_" :"""

main()
           
            
            
            
            
            
            
            
            
            
            
            
    
            
            
            
            
            
            
            
            
            
            
            