inputs = [1, 2, 3, 3, 1, 4]
store_bad = []
store_good = []

for i, value in enumerate(inputs):
    if inputs[i] in store_bad:
        try:
            store_good.remove(inputs[i])
        except ValueError:
            pass

    else:
        store_bad.append(inputs[i])
        store_good.append(inputs[i])

print(store_good)
