import tkinter as tk
import random

root = tk.Tk()
root.geometry("350x250")
root.title("Rock Paper Scissors")
options = (0, 1, 2)
readable = ("rock.", "paper.", "scissors.")
choice1 = 0
choice2 = 0
score = [0, 0]

text0 = tk.Label(root, text="Make your selection...", font=('Georgia', 32))
text0.pack()
text1 = tk.Label(root, text="", font=('Georgia', 18))
text1.pack()
text2 = tk.Label(root, text="", font=('Georgia', 18))
text2.pack()
text3 = tk.Label(root, text="", font=('Georgia', 18))
text3.pack()
text4 = tk.Label(root, text="", font=('Georgia', 18))
text4.pack()


def rock():
    global choice1
    global choice2
    random.seed()
    choice1 = 0
    choice2 = (random.choice(options))
    text1.config(text="You selected rock.")
    text2.config(text=("The computer selected " + str(readable[choice2])))
    if choice2 == 0:
        draw()
    elif choice2 == 1:
        lose()
    elif choice2 == 2:
        win()


def paper():
    global choice1
    global choice2
    random.seed()
    choice1 = 1
    choice2 = (random.choice(options))
    text1.config(text="You selected paper.")
    text2.config(text=("The computer selected " + str(readable[choice2])))
    if choice2 == 0:
        win()
    elif choice2 == 1:
        draw()
    elif choice2 == 2:
        lose()


def scissors():
    global choice1
    global choice2
    random.seed()
    choice1 = 2
    choice2 = (random.choice(options))
    text1.config(text="You selected scissors.")
    text2.config(text=("The computer selected " + str(readable[choice2])))
    if choice2 == 0:
        lose()
    elif choice2 == 1:
        win()
    elif choice2 == 2:
        draw()


def win():
    global score
    global text3
    global text4
    score[0] = score[0] + 1
    text3.config(text="You win this round.")
    text4.config(text="Score: " + str(score[0]) + ' to ' + str(score[1]))


def lose():
    global score
    global text3
    global text4
    score[1] = score[1] + 1
    text3.config(text="The computer wins this round.")
    text4.config(text="Score: " + str(score[0]) + ' to ' + str(score[1]))


def draw():
    global score
    global text3
    global text4
    text3.config(text="Nobody wins this round.")
    text4.config(text="Score: " + str(score[0]) + ' to ' + str(score[1]))


button1 = tk.Button(root, text="Rock", command=rock)
button1.pack()
button2 = tk.Button(root, text="Paper", command=paper)
button2.pack()
button3 = tk.Button(root, text="Scissors", command=scissors)
button3.pack()

root.mainloop()
