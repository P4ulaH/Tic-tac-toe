import tkinter

canvas = tkinter.Canvas(bg="white", height=530, width=530)
canvas.pack()

#grid
canvas.create_rectangle(10+50,10+50, 460+50, 460+50, outline="black", width=3)
canvas.create_line(160+50, 10+50, 160+50, 460+50, width=3)
canvas.create_line(310+50, 10+50, 310+50, 460+50, width=3)
canvas.create_line(10+50, 160+50, 460+50, 160+50, width=3)
canvas.create_line(10+50, 310+50, 460+50, 310+50, width=3)
#písmená
canvas.create_text(135, 35, text="1", font="Arial 30", fill="gray")
canvas.create_text(285, 35, text="2", font="Arial 30", fill="gray")
canvas.create_text(435, 35, text="3", font="Arial 30", fill="gray")
#čísla
canvas.create_text(35, 135, text="a", font="Arial 30", fill="gray")
canvas.create_text(35, 285, text="b", font="Arial 30", fill="gray")
canvas.create_text(35, 435, text="c", font="Arial 30", fill="gray")

print("\nrules: - you can put coordinations a-c and 1-3 to place the circle or the cross ob the grid")
print("       - you can type exit to exit the game")

def drawCircle(circleCoord):
    if circleCoord == "a1":
        canvas.create_oval(80, 80, 190, 190, fill="", outline="blue", width=10)
    elif circleCoord == "a2":
        canvas.create_oval(230, 80, 340, 190, fill="", outline="blue", width=10)
    elif circleCoord == "a3":
        canvas.create_oval(380, 80, 490, 190, fill="", outline="blue", width=10)
    elif circleCoord == "b1":
        canvas.create_oval(80, 230, 190, 340, fill="", outline="blue", width=10)
    elif circleCoord == "b2":
        canvas.create_oval(230, 230, 340, 340, fill="", outline="blue", width=10)
    elif circleCoord == "b3":
        canvas.create_oval(380, 230, 490, 340, fill="", outline="blue", width=10)
    elif circleCoord == "c1":
        canvas.create_oval(80, 380, 190, 490, fill="", outline="blue", width=10)
    elif circleCoord == "c2":
        canvas.create_oval(230, 380, 340, 490, fill="", outline="blue", width=10)
    elif circleCoord == "c3":
        canvas.create_oval(380, 380, 490, 490, fill="", outline="blue", width=10)
    return
    

def drawCross(crossCoord):
    if crossCoord == "a1":
        canvas.create_line(80, 80, 190, 190, fill="red", width=10)
        canvas.create_line(190, 80, 80, 190, fill="red", width=10)
    elif crossCoord == "a2":
        canvas.create_line(230, 80, 340, 190, fill="red", width=10)
        canvas.create_line(340, 80, 230, 190, fill="red", width=10)
    elif crossCoord == "a3":
        canvas.create_line(380, 80, 490, 190, fill="red", width=10)
        canvas.create_line(490, 80, 380, 190, fill="red", width=10)
    elif crossCoord == "b1":
        canvas.create_line(80, 230, 190, 340, fill="red", width=10)
        canvas.create_line(190, 230, 80, 340, fill="red", width=10)
    elif crossCoord == "b2":
        canvas.create_line(230, 230, 340, 340, fill="red", width=10)
        canvas.create_line(340, 230, 230, 340, fill="red", width=10)
    elif crossCoord == "b3":
        canvas.create_line(380, 230, 490, 340, fill="red", width=10)
        canvas.create_line(490, 230, 380, 340, fill="red", width=10)
    elif crossCoord == "c1":
        canvas.create_line(80, 380, 190, 490, fill="red", width=10)
        canvas.create_line(190, 380, 80, 490, fill="red", width=10)
    elif crossCoord == "c2":
        canvas.create_line(230, 380, 340, 490, fill="red", width=10)
        canvas.create_line(340, 380, 230, 490, fill="red", width=10)
    elif crossCoord == "c3":
        canvas.create_line(380, 380, 490, 490, fill="red", width=10)
        canvas.create_line(490, 380, 380, 490, fill="red", width=10)
    return


coords = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

circleSet = set()
crossSet = set()


def circleOrCross():

        
    while True:
        
        circle = input("\nCircle: ")
        circle = circle.lower()
        if circle == "exit":
            exit()
        elif circle in coords:
            drawCircle(circle)
            coords.remove(circle)
            circleSet.add(circle)
            break
        else:
            print("invalid coordination or the coordination is already occupied")

    if len(coords) == 0:
        print("All the coordinations are filled, it's a tie")
        print("Thanks for playing")
        input("Press any key to exit => ")
        exit()
        
    check()
        
    while True:
        cross = input("Cross: ")
        cross = cross.lower()
        if cross == "exit":
            exit()
        elif cross in coords:
                drawCross(cross)
                coords.remove(cross)
                crossSet.add(cross)
                break
        else:
            print("invalid coordination")


