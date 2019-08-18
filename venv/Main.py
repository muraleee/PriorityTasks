from math import *

from Task import Task

class main:


    file1 = open("tasks.txt", "a")

    boole = True
    sel = -1
    Mlists = []
    Slists = []
    priority = -1
    save = -1
    while boole:
        print("\n1. Add a task to end of a list")
        print("2. Print tasks")
        print("3. Remove a task")
        print("4. Clear file")
        print("5. exit")
        sel = int(input("Select an option"))

        if sel == 1:
          print(" Task properties")
          name= input("what is the name of the task?")
          while priority < 0 or priority > 2 :
              try:
               priority = int(input("Press 1 for main task and 2 for side task."))
              except ValueError:
                  print("give an integer")

          a= Task(name, priority)
          if a.getPriority() == 1:
             Mlists.append(a)
          elif a.getPriority() == 2:
              Slists.append(a)

          while save == -1:
           save= input("Do you want to save changes? Press 1 to save")

          if save == 1:
            file1.write("-----")
            file1.write("Main Tasks")
            file1.



        elif sel== 4:
            file1.close()
            file1 = open("tasks.txt", "w")
            file1.write("")

        elif sel == 5:
            boole = False

    file1.close()
