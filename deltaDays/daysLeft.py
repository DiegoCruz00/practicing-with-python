def main():
    currentDate, targetDate = input(), input()

    print("{} days left".format(timeLeft(currentDate, targetDate)))

def timeLeft(currentDate, targetDate):
    monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    currentDate, targetDate = formatDates(currentDate, targetDate)

    if targetDate[2] == currentDate[2]:
        if targetDate[1] == currentDate[1]:
            timeLeft = targetDate[0] - currentDate[0]
        else:
            daysToEndOfMonth = monthLengths[currentDate[1] - 1] - currentDate[0]
            daysInNextMonth = targetDate[0]

            daysBetweenMonths = 0
            for i in range(targetDate[1] - currentDate[1] - 1):
                daysBetweenMonths += monthLengths[currentDate[1] + i]

            timeLeft = daysToEndOfMonth + daysBetweenMonths + daysInNextMonth
    else:
        daysToEndOfMonth = monthLengths[currentDate[1] - 1] - currentDate[0]
        daysToEndOfYear = daysToEndOfMonth
        for i in range(12 - currentDate[1]):
            daysToEndOfYear += monthLengths[currentDate[1] + i]

        daysBetweenYears = 0
        for i in range(targetDate[2] - currentDate[2] - 1):
            daysBetweenYears += 365

        daysInTargetMonth = targetDate[0]
        daysSinceBeginningOfYear = daysInTargetMonth
        for i in range(targetDate[1] - 1):
            daysSinceBeginningOfYear += monthLengths[i]

        timeLeft = daysToEndOfYear + daysBetweenYears + daysSinceBeginningOfYear

    return timeLeft

def formatDates(currentDate, targetDate):
    currentDate = currentDate.split("/")
    targetDate = targetDate.split("/")

    for i in range(len(currentDate)):
        currentDate[i] = int(currentDate[i])
        targetDate[i] = int(targetDate[i])

    return currentDate, targetDate

main()

