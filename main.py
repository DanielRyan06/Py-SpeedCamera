#Imports required packages
import time
import re
import datetime

#Displays time on start
timer = datetime.datetime.now()
print(timer)

#Asks for the number plate then converts it to uppercase  
def main():
  number_plate = str(input("Input Number Plate (Type EXIT to quit.)\n"))
  plate = number_plate.upper()
  if plate == "EXIT":
    quit()
  print("Your selected Numberplate is", plate)

  #Checks to see if numberplate format is valid
  matched = re.match("[A-Z][A-Z][0-9][0-9][A-Z][A-Z][A-Z]", plate)
  is_match = bool(matched)
  
  if is_match ==  False:
    matched = re.match("[A-Z][0-9][0-9][0-9][A-Z][A-Z][A-Z]", plate)
    is_match = bool(matched)
    if is_match == False:
      print("Not a valid numberplate.")
      timer = datetime.datetime.now()
      f = open("log.txt", "a")
      f.write(str(timer)+" ")
      f.write(str(plate)+"\n")
      f.close()
      main()

  speed = int(input("What was the car's speed in mph?"))
  if speed > 70:
    timer = datetime.datetime.now()
    print("This person was speeding!")
    f = open("overspeed.txt", "a")
    f.write(str(timer)+" ")
    f.write(str(plate)+" ")
    f.write(str(speed)+"mph\n")
    f.close()
    main()
  main()
main()
