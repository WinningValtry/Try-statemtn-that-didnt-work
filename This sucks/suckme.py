from tkinter import *
from tkinter.tix import Tk
root=Tk()
root.title("Error")
root.geometry("500x400")

listofthings=["melon", "peach", "eggplant", "banana"]
listofstuff={"name": "Netram",
"age":"12" }

try:
    {
        print(listofthings[5]):
  print(listofstuff["ligma"])
    }
except IndexError:
    print("Error", "This index does not exist")

except KeyError:
    print("Error", "This key does not exist")

root.mainloop()