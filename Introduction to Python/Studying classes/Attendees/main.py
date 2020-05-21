from AttendeeManager import AttendeeManager

def main():
   app = AttendeeManager()
   app.run()
   # app.addAttendee({
   #    "name": "Diego",
   #    "company": "None",
   #    "state": "PB",
   #    "email": "diego@cruz.com"
   # })
   # app.updateAttendeeFile()

   app.showNamesAndEmails()

main()
