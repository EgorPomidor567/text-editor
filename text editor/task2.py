import time

class Pupil:
    def __init__(self,surname,name,mark):
        self.surname = surname
        self.name = name
        self.mark = mark

pupils = []

def print_class(pupils):
    for pupil in pupils:
        print(pupil.surname, pupil.name, pupil.mark)
    print("\n")

def print_five():
    for pupil in pupils:
        if pupil.mark =="5":
            print(pupil.surname, pupil.name, "-", pupil.mark)
        print("\n")

def find_averange():
    average = 0
    for pupil in pupils:
        average += pupil.mark

        average /= len(pupils)

        print("Середня оцінка - ", average)

start time = time.time()

with open("pupils.txt" , "r" , encoding="UTF=8") as file;
    for line in file:
        data = line.split(" ")
        pupil = Pupil(data[0] , data[1], data[2])
        pupils.append(pupil)

print_class(pupils)
print_five
find_averange