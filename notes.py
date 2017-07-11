
#type python in terminal to get into python shell >>> to get out type exit()
# variables
name = "Robin";
num = 1;

# delete variable using del
del num;

#functions
print("Hello, World");

#indendtation should be 4 spaces
#blocks start with a colon
#variable and functions should all be lower case with no hyphens, just underscores

def answer_the_phone():
    greeting = "Hello there";
    print(greeting);

#integers are whole numbers. floats are decimal numbers
# >>> 0.1 + 0.1 + 0.1 - 0.3
# 5.551115123125783e-17
# >>> round(5.551115123125783e-17)

# int(5.9) => 5
# int(5.3) => 5
# int just chops off float portion. Does not round

#triple quotes to escape quotes
greeting = """Hello there my dad's friend"""
new_line = """Here's a new line

right here!"""

str(5);

status_message = "We have 8 people using the site right now."
status_message = "We hae {} people using the site right now."
print(status_message.format(7));

#Lists
my_list = [1 , 2, 3];
print(my_list + [4, 5])
my_list.extend([4,5])
list_in_list = [1, 2, 3, [4, 5, 6], 7];
list_in_list.remove([4, 5, 6])
print(list_in_list)

list("hello")
#split generally splits on spaces unless otherwise specified
"hello".split();
#join
flavors = ["mint", "chocolate", "strawberry"];
print(", ".join(flavors));

available = "banana split;hot fudge;cherry;malted;black and white"
sundaes = available.split(";")
print(sundaes)
display_menu = ", ".join(sundaes);
menu = "Our available flavors are: {}.".format(display_menu);

#index
"alpha".index('a');

##booleans
bool(True);
bool([]);
bool([1, 2, 3]);
bool(None);

5 == 5
5 != 7
5 < 7
7 >= 5

5 is 5
"a" is "b"
# is checks if they are in the same place in memory
# handy for checking if something is none
#checks if a num is none or falsey

c = [];
d = [];

c == d #true
c is d #false

#IF AND ELSE STATEMENTS
age = 5000;
if age > 1000:
  print("wow")
elif age >= 5000:
  print("right on");
else: 
  print("oh")








