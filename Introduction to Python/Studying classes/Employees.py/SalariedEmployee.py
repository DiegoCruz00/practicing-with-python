from Employee import Employee

class SalariedEmployee(Employee):
   def setSalary(self, newSalary):
      self.salary = newSalary

   def getSalary(self, months):
      return self.salary * months

   def getSummary(self):
      summary = "Name: {}\n".format(Employee.getName(self))
      summary += "Age: {} years old\n".format(Employee.getAge(self))

      summary += "Monthly Salary: $ {}\n".format(self.getFormattedSalary())

      return summary

   def getFormattedSalary(self):
      salaryDollars = int(self.salary)
      salaryCents = (self.salary - salaryDollars) * 100

      salaryDollars = str(salaryDollars)

      salaryDollarsChr = []
      for number in salaryDollars:
         salaryDollarsChr.append(number)

      for i in range(len(salaryDollars) - 3, 0, -3):
         salaryDollarsChr.insert(i, " ")

      salaryDollars = "".join(salaryDollarsChr)

      return "{}.{:0>2}".format(salaryDollars, salaryCents)


emp1 = SalariedEmployee("Diego", 17)
emp1.setSalary(37000)

print(emp1.getSummary())
