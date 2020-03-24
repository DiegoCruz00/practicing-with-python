import math


def printArrivalTime():
   print("{0}:{1}".format(getArrivalHour(), getArrivalMinutes()))

def getArrivalHour():
   return math.floor(arrivalTime)

def getArrivalMinutes():
   return round((arrivalTime - (math.floor(arrivalTime))) * 60)


initialTime = 6 + (52 / 60)

minutesPerEasyPaceMile = 8.25
minutesPerTempoMile = 7.2

milesAtEasyPace = float(input())
milesAtTempo = float(input())

totalExerciseTimeInMinutes = (milesAtEasyPace * minutesPerEasyPaceMile) + (milesAtTempo * minutesPerTempoMile)

totalExerciseTimeInHours = totalExerciseTimeInMinutes / 60

arrivalTime = initialTime + totalExerciseTimeInHours

printArrivalTime()
