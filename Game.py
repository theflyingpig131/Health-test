global salary
global dfa

salary = 0
dfa = 0
day = 32
money = 1000
ei = 0
sickdays = 0



def jobpick():
    global job
    print("1 = Warehouse worker")
    print("2 = Office secretary")
    print("3 = Waiter")
    tempjob = input(": ")
    if tempjob == "1":
      print()
      print("======== Warehouse Worker ========")
      print("         Salary = $11/h           ")
      print("Distance from apartment = 10 miles")
      print("    Amount of EI created = 20    ")
      print()
      print("1 = Pick Job")
      print("2 = go back to choices")
      jobchoice = input(": ")
      if jobchoice == "1":
        job = 1
        jobpicked()
      if jobchoice == "2":
        jobpick()
        print()
    if tempjob == "2":
      print()
      print("======== Office Secretary ========")
      print("         Salary = $10/h           ")
      print("Distance from apartment = 6 miles")
      print("   Amount of EI created = 12 ")
      print()
      print("1 = Pick Job")
      print("2 = go back to choices")
      jobchoice = input(": ")
      if jobchoice == "1":
        job = 2
        jobpicked()
      if jobchoice == "2":
        jobpick()
        print()
    if tempjob == "3":
      print()
      print("======== Waiter ========")
      print("  Salary = $5/h + tips"  )
      print("Distance from apartment = 2.5 miles")
      print("Amount of EI created = 5")
      print()
      print("1 = Pick Job")
      print("2 = go back to choices")
      jobchoice = input(": ")
      if jobchoice == "1":
        job = 3
        jobpicked()
      if jobchoice == "2":
        jobpick()
        print()
def main():
  print("Time to choose your job!")
  print("You may choose between 3 jobs")
  print()
  print("To get more info choose the job and more info will pop up.")
  jobpick()

def jobpicked():
  global job
  global salary
  
  if job == 1:
    salary = 11
    dfa = 10
  if job == 2:
    salary = 10
    dfa = 6
  if job == 3:
    salary = 5
    dfa = 2.5
  startday()


def startday():
  global day
  global money
  global points
  global ei
  global salary
  global sickdays
  points = money - ei/3 - sickdays * 10

  if day > -1 and money > 0:
    ei = ei + dfa * 2
    day = day - 1
    print()
    print()
    print("There are " + str(day) + " days left")
    print("You have $" + str(money))
    print("press enter to start the day")
    input()
    print()
    print()
    if day == 7 or day == 14 or day == 21 or day == 28:
      print("Pay day!")
      tempsalary = salary * 40
      print("You made " + str(tempsalary) + " dollars")   
      money = money + tempsalary
      startday()
    if day == 31:
      print()
      print("Rent Day!")
      print("Your total is $" + str(763))
      print("Press enter to pay")
      input()
      money = money -763
      startday()
    if day == 30:
      print("You wake up, not feeling well. You can either go to work, or stay home sick. But if you stay home sick, your salary will go down $.50. If you go to work your sick days will go up and they hurt you a lot in the end.")
      print("1 = Go to work")
      print("2 = stay home")
      sick = input(": ")
      if sick == "1":
        sickdays = sickdays + 1
        print("About 40 million private sector workers do not have paid sick days, meaning they have to go to work sick.")
      if sick == "2":
        salary = salary - .5
        print("About 40 million private sector workers fo not have paid sick days, meaning that they may lose their job.")
      startday()
    if day == 29:
      print("You have recovered from your sickness luckily, but you reallize you don't have enough food for dinner. You have to go to the grocery store.")
      print()
      print("======== Grocery Store ========")
      print("1 = Ramen, $1")
      print("2 = Box of spaghetti, $2.49")
      print("3 = Frozen Pizza, $8")
      print("4 = Frozen Chicken nuggets, $4")
      grocery = input(": ")
      money = money - grocery
      print("Nearly 18 million adults don't have enough food in the house every day.")
  else:
    print("Game over, you ended with a total of " + str(points) + " points")
