import tkinter as tk
import random as rd

root = tk.Tk()  # Creates window and defines default size
root.geometry("600x400")

size = 6  # sets game board dimensions and randomization
seed = 0

position = 0 * (size * size)  # a list which corresponds to the board


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
        button.config(text=str(position[i]), fg="#ffffff")


def butt_select(i):  # Changes text color to black for the button that calls it
    buttons[i].config(fg="#000000")


buttons = [tk.Button(root, command=lambda i=i: butt_select(i)) for i in range(size * size)]
# Creates buttons which call the above function

for i, button in enumerate(buttons):  # Places the buttons in a grid
    button.grid(row=i // size + 3, column=i % size + 3)

clear = tk.Button(root, text="Clear", command=game)
clear.grid(row=0, column=0)  # Creates and places the reset button

labels = [tk.Label(root, text=0) for i in range(size * 2)]  # Creates labels

for i, label in enumerate(labels):  # Places labels along the grid
    if i < size:
        label.grid(row=2, column=i + 3)
    else:
        label.grid(row=(i + 1) - size + 2, column=2)

root.mainloop()
