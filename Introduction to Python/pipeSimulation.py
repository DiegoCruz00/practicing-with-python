# (entrance, value in m3 / min)
water = [(0, 150)]

# (consume in m3 / min)
machines = [100, 100, 100]
innerSpace = [50, 50, 50]

intervalInSeconds = 5

while True:
    for i in range(len(machines)):
        consume = machines[i] / (60 / intervalInSeconds)

        if innerSpace[i] - consume > 0:
            innerSpace[i] -= consume
        else:
            innerSpace[i] = 0

        print(f"Machine {i + 1}'s use: {consume:.2f} m3")

    availableWater = water[0][1] / (60 / intervalInSeconds)

    for i in range(len(innerSpace)):
        if  innerSpace[i] < 50:
            waterLeftToFill = 50 - innerSpace[i]

            if availableWater > waterLeftToFill:
                innerSpace[i] = 50
                availableWater -= waterLeftToFill

            else:
                innerSpace[i] += availableWater
                availableWater = 0
                break

    print(f"Inner space: {' '.join( map( lambda x: f'{x:.2f} m3', innerSpace))}")
    print(f"Availale water: {availableWater:.2f}")

    action = input()
    if action:
        break

# -> | | | |
