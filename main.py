from tkinter import *
from tkinter import font

# Main Menu Setup
root = Tk()
root.geometry('550x400')
root.resizable(False, False)
root.configure(background='#1f1f1f')

namelist = []
enteredno = 0

def score(screen, namelist, money, start_money, name, action, amount):
    # print(money)
    #The Specific user that was selected
    index = namelist.index(name)
    if action == "Add Money":
        amountadded = int(money[index]) + int(amount)
        money[index] = amountadded
        print(f"{amountadded} was added to {index}'s current balance")
        
    elif action == "Deduct Money":
        amountdeducted = int(money[index]) - int(amount)
        money[index] = amountdeducted
        print(f"{amountdeducted} was deducted to {index}'s current balance")
        
    
    placey = 80
    for i in money:
        moneydrop_label = Label(screen, text=i, font="bold, 14", bg="#1f1f1f", fg="#dedede")
        moneydrop_label.place(x=200, y=placey)
        placey = placey + 35
        

def submit(playerno):
    global namelist
    global enteredno
    
    #If name entered is not empty, add it to namelist
    if name.get()!='':
        namelist.append(name.get())
        enteredno = enteredno+1
        name.delete(0, END)
        
        
        #Stop the main menu screen if enteredno of entered names = player number
        if enteredno==int(playerno):
            root.destroy()
            print(namelist)
            gamescreen(namelist)
    
def gamescreen(namelist):
    screen = Tk()
    screen.geometry("350x560")
    screen.resizable(False, False)
    screen.configure(background='#1f1f1f')


    title = Label(screen, text="Monopoly Bank", font="bold, 20", bg="#1f1f1f", fg="#dedede")
    title.place(x=80, y=15)
    
    placey = 80
    start_money = 30000
    money=[]
    
    #Adding initial money for every player
    for i in namelist:
        money.append(start_money)
    
    #Printing the names and initial money
    for x in namelist:
        namedrop_label = Label(screen, text=x, font="bold, 14", bg="#1f1f1f", fg="#dedede")
        namedrop_label.place(x=20, y=placey)
        
        moneydrop_label = Label(screen, text=start_money, font="bold, 14", bg="#1f1f1f", fg="#dedede")
        moneydrop_label.place(x=200, y=placey)
        
        placey = placey+35
    
    #Player Selection Label
    playerdropdownlabel = Label(screen, text="Select the player:", font="bold, 11", bg="#1f1f1f", fg="#dedede")
    playerdropdownlabel.place(x=20, y=425)
    
    selectedname = StringVar()
    selectedname.set("Player Name:")
    #Dropdown Menu
    drop = OptionMenu(screen, selectedname, *namelist)
    drop.config(bg="#1f1f1f", fg="#dedede")
    drop.place(x=160, y=420)
    #Action Menu
    actionlabel = Label(screen, text="Enter option:", font="bold, 11", bg="#1f1f1f", fg="#dedede")
    actionlabel.place(x=20, y=450)
    
    action = StringVar()
    action.set("Select the action:")
    actionlist = ["Add Money", "Deduct Money"]
    #Dropdown Menu
    actionmenu = OptionMenu(screen, action, *actionlist)
    actionmenu.config(bg="#1f1f1f", fg="#dedede")
    actionmenu.place(x=160, y=455)
    #Amount
    amountlabel = Label(screen, text="Money:", font="bold, 11", bg="#1f1f1f", fg="#dedede")
    amountlabel.place(x=20, y=480)
    amount = Entry(screen, borderwidth=1, highlightthickness=0, bg="#1f1f1f", fg="#dedede")
    amount.place(x=160, y=485, width=110, height=25)
    #Enter Button
    enter = Button(screen, text="Enter", command=lambda:score(screen, namelist, money, start_money, selectedname.get(), action.get(), amount.get()), border = 5, height=1, width=14, bg="#1f1f1f", fg="#dedede")
    enter.place(x=160, y=520)
    
    screen.mainloop()

#MAIN MENU
# Title
title = Label(root, text="Monopoly Bank (To prevent cheating)",
              font="bold, 20", bg="#1f1f1f", fg="#dedede")
title.place(x=45, y=15)

# Label of player no
playerno = Label(root, text="Enter the number of players:", font="bold, 16", bg="#1f1f1f", fg="#dedede")
playerno.place(x=20, y=100, height=40)

# Entry field
number = Entry(root, borderwidth=5, bg="#1f1f1f", fg="#dedede")
number.place(x=350, y=100, width=150, height=35)

# Label of player names
playername = Label(root, text="Enter the player names:", font="bold, 16", bg="#1f1f1f", fg="#dedede")
playername.place(x=20, y=140)

# Entry field
name = Entry(root, borderwidth=5, bg="#1f1f1f", fg="#dedede")
name.place(x=350, y=140, width=150, height=35)

# submit button
btn = Button(root, text="Submit", command=lambda:submit(number.get()), border=5, height=2, width=20, bg="#1f1f1f", fg="#dedede")
btn.place(x=200, y=250)

root.mainloop()