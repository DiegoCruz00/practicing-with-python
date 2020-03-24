amountOfMissingDays = int(input("Missing days: "))
grade1 = float(input(" > Grade 1: "))
grade2 = float(input(" > Grade 2: "))
grade3 = float(input(" > Grade 3: "))

average = (grade1 + grade2 + grade3) / 3

failedForMissingDays = amountOfMissingDays >= 8

approved = average >= 7 and not failedForMissingDays
failedForLowGrades = average < 4 and not failedForMissingDays

finalTestIsRequired = 4 <= average < 7 and not failedForMissingDays


if failedForMissingDays:
  message = "Sinto muito. Você foi reprovado por faltas."

else:
  if finalTestIsRequired:
    gradeOnFinalTest = float(input(" > Grade on final test: "))
    average = 0.4 * gradeOnFinalTest + 0.6 * average
    passedTheFinalTest = average >= 5

    if passedTheFinalTest:
        message = "Parabéns. Você foi aprovado na final."
    else:
        message = "Sinto muito. Você foi reprovado na final."
  else:

    if approved:
      message = "Parabéns. Você foi aprovado por média."

    elif failedForLowGrades:
      message = "Sinto muito. Você foi reprovado por média."

print(message)
print("Média final = {:.1f}".format(average))
