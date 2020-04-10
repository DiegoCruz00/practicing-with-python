distanceInKilometers = float(input())
timeInMinutes = float(input())

distanceInMiles = distanceInKilometers / 1.61
timeInHours = timeInMinutes / 60

speedInMilesPerHour = distanceInMiles / timeInHours

print(speedInMilesPerHour)
