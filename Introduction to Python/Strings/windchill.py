message = "|        |"

for temperature in range(-20, 70, 10):
   message += " {:^6} |".format(str(temperature) + "°F")

message += "\n" + "-" * 91 + "\n"

for windspeed in range(0, 55, 5):
   message += "| {:>2} mph |".format(windspeed)

   for temperature in range(-20, 70, 10):
      t, ws = temperature, windspeed
      windchill = 35.74 + 0.6215 * t - 35.75 * (ws ** 0.16) + 0.4275 * t * (ws ** 0.16)

      message += " {:>6.2f} |".format(windchill)

   message += "\n"

print(message)
