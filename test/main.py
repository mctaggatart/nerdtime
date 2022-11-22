# This is a sample Python script.
import time
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
def ifelse_example(veracity):
    if veracity == True:
        print('True')
    else:
        print('False')
def while_example(reps):
    i = 0
    while i < len(reps):
        print(reps[i])
        i += 1
def for_example(fruits):
    for x in range(0,3,2):
        print(fruits[x])

def for_example_basic(fruits):
    for x in fruits:
        print(x)
def fizz_buzz (number):
    outstring = ""
    for y in range(number):
        outstring = ""
        if (y % 3 == 0):
            outstring = outstring+"Fizz"

        if (y % 5 == 0):
            outstring = outstring+"Buzz"

        print(y, ": ", outstring)
  #  fizzy=''
  #  for y in range(number):
      #  if(y%3==0):
       #    fizzy=('fizz')
           # print('fizz')
     #   if(y%5==0):
       #     print('buzz')
  #  print(fizzy)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  #  print_hi("PyCharm")
   # ifelse_example(True)
   #while_example(["apple", "banana", "cherry"])
   # start = time.time()
  #  x = input()
   # for_example_basic(x)
  #  fizz_buzz(16)
  for_example(["apple", "banana", "cherry"])
   # for_example(["goldendoodle", "banana", "cherry"])
   # for_example_basic("Caffiene")
   # end = time.time()
    #print("exec time", (end-start) * 10**3, "ms")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
