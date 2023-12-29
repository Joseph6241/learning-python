import random
import matplotlib.pyplot as plt

sides = input("How many sides on the die?")
while not sides.isdigit() or int(sides) <= 0:
    print("Please input whole positive integer in numerals.")
    sides = input("How many sides on the die?")

samples = input("How many rolls to average over?")
while not samples.isdigit() or int(samples) <= 0:
    print("Please input whole positive integer in numerals.")
    samples = input("How many rolls to average over?")

counters = [0] * int(sides)
faces = tuple(i for i in range(1, int(sides) + 1))

for _ in range(int(samples)):
    roll = random.choice(faces)

    for i in range(int(sides)):
        if roll == i + 1:
            counters[i] += 1

for i in range(int(sides)):
    print(f"{((100*counters[i]) / int(samples)):.2f}% {i+1}'s ({counters[i]})")

fig, ax = plt.subplots()
ax.bar(faces, counters)
ax.set_ylabel('Number of rolls')
ax.set_title('Results')
plt.show()