def check():
    
    #checking circle
    if "a1" in circleSet and "a2" in circleSet and "a3" in circleSet:
        canvas.create_line(70, 140, 500, 140, width=15, fill="black")
        print("The winner is CIRCLE!!!")
        input("Press any key to exit => ")
        exit()
    
    elif "b1" in circleSet and "b2" in circleSet and "b3" in circleSet:
        canvas.create_line(70, 290, 500, 290, width=15)
        print("The winner is CIRCLE!!!")
        input("Press any key to exit => ")
        exit()
        
    
    elif "c1" in circleSet and "c2" in circleSet and "c3" in circleSet:
        canvas.create_line(70, 440, 500, 440, width=15)
        print("The winner is CIRCLE!!!")
        input("Press any key to exit => ")
        exit()
    
    elif "a1" in circleSet and "b1" in circleSet and "c1" in circleSet:
        canvas.create_line(140, 70, 140, 500, width=15)
        print("The winner is CIRCLE!!!")
        input("Press any key to exit => ")
        exit()

    elif "a2" in circleSet and "b2" in circleSet and "c2" in circleSet:
        canvas.create_line(290, 70, 290, 500, width=15)
        print("The winner is CIRCLE!!!")
        input("Press any key to exit => ")
        exit()
    
    elif "a3" in circleSet and "b3" in circleSet and "c3" in circleSet:
        canvas.create_line(440, 70, 440, 500, width=15)
        print("The winner is CIRCLE!!!")
        input("Press any key to exit => ")
        exit()
   
    elif "a1" in circleSet and "b2" in circleSet and "c3" in circleSet:
        canvas.create_line(80, 80, 490, 490, width=15)
        print("The winner is CIRCLE!!!")
        input("Press any key to exit => ")
        exit()
    
    elif "c1" in circleSet and "b2" in circleSet and "a3" in circleSet:
        canvas.create_line(490, 80, 80, 490, width=15)
        print("The winner is CIRCLE!!!")
        input("Press any key to exit => ")
        exit()

    
    #checking cross
    if "a1" in  crossSet and "a2" in  crossSet and "a3" in  crossSet:
        canvas.create_line(70, 140, 500, 140, width=15, fill="black")
        print("The winner is CROSS!!!")
        input("Press any key to exit => ")
        exit()
    
    elif "b1" in  crossSet and "b2" in  crossSet and "b3" in  crossSet:
        canvas.create_line(70, 290, 500, 290, width=15)
        print("The winner is CROSS!!!")
        input("Press any key to exit => ")
        exit()
        
    
    elif "c1" in  crossSet and "c2" in  crossSet and "c3" in  crossSet:
        canvas.create_line(70, 440, 500, 440, width=15)
        print("The winner is CROSS!!!")
        input("Press any key to exit => ")
        exit()
    
    elif "a1" in  crossSet and "b1" in  crossSet and "c1" in  crossSet:
        canvas.create_line(140, 70, 140, 500, width=15)
        print("The winner is CROSS!!!")
        input("Press any key to exit => ")
        exit()

    elif "a2" in  crossSet and "b2" in  crossSet and "c2" in  crossSet:
        canvas.create_line(290, 70, 290, 500, width=15)
        print("The winner is CROSS!!!")
        input("Press any key to exit => ")
        exit()
    
    elif "a3" in  crossSet and "b3" in  crossSet and "c3" in  crossSet:
        canvas.create_line(440, 70, 440, 500, width=15)
        print("The winner is CROSS!!!")
        input("Press any key to exit => ")
        exit()
   
    elif "a1" in  crossSet and "b2" in  crossSet and "c3" in  crossSet:
        canvas.create_line(80, 80, 490, 490, width=15)
        print("The winner is CROSS!!!")
        input("Press any key to exit => ")
        exit()
    
    elif "c1" in  crossSet and "b2" in  crossSet and "a3" in  crossSet:
        canvas.create_line(490, 80, 80, 490, width=15)
        print("The winner is CROSS!!!")
        input("Press any key to exit => ")
        exit()

    return 

    
    
while True:
    
    if len(coords) == 0:
        print("All the coordinations are filled, it's a tie")
        print("Thanks for playing")
        input("Press any key to exit => ")
        exit()
    
    circleOrCross()
    
    check()




    

    
    




