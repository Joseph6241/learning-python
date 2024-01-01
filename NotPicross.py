import tkinter as tk
from tkinter import ttk
import random as rd

root = tk.Tk()  # Creates window and defines default size
root.minsize(width=300, height=250)
root.title("Not Picross")

size = 6  # sets game board dimensions and randomization
seed = 0

position = [0] * (size * size)  # a list which corresponds to the board
labels = []
mistakes = 0

style_blank = ttk.Style()

style_blank.configure(
    "blank.TButton", 
     foreground="#aaaaaa", 
     background="#aaaaaa"
     )

style_blank.layout(
    "blank.TButton",
    [
        ("Button.focus", {
            'children': [
                ("Button.padding", {
                    'children': [
                        ("Button.label", {'side': 'top', 'sticky': ''})
                    ],
                    'sticky': 'nswe'
                })
            ],
            'sticky': 'nswe'
        })
    ]
)


style_marked = ttk.Style()

style_marked.configure(
    "marked.TButton", 
     foreground="#ffaaaa", 
     background="#ffaaaa"
     )

style_marked.layout(
    "marked.TButton",
    [
        ("Button.focus", {
            'children': [
                ("Button.padding", {
                    'children': [
                        ("Button.label", {'side': 'top', 'sticky': ''})
                    ],
                    'sticky': 'nswe'
                })
            ],
            'sticky': 'nswe'
        })
    ]
)


style_correct = ttk.Style()

style_correct.configure(
    "correct.TButton", 
     foreground="#000000", 
     background="#000000"
     )

style_correct.layout(
    "correct.TButton",
    [
        ("Button.focus", {
            'children': [
                ("Button.padding", {
                    'children': [
                        ("Button.label", {'side': 'top', 'sticky': ''})
                    ],
                    'sticky': 'nswe'
                })
            ],
            'sticky': 'nswe'
        })
    ]
)


style_incorrect = ttk.Style()

style_incorrect.configure(
    "incorrect.TButton", 
     foreground="#ff0000", 
     background="#ff0000"
     )

style_incorrect.layout(
    "incorrect.TButton",
    [
        ("Button.focus", {
            'children': [
                ("Button.padding", {
                    'children': [
                        ("Button.label", {'side': 'top', 'sticky': ''})
                    ],
                    'sticky': 'nswe'
                })
            ],
            'sticky': 'nswe'
        })
    ]
)


buttons = [ttk.Button(root, style="blank.TButton") for i in range(size * size)]

for i, button in enumerate(buttons):
    button.bind("<Button-1>", lambda event, i=i: left_select(i))
    button.bind("<Button-3>", lambda event, i=i: right_select(i))


def game():  # Creates a new game
    global seed, position, button, buttons, label, labels, mistakes
    seed += 1
    rd.seed(seed)
    position = rd.choices(population=(0, 1), k=(size * size))
    mistakes = 0
    score.config(text = f"Mistakes: {mistakes}")


    def new_sum(input_list):
        result = []
        current_sum = 0

        for num in input_list:
            if num == 1:
                current_sum += 1
            elif num == 0:
                result.append(current_sum)
                current_sum = 0

        if current_sum > 0:
            result.append(current_sum)

        return result

    for i, label in enumerate(labels): # Update labels with sums

        if i < size:
            column_sum = new_sum(position[j * size + i] for j in range(size))
            label.config(text="\n".join(str(item) for item in column_sum if item != 0))
        else:
            row_sum = new_sum(position[(i - size) * size: (i - size + 1) * size])
            label.config(text=" ".join(str(item) for item in row_sum if item != 0))

        for i, button in enumerate(buttons):
            button.configure(text=str(position[i]), style="blank.TButton")


def left_select(i):  # Changes color of the button based on stored value
    global mistakes
    if position[i] == 1:
        buttons[i].configure(style="correct.TButton")
    else:
        buttons[i].configure(style="incorrect.TButton")
        mistakes += 1
        score.config(text = f"Mistakes: {mistakes}")


def right_select(i):  # Changes color of the button based on stored value
    global mistakes
    if position[i] == 0:
        buttons[i].configure(style="marked.TButton")
    else:
        buttons[i].configure(style="incorrect.TButton")
        mistakes += 1
        score.config(text = f"Mistakes: {mistakes}")


for i, button in enumerate(buttons):  # Sets button size and color
    button.configure(
        width=2,
        style="blank.TButton"
    )

for i, button in enumerate(buttons):  # Places the buttons in a grid
    button.grid(
        row=i // size + 2,
        column=i % size + 2
    )

clear = ttk.Button(root, text="New Game", command=game)  # Creates and places new game and score elements
clear.grid(row=0, column=0)
score = tk.Label(root, text = f"Mistakes: {mistakes}")
score.grid(row=1, column=0)

for i in range(size * 2):
    label = tk.Label(root, text="?")
    labels.append(label)

for i, label in enumerate(labels):  # Place labels along the grid
    row = 1 if i < size else (i + 1) - size + 1
    column = i + 2 if i < size else 1
    label.grid(row=row, column=column, padx=5, pady=5)

root.mainloop()
