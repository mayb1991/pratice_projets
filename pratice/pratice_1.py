def name(*fname):
    for first in fname:
        print("My name is " + first.title() + ".  \
        What is yours?")
  
name("brad", "bradley", "bradlee")


def family(mem_2, mem_3, mem_1):
    print("My Wife " + mem_2.title() + " is so pretty!")

family(mem_1= "brad", mem_2= "jessica", mem_3= "ezra")

def car_owned(**brand):
    print("I currlenty own 2 " + brand["make"])
car_owned(make = "toyota", model_1 = "rav4", model_2 = "cramy")


def my_name(fname = "Bradley"):
    print("My name is " + fname)
my_name("Jessica")
my_name("Brad")
my_name()


def my_foods_list (foods):
    for food in foods:
        print(food.title() + " is the best")
snacks = ["chips", "cookies", "brownies"]
healty_food = ["bananas", "cherries", "tamatos"]
my_foods_list(healty_food)

def my_return(x):
    return 15 * x

print(my_return(15))

def my_pass(lname):
    pass

def reuse(c):
    if c > 0:
        result = c + reuse(c -1)
        print(result)
    else:
        result = 0
    return result
print("My examples of recustion")
reuse(5)

past_cars = ["toyota", "huyinda", "crylister", "caddie", 
"pontic", "murcey", "honda"]
for car in past_cars:
    if car == "caddie":
        print('I had 22" on my ' + car.title())
    if car == "murcey":
        print(car.title() + " was the oldest car I ever ownd ")
    print(car)