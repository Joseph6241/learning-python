import tkinter as tk
from tkinter import ttk
import random as rd

root = tk.Tk()  # Creates window and defines default size
root.geometry("700x700")

size = 10  # sets game board dimensions and randomization
seed = 0

position = [0] * (size * size)  # a list which corresponds to the board

style_blank = ttk.Style()
style_blank.configure("blank.TButton", foreground="#f0f0f0", background="#f0f0f0")
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

style_correct = ttk.Style()
style_correct.configure("correct.TButton", foreground="#000000", background="#000000")
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
style_incorrect.configure("incorrect.TButton", foreground="#ff0000", background="#ff0000")
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


def game():  # Creates a new game
    global seed, position, button, buttons, label, labels
    seed += 1
    rd.seed(seed)
    position = rd.choices(population=(0, 1), k=(size * size))

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

    for i, label in enumerate(labels):
        if i < size:
            column_sum = new_sum(position[j * size + i] for j in range(size))
            label.config(text=f"{', '.join(str(item) for item in column_sum if item != 0)}")
        else:
            row_sum = new_sum(position[(i - size) * size: (i - size + 1) * size])
            label.config(text=f"{', '.join(str(item) for item in row_sum if item != 0)}")

    for i, button in enumerate(buttons):
        button.configure(text=str(position[i]), style="blank.TButton")


def butt_select(i):  # Changes color of the button based on stored value
    if position[i] == 1:
        buttons[i].configure(style="correct.TButton")
    else:
        buttons[i].configure(style="incorrect.TButton")


buttons = [ttk.Button(root, style="blank.TButton", command=lambda i=i: butt_select(i)) for i in range(size * size)]
# Creates buttons which call the above function

for i, button in enumerate(buttons):  # Sets button size and color
    button.configure(style="blank.TButton")

for i, button in enumerate(buttons):  # Places the buttons in a grid
    button.grid(row=i // size + 3, column=i % size + 3)

clear = ttk.Button(root, text="Clear", command=game)
clear.grid(row=0, column=0)  # Creates and places the reset button

labels = [tk.Label(root, text=0) for i in range(size * 2)]  # Creates labels

for i, label in enumerate(labels):  # Places labels along the grid
    if i < size:
        label.grid(row=2, column=i + 3)
    else:
        label.grid(row=(i + 1) - size + 2, column=2)

root.mainloop()
