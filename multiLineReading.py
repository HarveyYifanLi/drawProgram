import turtle

def main():
    
    #filename = input("Please enter drawing filename: ")
    filename = "drawingMulti.txt"
    t=turtle.Turtle()
    screen=t.getscreen()
    
    file = open(filename,"r")
    
    """ Start off by reading the first line of the records """
    """ And note,it is required that each line of the file must contain one single command,"""
    """ but each record consists of multiple single commands"""
    command = file.readline().strip()
    
    """ If the command is not empty we can proceed using the while loop
    to process each records """
    """ This is called 'a loop and half' pattern"""
    while command != "":
        
        """ Note how to handle the potential extra comma (or whatever punctuation marks) in the command """
        if command == "goto" or command == "goto,":
            """ then read the next line using  file.readline()  and 
            create new object based on that result"""
            
            """ x = float(file.readline()) will do the work if file.readline() returns 
            a string containing no comma but it contains a comma and 
            therefore we need operator  .replace(',','')   to strip away the 
            comma in the string above"""
            x = float(file.readline().replace(',','')) 
            """ then read the next line ......"""
            y = float(file.readline().replace(',','')) 
            width = float(file.readline().replace(',','')) 
            color = file.readline().strip() 
            t.width(width) 
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle" or command == "circle,":
            radius = float(file.readline().replace(',','')) 
            width = float(file.readline().replace(',','')) 
            color = file.readline().strip() 
            t.width(width) 
            t.pencolor(color) 
            t.circle(radius)
        elif command == "beginfill" or command == "beginfill,":
            color = file.readline().strip() 
            t.fillcolor(color) 
            t.begin_fill()
        elif command == "endfill" or command == "endfill,":
            t.end_fill()
        elif command == "penup" or command == "penup,":
            t.penup()
        elif command == "pendown" or command == "pendown,":
            t.pendown()
        else:
            print "Unknown command found in file",command
        """ the first line of every other record is read 
        inside the while loop just before the end. 
        When the condition becomes false, the while loop terminates."""
        command = file.readline().strip()
    
    file.close()
    
    t.ht()
    screen.exitonclick()
    print "Program execution completed"
"""    
if _name_ == "_main_":"""
main()
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
