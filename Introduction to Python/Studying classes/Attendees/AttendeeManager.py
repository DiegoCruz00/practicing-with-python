from Attendee import Attendee

class AttendeeManager:
   def __init__(self):
      self.path = "E:/Diego/ComputerScience/Programming/Training Projects/Python/Introduction to Python/Classes/Attendees/attendees.txt"

   def run(self):
      attendeeFile = open(self.path, "r")

      self.attendees = []
      for attendeeData in attendeeFile:
         self.attendees.append(Attendee(eval(attendeeData)))

      attendeeFile.close()


   def addAttendee(self, data):
      self.attendees.append(Attendee(data))


   def deleteAttendee(self, name):
      for i in range(len(self.attendees)):
         if self.attendees[i].getName() == name:
            self.attendees.pop(i)
            break


   def showInfo(self, name):
      currentAttendee = {}

      for attendee in self.attendees:
         if attendee.getName() == name:
            currentAttendee = attendee
            break

      if currentAttendee:
         attendeesData = currentAttendee.getData()
         for key in attendeesData.keys():
            print("  {}: {}".format(key.title(), attendeesData[key]))

      else:
         print("Attendee not found")


   def showNamesAndEmails(self, state=""):
      for attendee in self.attendees:
         if state:
            if attendee.getState() == state:
               print(" Name: {} ({})".format(attendee.getName(), attendee.getState()))
               print(" Email: {}\n".format(attendee.getEmail()))
         else:
            print(" Name: {} ({})".format(attendee.getName(), attendee.getState()))
            print(" Email: {}\n".format(attendee.getEmail()))


   def updateAttendeeFile(self):
      attendeeFile = open(self.path, "w")

      for attendee in self.attendees:
         print(attendee.getData(), file=attendeeFile)

      attendeeFile.close()
